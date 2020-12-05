def test_num(number):
    try:
        float(number)
        print('This is a valid number.')
    except:
        print("Invalid number.")
test_num(5)