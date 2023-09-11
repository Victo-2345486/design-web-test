def neighbors(arr, x, y, n):
    result = []
    row_start = max(0, x-n)
    row_end = min(len(arr)-1, x+n)
    col_start = max(0, y-n)
    col_end = min(len(arr[0])-1, y+n)
    for i in range(row_start, row_end+1):
        for j in range(col_start, col_end+1):
            result.append((i, j))
    return result