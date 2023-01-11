def ieee745(N): # ieee-745 bits (max 32 bit)
    a = int(N[0])        # sign,     1 bit
    b = int(N[1:9],2)    # exponent, 8 bits
    c = int("1"+N[9:], 2)# fraction, len(N)-9 bits

    return (-1)**a * c /( 1<<( len(N)-9 - (b-127) ))

N = "01000011011100010000000000000000"  # str of ieee-745 bits
print( ieee745(N)  )  # -->  -20.59375