class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        start, end = 0, len(self.hashmap[key]) - 1

        while start <= end:
            mid = start + (end - start) // 2
            
            if self.hashmap[key][mid][1] == timestamp:
                return self.hashmap[key][mid][0]
            
            elif self.hashmap[key][mid][1] < timestamp:
                start = mid + 1
            else:
                end = mid - 1

        if end >= 0:
            return self.hashmap[key][end][0]
            
        return ""
