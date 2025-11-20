from orve import pika_superman

class pika_superman_pro(pika_superman):
    def __init__(self):
        super().__init__()
        self.hp = 5133

    def attack(self):
        super().attack()
        self.hp += 100
        print("self.hp:", self.hp)

if __name__ == "__main__":
    # pika_superman_pro1 = pika_superman_pro()
    print(f"觉醒皮卡超人 生命值: {pika_superman_pro().hp}")
    print(f"觉醒皮卡超人 攻击力: {pika_superman_pro().hurt}")    

    pika_superman_pro1 = pika_superman_pro()
    pika_superman_pro1.attack()
    pika_superman_pro1.display_info()