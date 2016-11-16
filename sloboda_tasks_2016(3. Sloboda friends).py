N = int(input())#number of people in the company
S = int(input())# a specific number of person
Matrix= [] # create an empty matrix
Result = 0 # number of friends and friends of friends
Friends = [] # array of friends and friends of friends
# fill input data matrix
for i in range(N):
    Matrix.append([])
    for j in range(N):
        Matrix[i].append(int(input()))
# to add friends
for j in range(N):
    if Matrix[S][j]== 1:
        Friends.append(j)
        i = j
        # to add friends of friends
        for x in range(N):
            #don't add person with a specific number again
            if Matrix[i][x]== 1 and x != S:
                # don't add already added friends and friends of friends
                if Friends.count(x) !=1:
                    Friends.append(x)
Result = len(Friends)# to count friends and friends of friends
print('Result:', Result)
