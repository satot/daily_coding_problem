import unittest
from queue import Queue

def solve(arr:list[list[str]]) -> int:
    def bfs(arr, sx:int, sy:int) -> None:
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        q = Queue()
        q.put([sx, sy])
        while not q.empty():
            cx, cy = q.get()
            if arr[cx][cy] != " ":
                continue
            arr[cx][cy] = "#"
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == " ":
                    q.put([nx, ny])

    m, n = len(arr), len(arr[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == " ":
                bfs(arr, i, j)
                count += 1
    return count

class TestFunc(unittest.TestCase):
    def test1(self):
        arr = [
          ["\\", " ", " ", " ", " ", "/"],
          [" ", "\\", " ", " ", "/", " "],
          [" ", " ", "\\", "/", " ", " "],
        ]
        self.assertEqual(solve(arr), 3)

if __name__ == "__main__":
    unittest.main()
