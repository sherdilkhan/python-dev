
# while statement in python
# Guess Game for secret number in three tries

sec_num = '15'
i = 0

while i<3:
    num = input ('Please guess the seceret number from 0~15: ')
    if num == sec_num:
        print('You Won!')
    else:
        print ('Try Again')
        i+=1
        if i == 3:
            print ('you Failed!')