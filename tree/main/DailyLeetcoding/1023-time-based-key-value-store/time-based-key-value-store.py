from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.key_to_entries = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_entries[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.key_to_entries[key]
        left, right = 0, len(entries) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            mid_timestamp, mid_value = entries[mid]

            if mid_timestamp <= timestamp:
                result = mid_value      # valid candidate, try to find a later (closer) one
                left = mid + 1
            else:
                right = mid - 1

        return result