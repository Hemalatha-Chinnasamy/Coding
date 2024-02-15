def StringChallenge(strParam):

    # code goes here
    max_unique_chars = 0
    for i in range(len(strParam)):
        for j in range(i + 1, len(strParam)):
            if strParam[i] == strParam[j]:
                unique_chars = len(set(strParam[i + 1:j]))
                max_unique_chars = max(max_unique_chars, unique_chars)
    return max_unique_chars

# keep this function call here
print StringChallenge(raw_input())
