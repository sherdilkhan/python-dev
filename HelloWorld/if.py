
# if statements in pyhton

weight_str = input ('enter your weight: ')
pound_kg = input ('Enter "L" for Pound and "K" for KG: ')

l_k = pound_kg.upper() #remove case sensitivity

weight = float(weight_str)

if l_k [0] == 'K':
    print (f'your weight in Lb is: {(weight*2.2)} ')
elif l_k [0] == 'L':
    print (f'your weight in Kg is: {(weight/2.2)}')