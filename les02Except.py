try:
    x = int(input('Input an integer: '))
    print(x)
except:
    print('Value not integer\n')
finally:
    print('Always execute this step.')