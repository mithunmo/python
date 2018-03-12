

prices = [2,5,7,3]
length = 5

dp = [ [0 for i in xrange(length+1)] for i in xrange(len(prices)+1)]
print dp

for i,val in enumerate(prices,start=1):
    #for j in xrange(length+1):
    #print i,val
    for j in xrange(1,length+1):
        if i <= j:
            dp[i][j] = max(dp[i-1][j], val + dp[i][j-i] )
        else:
            print i,j
            dp[i][j] = dp[i-1][j]
print dp



