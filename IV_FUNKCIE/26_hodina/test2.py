import test1

print('I am in test2 file')
test1.my_fun()
if __name__ == '__main__':
    print('test2.py will run as standalone')
else:
    print('test2.py will run only when imported')

