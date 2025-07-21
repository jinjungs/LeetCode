from collections import deque

def chebyshev_dist(a, b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

def is_possible(grid, D):
    n, m = len(grid), len(grid[0])
    q = deque()
    visited = [[False]*m for _ in range(n)]

    # 현재 센터에서 D 이하인 지점은 커버 가능
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j, 0))
                visited[i][j] = True

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

    while q:
        x, y, d = q.popleft()
        if d == D:
            continue
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, d+1))

    # 커버 안 되는 칸들 수집
    uncovered = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                uncovered.append((i,j))

    if not uncovered:
        return True  # 기존 센터로 커버 가능

    # 커버 안 되는 애들이 하나의 정사각형 (2D+1) 안에 들어갈 수 있는지?
    min_x = min(i for i, j in uncovered)
    max_x = max(i for i, j in uncovered)
    min_y = min(j for i, j in uncovered)
    max_y = max(j for i, j in uncovered)

    return max(max_x - min_x, max_y - min_y) <= 2*D


def minimize_inconvenience_optimized(grid):
    n, m = len(grid), len(grid[0])
    low, high = 0, n + m  # 최대 거리 제한

    while low < high:
        mid = (low + high) // 2
        if is_possible(grid, mid):
            high = mid
        else:
            low = mid + 1

    return low


grid = [
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]

print(minimize_inconvenience_optimized(grid))  # 출력: 1