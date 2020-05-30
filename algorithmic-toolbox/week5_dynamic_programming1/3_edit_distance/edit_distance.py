# Uses python3
def edit_distance(s, t):
    # Initialize distance matrix
    dim_s = len(s) + 1
    dim_t = len(t) + 1
    dist = [[0 for _ in range(dim_t)] for _ in range(dim_s)]

    # Initialize 0-th row and 0-th column
    for i in range(1, dim_s):
        dist[i][0] = dist[i-1][0] + 1
    for j in range(1, dim_t):
        dist[0][j] = dist[0][j-1] + 1

    # Compute remaining elements
    for i in range(1, dim_s):
        for j in range(1, dim_t):
            candidates = [dist[i-1][j-1], dist[i-1][j] + 1, dist[i][j-1] + 1]
            if s[i-1] != t[j-1]:
                candidates[0] += 1
            dist[i][j] = min(candidates)
    return dist[dim_s-1][dim_t-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
