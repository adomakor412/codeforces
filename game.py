import sys

def solve(n, compartments):
    INF = sys.float_info.max
    
    # Initialize the dp table with maximum values
    dp = [[INF] * n for _ in range(n)]
    
    # Initialize the base cases (when i == j)
    for i in range(n):
        dp[i][i] = compartments[i][0]
    
    # Iterate over the compartment range
    for l in range(1, n):
        for i in range(n):
            j = (i + l) % n
            for k in range(i, i + l):
                p_sum = sum(compartments[x][1] for x in range(i, j+1))
                dp[i][j] = min(dp[i][j], dp[i][k % n] + dp[(k + 1) % n][j] + p_sum)
    
    # Calculate the minimum possible expected score for starting from any compartment
    min_expected_score = min(dp[i][(i + n - 1) % n] for i in range(n))
    
    return min_expected_score

# Read input
n = int(input())
compartments = []
for _ in range(n):
    ai, bi = map(int, input().split())
    compartments.append((ai, bi))

# Solve the problem
result = solve(n, compartments)

# Print the result
print("{:.10f}".format(result))

