class army:
    def __init__(self):
        self.rarity = "epic"
        self.hp = 3422
        self.hurt = 412
        self.cost = 7
        self.target = "ground"
        self.attack_speed = 1.8
        self.movement_speed = 1.0

    def attack(self):
        print("攻击")
        return self.hurt
    
    def take_damage(self, damage):
        self.hp -= damage

    def die(self):
        self.hp = 0
        print("饿啊！")

class pika_superman:
    cost = 7
    def __init__(self):
        self.rarity = "epic"
        self.hp = 3422
        self.hurt = 412
        self.cost = 7
        self.target = "ground"
        self.attack_speed = 1.8
        self.movement_speed = 1.0
        
    #静态方法
    @staticmethod
    def create(holy_water):
        if holy_water >= pika_superman.cost:
            print("咚咚，咚~~")
            print("创建了一个皮卡超人单位。")
            # print(self.rarity)
            return pika_superman()
        else:
            print("圣水不足，无法创建皮卡超人单位。")
            return None

    def display_info(self):
        print(f"职业: 皮卡超人, 稀有度: {self.rarity}, 生命值: {self.hp}, 伤害: {self.hurt}, 花费: {self.cost}, 目标: {self.target}, 移动速度: {self.movement_speed}, 攻击速度: {self.attack_speed}")

    def attack(self):
        print("bemm!")
        return self.hurt

    def take_damage(self, damage):
        self.hp -= damage
        print(f"皮卡超人 受到 {damage} 点伤害，剩余生命值: {self.hp}")

    def die(self):
        self.hp = 0
        print("皮卡超人:饿啊！")
        
if __name__ == "__main__":
    holy_water = 10
    # unit1 = pika_superman.create(holy_water)
    unit1 = pika_superman()
