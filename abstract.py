from abc import ABC, abstractmethod



class class_abstract(ABC):

    def print(self,x):
        print(f"Passed Value: {x}")

    @abstractmethod
    def task(self):
        print("We are inside class_abstract's task.")


class test_class(class_abstract):
    def task(self):
        print("We are inside test_class' task.")
    

test_obj = test_class()
test_obj.task()
test_obj.print(100)