class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for word, cnt in counter.items():
            heapq.heappush(heap, (-cnt, word))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
