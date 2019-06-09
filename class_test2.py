class Animal(object): #父類別
    def run(self):
        print('animal is running')
class Dog(Animal):#子類別
    def run(self):
        print('dog is running')
    def eat (self):
        print('eating...')    
    pass
class Cat(Animal):#子類別
    def run(self):
        print('Cat is running')
    pass
dog = Dog()
dog.run()
dog.eat()

Cat = Cat()
Cat.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))

print(isinstance(c, Animal))

b = Animal()
print(isinstance(b, Dog))

def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(Animal())

run_twice(Dog())
run_twice(Cat)