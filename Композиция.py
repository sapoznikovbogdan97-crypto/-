class Owner:
    class Pet:
        def __init__(self,name):
            self.name = name
            self.__mood = 0
            self.__hunger = 100

        def get_mood(self):
            return self.__mood

        def get_hunger(self):
            return self.__hunger

        def feed(self):
            self.__hunger += 1
            self.__mood += 1

        def play(self):
            self.__hunger -= 1
            self.__mood += 1

        def speak(self):
            pass

    class Cat(Pet):
        def __init__(self, name):
            super().__init__(name)
            self.kind = "cat"

        def speak(self):
            print("Мяу!")

    class Pig(Pet):
        def __init__(self, name):
            super().__init__(name)
            self.kind = "pig"

        def speak(self):
            print("Хрю!")

    class Raven(Pet):
        def __init__(self, name):
            super().__init__(name)
            self.kind = "raven"

        def speak(self):
            print("Кар!")

    class Dog(Pet):
        def __init__(self, name):
            super().__init__(name)
            self.kind = "dog"

        def speak(self):
            print("Гав!")

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def feed_all(self):
        for pet in self.pets:
            if pet.get_hunger() < 100:
                pet.feed()
                print("голод питомцев уменьшен на 1")
            elif pet.get_hunger() == 100:
                print("питомецы не хотят есть")

    def play_with_all(self):
        for pet in self.pets:
            if pet.get_hunger() > 0:
                pet.play()
                print("настроение питомцев увеличено на 1")
            elif pet.get_hunger() == 0:
                print("питомецы голодны и не могут играть")

    def get_info(self):
        for pet in self.pets:
            print(pet.name,"Настроение:",pet.get_mood())
            print(pet.name,"Сытость:",pet.get_hunger())

owner1 = Owner("Бяша","12")
owner2 = Owner("Рома","12")
cat = owner1.Cat("Барсик")
pig = owner1.Pig("Жорик")
dog = owner2.Dog("Дружок")
raven = owner2.Raven("Невер")
owner1.add_pet(cat)

def menu():
    print("1 - Покормить всех питомцев хозяина")
    print("2 - Поиграть со всеми питомцами")
    print("3 - Показать информацию")
    print("4 - Питомцы говорят!")
    choice = input("ваш выбор:").strip()

    if choice == "1":
        owner1.feed_all()
    elif choice == "2":
        owner1.play_with_all()
    elif choice == "3":
        owner1.get_info()
    elif choice == "4":
        for pet in owner1.pets:
            pet.speak()
menu()