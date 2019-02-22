##exercise
## Animal is a object
class Animal(object):
    pass

## Dog is a animal
class Dog(Animal):

    def __init__(self, name):
        ##Dog has a name
        self.name = name

## Cat is a animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name
        self.name = name

##Person is an object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has a pet of some kind
        self.pet = None

## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        ## Employee has a salary with some kind
        self.salary =salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(fish):
    pass

##Halibut is a fish
class Halibut(fish):
    pass

## rover is a Dog
rover = Dog("Rover")

##satan is a Cat
satan = Cat("Satan")

##Mary is a Person
mary = Person("Mary")

##mary has a pet called satan
mary.pet = satan

##Frank is an Employee has 120000 salary
frank = Employee("Frank", 120000)

##frank has a pet called rover ??
frank.pet = rover

##flipper is a fish
flipper = Fish()

##crouse is a Salmon
crouse = Salmon()

##harry is a Halibut
harry = Halibut()
