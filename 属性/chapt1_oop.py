class military:
    materials = "圣水"
    def __init__(self, occupation,rarity, hp, hurt,cost,target,movement_speed,attack_speed):
        self.occupation = occupation
        self.rarity = rarity
        self.hp = hp
        self.hurt = hurt
        self.cost = cost
        self.target = target
        self.attack_speed = attack_speed
        self.movement_speed = movement_speed
print(military.materials)
# military.hp -= 100
# military.materials = "阳光"
unit1 = military("knight","common",1462,167,3,"ground",2,1.2)
unit1.materials = "阳光"
print(unit1.materials)
unit2 = military("knight","common",1462,167,3,"ground",2,1.2)
print(unit2.materials)
unit3 = military("knight","common",1462,167,3,"ground",2,1.2)
print(unit3.materials)
unit4 = military("knight","common",1462,167,3,"ground",2,1.2)
print(unit4.materials)
