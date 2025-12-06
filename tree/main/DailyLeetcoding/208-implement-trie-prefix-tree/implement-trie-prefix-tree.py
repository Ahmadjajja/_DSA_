# Each node in the Trie stores:
# 1. children: a map of char -> TrieNode
# 2. endOfWord: marks if a complete word ends at this node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


# Trie class to insert words, search words, and check prefixes
class Trie:
    def __init__(self):
        # Root is an empty node (does not store any character)
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        
        # Traverse each character in the word
        for c in word:
            # If character not present, create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            # Move to the next node
            cur = cur.children[c]
        
        # Mark the end of the word
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        
        # Traverse the Trie following the characters of the word
        for c in word:
            # If character path breaks, word does not exist
            if c not in cur.children:
                return False
            
            cur = cur.children[c]

        # Word exists only if endOfWord is True
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        # Same logic as search, but we don't require endOfWord
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        # If we never broke the path, prefix exists
        return True
        

