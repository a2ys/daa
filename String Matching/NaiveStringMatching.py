def naive(string, pattern):
    n = len(string)
    m = len(pattern)

    for i in range(n - m + 1):
        if string[i : i + m] == pattern:
            print("Match found at position: ", i)

string = "ABCBBBCBCBBACBABCBABC"
pattern = "ABC"

naive(string, pattern)

