class Error(Exception):
    #base class for other exceptions
    pass
class ValueTooBigError(Error):
    #raise when the input is too large
    pass
class ValueTooSmallError(Error):
    #raise when the input is too small
    pass

while True:
    try:
        user_inp=float(input("What is your mark?: "))
        if  user_inp>100:
            raise ValueTooBigError
        elif user_inp<0:
            raise ValueTooSmallError
        break
    except ValueTooBigError:
        print("This value is too big! Try Again!\n")
    except ValueTooSmallError:
        print("This value is too Small! Try Again!\n")
print("Thank You!")