from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run.")

class Snake(Animal):
    def move(self):
        print("I can slither.")

class Fish(Animal):
    def move(self):
        print("I can swim.")

class Ant(Animal):
    def move(self):
        print("I can crawl.")


H = Human()
H.move()

S = Snake()
S.move()

F = Fish()
F.move()

A = Ant()
A.move()