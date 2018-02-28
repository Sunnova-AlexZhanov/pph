
class BaseClass():

    bc_var = None

    #def __new__(cls, *args, **kwargs):
    #    print("BaseClass::__new__")
    #    return super(BaseClass, cls).__new__(cls)

    def __init__(self, i_par):
        print("BaseClass::__init__ " + str(i_par))
        self.bc_var = "x"
        self.__setattr__("argh", "darn")

    def __call__(self, *args, **kwargs):
        print("BaseClass::__call__")


    def do_stuff(self):
        print("BaseClass::do_stuff " +  str(self.bc_var))
        print("Class = " + str(self.__class__))
        print("Class = " + str(type(self)))
        keys = self.__dict__.keys()
        values = self.__dict__.values()
        for key in keys:
            print("key = " + str(key))
        for value in values:
            print("value = " + str(value))

    def _dont_call(self):
        print("BaseClass::dont_call " +  str(self.bc_var))


if __name__ == "__main__":

    o = BaseClass('y')
    o.do_stuff()
    o._dont_call()
    o()