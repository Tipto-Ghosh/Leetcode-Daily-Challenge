from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """ 
        Length 3-> so we dont care about the middle one. and left and right most chars must be same.
        If we take a letter M as the middle then we just have to find that does 1 same letter has both left and right side of M?
        To achive this we can go left using a loop and go right using another loop. => O(n^2)
        
        Instead of going both side for each letter, we count the left and right frequency.
        So we can use 2 hashmap to store the left and right frequencies.
        
        at each iteration we will take a char m and remove it from right and count sub-sequences
        then add m to left.
        But we dont need the freq of right chars cause.
        
        We have to use hashmap for right side cause we will remove one chars always so if set then 
        we will miss all the other frequencies also. But for left we can use set cause we are not
        removing anything from the left.
        """
        
        left_set = set()
        right_hashmap = Counter(s) # count all the freq of chars initially all the right side
        ans = set() # only the unique one's
        
        # now take each chars m as middle letter
        for m in s:
            # remove it from the right cause it's now the middle char
            right_hashmap[m] -= 1
            
            # now count the sub-seqences
            for c in left_set:
                if right_hashmap[c] > 0:
                    # we got same char in both left and right side
                    sub_seq = f"{c}{m}{c}"
                    # store it in ans
                    ans.add(sub_seq)
            
            # now m becomes the left chars so add there
            left_set.add(m)
        
        return len(ans)

sol = Solution()

print(sol.countPalindromicSubsequence("aabca"))
print(sol.countPalindromicSubsequence("adc"))
print(sol.countPalindromicSubsequence("bbcbaba"))