X = int(input())# candy weighs in grams
Y = int(input())# tangerine  weighs in grams
Z = int(input())# apple weighs in grams
W = int(input())# exact weight of gifts
Result = 0 # the number of gift options
# Getting the integer part of the division
c = W//X # maximum amount  of candy in gift
t = W//Y # maximum amount  of tangerine in gift
a = W//Z # maximum amount  of apple in gift
total = 0 #total weight in grams of gifts
# increase in the amount of candy to the maximum inclusive
for x in range(c+1):
    # increase in the amount of tangerine  to the maximum inclusive
    for y in range(t+1):
        # increase in the amount of apple to the maximum inclusive
        for z in range(a+1):
            total = x*X + y*Y + z*Z
            if W == total:
                Result +=1           
            total = 0
print('Result:', Result)