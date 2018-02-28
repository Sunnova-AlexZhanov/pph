from L2.base_class import BaseClass
import sys

class DerivedClass(BaseClass):

    my_var = "Hello World!"

    def __init__(self):
        super()._dont_call()

    @staticmethod
    def a_method():
        #print("var = " + str(self.my_var))
        pass

    def do_stuff(self):
        super().do_stuff()
        print("Do more stuff")

    def another_method(self):
        pass

    @staticmethod
    def some_static_method():
        print("in ",sys._getframe().f_code.co_name)

if __name__ == "__main__":

    o = DerivedClass()
    o.do_stuff()

    #DerivedClass.some_static_method()
