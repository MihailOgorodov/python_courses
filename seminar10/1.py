class Human: # класс
    sub_class = 'Человек'  # переменная класса, у всех объектов одинаковая
    def hello(self):  # метод класса
        return f'Тебя приветствует {self.name}'

    def __init__(self, name: str, age: int, weight: float = 100, height: float = 120): # объект класса
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


kiril = Human('Igor', 20)
sveta = Human('Sveta', 18)
print(kiril.name)
print(sveta.name)
print(kiril.hello())
print(sveta.hello())
