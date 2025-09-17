arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []

def recur(idx, start):
    if idx == N:
        print(*path)
        return


    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(idx + 1, i + 1)
        path.pop()


recur(0, 0)
