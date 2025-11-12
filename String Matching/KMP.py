def lps(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] == 0
                i += 1

    return lps

def kmp(string, pattern):
    n = len(string)
    m = len(pattern)

    lps_table = lps(pattern)

    i, j = 0, 0

    while i < n:
        if string[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print("Pattern found at index: ", i - j)
            j = lps_table[j - 1]
        elif i < n and string[i] != pattern[j]:
            if j != 0:
                j = lps_table[j - 1]
            else:
                i += 1

string = "ABABDABACDABABCABAB"
pattern = "ABABC"

kmp(string, pattern)

