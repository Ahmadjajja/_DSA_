class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ------------------------------------------------------------------
        # Example walkthrough (embedded as comments):
        #
        #   nums = [1, 1, 1, 2, 2, 3]
        #   k = 2
        # ------------------------------------------------------------------

        freq = Counter(nums)
        # freq = {1: 3, 2: 2, 3: 1}
        # (1 appears 3x, 2 appears 2x, 3 appears 1x)

        buckets = [[] for _ in range(len(nums) + 1)]
        # len(nums) = 6, so buckets has indices 0..6 (7 buckets total)
        #
        # Bucket index:   0    1    2    3    4    5    6
        #                 |    |    |    |    |    |    |
        # buckets    =   [ [], [], [], [], [], [], [] ]   <- before filling

        for key, count in freq.items():
            buckets[count].append(key)
            # key=1, count=3  -> buckets[3].append(1)  -> buckets[3] = [1]
            # key=2, count=2  -> buckets[2].append(2)  -> buckets[2] = [2]
            # key=3, count=1  -> buckets[1].append(3)  -> buckets[1] = [3]
            #
            # Final buckets:
            # Bucket index:   0    1    2    3    4    5    6
            #                 |    |    |    |    |    |    |
            # buckets    =   [ [], [3], [2], [1], [], [], [] ]

        res = []
        for count in range(len(buckets) - 1, 0, -1):
            # scan from index 6 down to index 1 (highest freq -> lowest freq)
            for key in buckets[count]:
                res.append(key)
                # count=6 -> buckets[6]=[]     -> res = []          (skip)
                # count=5 -> buckets[5]=[]     -> res = []          (skip)
                # count=4 -> buckets[4]=[]     -> res = []          (skip)
                # count=3 -> buckets[3]=[1]    -> res = [1]         (len=1)
                # count=2 -> buckets[2]=[2]    -> res = [1, 2]      (len=2 == k!)
                if len(res) == k:
                    return res
                    # returns [1, 2] here — matches expected top-2 result

        return res