class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjList = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)
        
        res = 1
        visit = set([beginWord])
        q = deque()
        q.append(beginWord)

        while q:
            qLen = len(q)
            for i in range(qLen):
                w = q.popleft()
                if w == endWord:
                    return res
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i + 1:]
                    for nei in adjList[pattern]:
                        if nei in visit:
                            continue
                        visit.add(nei)
                        q.append(nei)
            res += 1

        
        return 0

        