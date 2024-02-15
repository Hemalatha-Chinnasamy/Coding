def SearchingChallenge(strArr):
    def dfs(matrix, i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == "1":
            return
        matrix[i][j] = "1"
        dfs(matrix, i + 1, j)
        dfs(matrix, i - 1, j)
        dfs(matrix, i, j + 1)
        dfs(matrix, i, j - 1)

    matrix = [list(row) for row in strArr]
    holes = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "0":
                holes += 1
                dfs(matrix, i, j)

    return holes

# Test cases
print(SearchingChallenge(raw_input()))
