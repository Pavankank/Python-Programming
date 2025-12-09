class GParent:
    def GTalent(self):
        print("He is a musician")

class Parent(GParent):
    def GTalent(self):
        return super().GTalent()

class Child()