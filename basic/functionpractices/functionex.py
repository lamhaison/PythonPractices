__author__ = 'root'


# Define function with default argument
# NOTE: default value always behind normal value
def show_args(a, b=20, c=30):
    print a
    print b
    print c


if __name__ == '__main__':

    # Call in case using default argument
    show_args(10)

    # Call function with full argument, don't use default value of argument
    show_args(10, 30, 40)


