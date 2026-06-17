class mob:
    def __init__(self, name):
        x = 0
        y = 0
        self.rec = 0
        self.name = name
        self.height = 10
        self.health = 20
        self.speed = 100
        self.pos = [x, y]

    def __str__(self):
        return f"{self.name}"

    def stats(self):
        return f"{'-' * 21} STATS {"-" * 22}\n{"-" * 50}\nHeight: {self.height}\nHealth: {self.health}\nSpeed: {self.speed}\nPosition: {self.pos}\n{"-" * 50}"

    def run(self, mts, dtn): #meters, direction (N, S, E, W)
        x, y = self.pos
        dtns = {
            'N': [1,  1],
            'S': [1, -1],
            'E': [0,  1],
            'W': [0, -1]
            }

        self.pos[dtns[dtn][0]] = self.pos[dtns[dtn][0]] + (dtns[dtn][1] * mts)
        self.rec = self.rec + mts
        return f"{self} ran {mts} meters to {self.pos}"

    def fatigue(self):
        ftg = (300 - self.rec)/300
        return f"{self} has {ftg} energy left"

dog = mob("Dog")
print(dog)
print(dog.stats())
print(dog.run(10, 'N'))
print("-" * 50)
print(dog.run(5, 'W'))
print("-" * 50)
print("New position:", dog.pos, )
print("-" * 50)
print(dog.fatigue())
print("-" * 50)
