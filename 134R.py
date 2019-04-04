import time
import random
while True :
    a=''
    for i in range(0,5):
        a=a+str(random.randint(0,9))
    print(a)
    time.sleep(1)
    b=input()
    if a==b:
        print('ugadal')
    elif not a==b:
        print('hah loh')


