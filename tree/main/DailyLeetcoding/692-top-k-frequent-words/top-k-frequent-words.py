class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        words.sort()
        initial_freq = {}
        for i in range(len(words)):
            word = words[i]
            if word in initial_freq:
                freq, index = initial_freq[word]
                initial_freq[word] = [freq + 1, index]
            else:
                initial_freq[word] = [1, i]
        
        cur_freq = {}
        for key, val in initial_freq.items():
            freq, index = val
            cur_freq[(-freq, index)] = key

        maxH = list(cur_freq.keys())
        heapq.heapify(maxH)
        res = []
        for _ in range(k):
            poppedElem = heapq.heappop(maxH)
            res.append(cur_freq[poppedElem])

        return res

        # tc -> O(nlogn) + O(n) + O(u) + O(u) + O(klogu) -> O(nlogn)
        # sc -> O(n) + O(u) + O(k) -> O(n)

        