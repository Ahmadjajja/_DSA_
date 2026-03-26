class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}
        for s in strs:

            freq = [0] * 26
            for ch in s:
                chIndex = ord(ch) - ord('a')
                freq[chIndex] += 1
            freq = tuple(freq)
            if freq in hm:
                hm[freq].append(s)
            else:
                hm[freq] = [s]

        print(list(hm.values()))

        return list(hm.values())

# tc -> O(n)
# sc -> O(n)