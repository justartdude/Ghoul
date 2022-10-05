import time

a = 1000
b = 7
while a > b:
    a -= b
    print (f'{a}-{b}?')
    time.sleep (0.01)
print ('im GHOUL')