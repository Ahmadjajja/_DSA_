class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # len of strs ? 1 < > 10 ^ 4
        # len of each word ? 0 < > 100
        # letters type ? small
        # any duplicate letters in word ? No
        # len of strs -> m
        # len strs[i] -> n

        # sol 1 brute force -> O(n2) 
        # sol 2 efficient -> 

        # every word have 26 unique characters 

        # 0 - 25
        # freq -> ()
        # {
        #     (1, 0, 0, 0, 1, 0, 0, ...., 1, 0, 0) :  ['eat', 'tea', 'ate'],
        #     () : ['tan', 'nat'],
        #     () : ['bat'] 
        # }

        # # tc -> O(n), sc -> O(n)

        # 1. have hm
        freq_hm = {}

        # 2. loop over each elem, find freq and put in hm
        for word in strs:
            freq = [0] * 26
            for ch in word:
                ch_location = ord(ch) - ord('a')
                freq[ch_location] += 1
            
            freq_key = tuple(freq)
            print("freq_key : ", freq_key) 
            if freq_key in freq_hm:
                freq_hm[freq_key].append(word)
            else:
                freq_hm[freq_key] = [word]
        res = []
        for key, value in freq_hm.items():
            res.append(freq_hm[key])
        return res












        