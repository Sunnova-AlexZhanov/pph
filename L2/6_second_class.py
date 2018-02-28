
"""Some helpful info about what this clas does."""
class MyFirstClass:

    var = "str"

    def not_very_important_method(self):
        pass

    def important_method(self):
        print("class : " + str(__class__))
        print("name : ", format(__name__) )
        print("doc : ", __doc__ )

if __name__ == "__main__":
    o = MyFirstClass()
    o.important_method()