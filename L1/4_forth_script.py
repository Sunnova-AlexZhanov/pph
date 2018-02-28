import sys


def my_important_method():
    print("in my_important_method" )

def my_even_more_important_method():
    print(sys._getframe().f_code.co_name)

if __name__ == "__main__":
    my_even_more_important_method()
    print("par =  " + str(sys.argv[0]))