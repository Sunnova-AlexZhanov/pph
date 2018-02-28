
import inspect

def my_important_method():
    print("in " + inspect.getframeinfo(inspect.currentframe()).function)

def my_even_more_important_method(f):
    print("in my_even_more_important_method")
    f()

if __name__ == "__main__":
    my_even_more_important_method(my_important_method)