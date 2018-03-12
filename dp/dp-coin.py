

prices = [1,5,6,8]
length = 11

dp = [ [1000 for i in xrange(length+1)] for i in xrange(len(prices))]
print dp
for i in xrange(len(dp)):
    dp[i][0] = 0

print dp

for i,val in enumerate(prices,start=0):
    #for j in xrange(length+1):
    #print i,val
    for j in xrange(1,length+1):
        if i <= j:
            print i,j,val
            dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-val] )
        else:
            dp[i][j] = dp[i-1][j]
print dp



