
import functools

def logme(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return wrapped


@logme
def myfunction():
    print("Doing some stuff")

if __name__ == "__main__":
    myfunction()