from typing import List
from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # make a method to check anagram
        def is_anagram(word1: str , word2: str) -> bool:
            count1 = Counter(word1)
            count2 = Counter(word2)
            
            for key , val1 in count1.items():
                val2 = count2[key]
                if val1 != val2:
                    return False
            
            for key , val1 in count2.items():
                val2 = count1[key]
                if val1 != val2:
                    return False
            
            return True
        
        # store the indices these are removed
        is_removed = set()
        n = len(words)
        
        for i in range(n - 1 , 0 , -1):
            curr , prev = words[i] , words[i - 1]
            
            if is_anagram(curr , prev):
                # remove curr 
                is_removed.add(i)
        
        # build the answer without these indices that are present in is_removed
        ans = []
        for i in range(n):
            if i not in is_removed:
               ans.append(words[i])
        
        return ans 
    
sol = Solution()

print(sol.removeAnagrams(["abba","baba","bbaa","cd","cd"])) 
print(sol.removeAnagrams(["a","b","c","d","e"]))