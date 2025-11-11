def RabinKarp(string, pattern):
    n = len(string)
    m = len(pattern)

    string_hash = 0
    pattern_hash = 0

    for i in range(m):
        string_hash += ord(string[i])
        pattern_hash += ord(pattern[i])

    for i in range(n - m + 1):
        if string_hash == pattern_hash:
            if string[i : i + m] == pattern:
                print("Match found at position: ", i)

        if i + m < n:
            string_hash -= ord(string[i])
            string_hash += ord(string[i + m])

string = "ABCBBBCBCBBACBABCBABC"
pattern = "ABC"

RabinKarp(string, pattern)

