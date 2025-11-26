class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            # make freq hashmap
            fArr = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                fArr[index] += 1
            
            if tuple(fArr) in hashmap:
                hashmap[tuple(fArr)].append(s)
            else:
                hashmap[tuple(fArr)] = [s]

        ans = []

        for key in hashmap:
            ans.append(hashmap[key]) 
        
        return ans
        