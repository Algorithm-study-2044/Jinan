import bisect


class TimeMap:

    def __init__(self):
        # Dictionary to hold the key and a list of tuples (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Append the (timestamp, value) to the list for the key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or not self.store[key]:
            return ""

        # List of tuples (timestamp, value) for the key
        time_value_pairs = self.store[key]

        # Binary search to find the rightmost value less than or equal to the given timestamp
        i = bisect.bisect_right(time_value_pairs, (timestamp, chr(127)))

        if i == 0:
            return ""
        else:
            return time_value_pairs[i - 1][1]
