#car game help menue example

from ast import While


print ('''
x----------------Main Menu-------------x
cntr ---> for Car Control
scr  ---> for score board
car  ---> for Car Model

''')

while (1):
    request = input ('Please input any of the above options: ')
    if 'cntr' in request:
        print ('''
        Key Up     ------ Accelerate
        Key Down   ------ Brake
        Key Left   ------ Left Steer
         ''')
    elif 'scr' in request:
        print ('''
        1st ---- Max
        2nd ---- Ham
        3rd ---- Lec
        ''')
    else:
        print ('command makes no sense')
    break





