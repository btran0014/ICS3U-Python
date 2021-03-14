def test_num(number):
    try:
        float(number)
        print('This is a valid number.')
    except:
        print("This is an invalid number.")
test_num(5)
test_num("bonk")