class Clothes:
    def __init__(self, type):
        self.type = type
        self.isDirty = True
        self.isWet = False

    def clean(self):
        self.isDirty = False
        self.isWet = True
        print(f"{self.type} 已清洗干净。")

    def dry(self):
        if self.isWet:
            self.isWet = False
            print(f"{self.type} 已晾干。")

class WashingMachine:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.clothesInside = []
        self.running = False

    def load(self, clothes):
        if len(self.clothesInside) < self.capacity:
            self.clothesInside.append(clothes)

    def wash(self):
        self.running = True
        for c in self.clothesInside:
            c.clean()
        self.running = False
        print("洗衣机: 洗涤完成")

    def unload(self):
        clothes = self.clothesInside
        self.clothesInside = []
        return clothes

class Person:
    def __init__(self, name):
        self.name = name

    def putClothesIn(self, machine, clothes):
        machine.load(clothes)

    def startWash(self, machine):
        print("洗衣机: 洗衣服中...")
        machine.wash()
       

    def takeClothesOut(self, machine):
        return machine.unload()
    
if __name__ == "__main__":
    me = Person("EElyan")
    machine = WashingMachine(capacity=3)
    shirt = Clothes("shirt")

    me.putClothesIn(machine, shirt)
    me.startWash(machine)
    me.takeClothesOut(machine)

