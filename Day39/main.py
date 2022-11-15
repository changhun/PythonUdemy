
MAX_N = 1001
n = int(input())

tile = [0] * MAX_N
tile[1] = 1
tile[2] = 3

for i in range(3, n+1):
    tile[i] = tile[i-1] + tile[i-2] * 2

print(tile[n])