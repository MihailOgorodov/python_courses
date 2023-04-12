class Contact:
    def __init__(self, name: str, phone: str, comment: str = ''):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):  # метод, который вызывается и возвращает значение, когда объект закладываем в print
        return f'{self.name} | {self.phone} | {self.comment}'  # то, как мы хотим распечатать


stone = Contact('Кирилл', '87984613132')  # создан объект класса Contact
print(stone)
