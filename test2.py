import cv2
import numpy as np
import math

class Armor:
    def __init__(self, rect1, rect2):
        self.rect1 = rect1
        self.rect2 = rect2

class ArmorDetector:  # 定义检测器类
    def __init__(self):
        self.img_resized = None
        self.img_binary = None
        self.drawn_img = None
        self.rects = []
        self.armors_center = []
        self.armors = []


    def process_img(self,img, val):
        """处理图像，返回二值图像、调整大小和亮度的图像"""   
        self.img = img 
        self.img_resized = cv2.resize(img, (640, 480))  # 调整图像大小
        self.img_resized = cv2.convertScaleAbs(self.img_resized, alpha=0.3)  # 调整亮度
        img_gray = cv2.cvtColor(self.img_resized, cv2.COLOR_BGR2GRAY)  # 转为灰度图
        _, self.img_binary = cv2.threshold(img_gray, val, 255, cv2.THRESH_BINARY)  # 二值化处理
        # cv2.imshow("Binary Image", self.img_binary)  # 显示二值图像
        return self.img_resized, self.img_binary 
    
    def adjust(self,rect):
        c, (w, h), angle = rect
        if w > h:
            w, h = h, w
            angle = (angle + 90) % 360
            angle = angle - 360 if angle > 180 else angle - 180 if angle > 90 else angle
        return c, (w, h), angle
    
    def find_light(self):
        contours, _ = cv2.findContours(self.img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.rects = []
        for contour in contours:
            rect = cv2.minAreaRect(contour)
            area = cv2.contourArea(contour)
            if area < 5:
                continue
            rect = self.adjust(rect)
            (cx, cy), (w, h), angle = rect
            if h/w > 2.5:
                if -35 < angle < 35:
                    box = cv2.boxPoints(rect)
                    box = np.int64(box)
                    self.rects.append(rect)
                    # cv2.drawContours(self.img_resized, [box], 0, (0, 255, 0), 2)
        # cv2.imshow('Detected Rotated Rectangles', self.img_resized)
        return self.img_resized, self.rects
    def is_close(self,rect1, rect2, light_angle_tol, line_angle_tol, height_tol, width_tol, cy_tol):
        (cx1, cy1), (w1, h1), angle1 = rect1
        (cx2, cy2), (w2, h2), angle2 = rect2
        distance = math.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)
        if distance > 20:
            angle_diff = min(abs(angle1 - angle2), 360 - abs(angle1 - angle2))
            if angle_diff <= light_angle_tol:
                if abs(h1 - h2) <= height_tol and abs(w1 - w2) <= width_tol:
                    line_angle = math.degrees(math.atan2(cy2 - cy1, cx2 - cx1))
                    if line_angle > 90:
                        line_angle -= 180
                    elif line_angle < -90:
                        line_angle += 180
                    if (abs(line_angle - angle1) <= line_angle_tol or abs(line_angle - angle2) <= line_angle_tol or abs(cy1 - cy2) < cy_tol):
                        return True
        return False

    def is_armor(self,lights, light_angle_tol=5, line_angle_tol=7, height_tol=10, width_tol=10, cy_tol=5):
        self.lights_matched = []
        processed_indices = set()
        lights_count = len(lights)
        for i in range(lights_count):
            if i in processed_indices:
                continue
            light1 = lights[i]
            close_lights = [j for j in range(lights_count) if j != i and self.is_close(light1, lights[j], light_angle_tol, line_angle_tol, height_tol, width_tol, cy_tol)]
            if close_lights:
                group = [light1] + [lights[j] for j in close_lights]
                self.lights_matched.append(group)
                processed_indices.update([i] + close_lights)
        self.armors = []
        for light_matched in self.lights_matched:
            if light_matched:
                points = np.concatenate([cv2.boxPoints(light) for light in light_matched])
                armor_raw = cv2.minAreaRect(points)
                if 200 <= armor_raw[1][0] * armor_raw[1][1] <= 11000:
                    armor_flit = self.adjust(armor_raw)
                    if 1 <= armor_flit[1][1] / armor_flit[1][0] <= 3.5:
                        self.armors.append(self.adjust(armor_flit))
        self.armors_center = []
        for armor in self.armors:
            center, (width, height), angle = armor
            max_size = max(width, height)
            box = cv2.boxPoints(((center[0], center[1]), (max_size, max_size), angle)).astype(int)
            (center_x, center_y) = map(int, armor[0])
            armor_center = (center_x, center_y)
            self.armors_center.append(armor_center)
        return self.armors_center
    
    def detector(self,img_raw):
        self.process_img(img_raw,65)
        self.drawn_img, rects = self.find_light()
        armors_center = self.is_armor(rects)
        self.display_results()
        return armors_center
    
    def draw_lights(self):
        for rect in self.rects:
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            cv2.drawContours(self.drawn_img, [box], 0, (0, 255, 0), 2)
    def draw_armors(self):
        for armor in self.armors:
            center, (width, height), angle = armor
            max_size = max(width, height)
            box = cv2.boxPoints(((center[0], center[1]), (max_size, max_size), angle)).astype(int)
            cv2.drawContours(self.drawn_img, [box], 0, (255, 0, 255), 2)
            cv2.circle(self.drawn_img, (int(center[0]), int(center[1])), 5, (255, 0, 255), -1)
            (center_x, center_y) = map(int, armor[0])
            cv2.putText(self.drawn_img, f"({center_x}, {center_y})", (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 255, 255), 1)  # 在图像上标记坐标


    def display_results(self):
        self.draw_lights()
        self.draw_armors()
        cv2.imshow("Results", self.drawn_img)

if __name__ == "__main__" :
    img_raw = cv2.imread("D:\\100-Work\\sb.png")
    detector = ArmorDetector()
    armors_center = detector.detector(img_raw)
    print(armors_center)
    cv2.waitKey(0)
    cv2.destroyAllWindows()