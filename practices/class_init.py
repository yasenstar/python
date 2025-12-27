class Fruit:
    def __init__(self):
        print('1')

class Apple(Fruit):
    def __init__(self):
        super().__init__()
        print('2')

obj1 = Apple()