from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.hist = [[(0,0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        arr = self.hist[index]
        # 같은 snap_id에서 여러 번 set되면 마지막 값만 남기기
        if arr[-1][0] == self.snap_id:
            arr[-1] = (self.snap_id, val)
        else:
            arr.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.hist[index]
        # (snap_id, +infty) 위치를 찾아서 그 바로 왼쪽이 snap_id 이하의 마지막 기록
        pos = bisect_right(arr, (snap_id, 10**18)) - 1
        return arr[pos][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)