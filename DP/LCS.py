def LCS(X, Y):
    n = len(X)
    m = len(Y)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    i, j = n, m
    seq = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            seq.append(X[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        
    seq.reverse()
    
    return dp[n][m], ''.join(seq)

X = "ABCBDAB"
Y = "BDCABA"

length, sequence = LCS(X, Y)
print(length)
print(sequence)

