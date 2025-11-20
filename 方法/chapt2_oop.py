import time
class military:
    materials = "圣水"
    def __init__(self, occupation,rarity, hp, hurt,cost,target,movement_speed,attack_speed, attack_voice):
        self.occupation = occupation
        self.rarity = rarity
        self.hp = hp
        self.hurt = hurt
        self.cost = cost
        self.target = target
        self.attack_speed = attack_speed
        self.movement_speed = movement_speed
        self.attack_voice = attack_voice
    
    def display_info(self):
        print(f"职业: {self.occupation}, 稀有度: {self.rarity}, 生命值: {self.hp}, 伤害: {self.hurt}, 花费: {self.cost}, 目标: {self.target}, 移动速度: {self.movement_speed}, 攻击速度: {self.attack_speed}")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.occupation} 受到 {damage} 点伤害，剩余生命值: {self.hp}")

    def attack(self):
        # print(f"{self.occupation} 攻击 {target}，造成 {self.hurt} 点伤害")
        if self.hp > 0:
            print(self.attack_voice)
            return self.hurt
    
    def die(self):
        print(f"饿啊！")

    def live(self,damage = 0):
        if self.hp > 0:
            time.sleep(0.1)
            self.take_damage(damage)
            print(f"活着真好！")
        else:
            self.die()

  
unit1 = military("knight","common",1462,167,3,"ground",2,1.2, "啊哈！")
# unit1_b = military("knight","common",1462,167,3,"ground",2,1.2, "啊哈！")
king_hp = 5000



# while king_hp > 0:
#     if unit1.hp > 0:
#         king_hp -= unit1.attack()
#         unit1.take_damage(100)
#         print(f"国王剩余生命值: {king_hp}")
#     else :
#         unit1.die()
#         break
#     # unit1.live(50)

# print("战斗结束")