class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            # make freq hashmap
            fArr = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                fArr[index] += 1

            hashmap[tuple(fArr)].append(s)
        
        return list(hashmap.values())

# tc: O(n)
# sc: O(n)