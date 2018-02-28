
class MyFirstClass:

    my_value = None

    def not_very_important_method(self):
        pass

    def important_method(self):
        print("class : " + str(__class__))
        print("name : ", format(__name__) )