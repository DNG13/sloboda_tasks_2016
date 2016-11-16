N  = int(input())# copies of the same document
x = int(input())# the time in seconds to copy the list of paper for the first Xerox 
y = int(input())# the time in seconds to copy the list of paper for the second Xerox 
Result = 0 # the minimum time in seconds required for the preparation of N copies.
fastest = 0 # the time in seconds to copy the list of paper for the fastest Xerox
slowest = 0 # the time in seconds to copy the list of paper for the slowest Xerox
#find out which Xerox is faster
if x>y:
    fastest = y
    slowest = x
elif x<=y:
    fastest = x
    slowest = y
# do not need to do any copy
if N == 0:
    print('Result:', Result)
# need to do only one copy
elif N == 1:
    Result = fastest
    print('Result:', Result)
else:
    # make the first copy  to use both Xerox machine at the same time    
    N -= 1
    Result += fastest
    # how many times faster
    times = slowest/fastest
    # to use both Xerox machine at the same time   
    if slowest%fastest == 0:
        while N >= (times + 1):
            N -= (times + 1)
            Result += slowest
        while N > 0:
            N -= 1
            Result += fastest 
        print('Result:', Result)
    # for remainder of the division
    else:
        timer = 0 # to count time for slowest Xerox machine 
        while N > 0:
            N -= 1
            Result += fastest
            timer += fastest
            if timer >= slowest and N > 0:
               timer  %= slowest 
               N -= 1
        print('Result:', Result)
raw_input() 