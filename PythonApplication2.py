import math
def hex_to_bigendian (hex):
    V = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    l = len(hex)
    value = 0
    for i in range(0, l):
        value = value + (16**(l - i - 1))*(V.index(hex[i]))
    return value 

def hex_to_littelendian (hex):
    V = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    l = len(hex)
    value = 0
    for i in range(0, l):
        value = value + (16**(i))*(V.index(hex[i]))
    return value 

def bigendian_to_hex_ (big, ex):
    V = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if big == 0:
        return ex*'0'
    else:
        a = 1;
        i = 0;
        while a <= big/16:
            a = a*16
            i = i+1
        b = int(big/a)
        return V[b] + bigendian_to_hex_ (big - a*b, i)

def bigendian_to_hex (big):
    return bigendian_to_hex_ (big, 1)


def littelendian_to_hex (littel):
    hex = bigendian_to_hex_ (littel, 1)
    return hex[::-1]


print(hex_to_bigendian('3F'))
print(hex_to_littelendian('F3'))
print (littelendian_to_hex (63))
print (bigendian_to_hex (63))