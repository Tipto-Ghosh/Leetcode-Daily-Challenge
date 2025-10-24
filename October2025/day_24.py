class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        UPPER_RANGE = 1224444
        
        for num in range(n + 1 , UPPER_RANGE + 1):
            # count the occurrences digits in number     
            freq = {}
            num_str = str(num)
            for d in num_str:
                d = ord(d) - ord('0')
                freq[d] = freq.get(d , 0) + 1
            
            # now check every digit d has d occurrences
            ans = True 
            for key , val in freq.items():
                if key != val:
                    ans = False
                    break
            
            if ans:
                return num

sol = Solution()

print(sol.nextBeautifulNumber(1))
print(sol.nextBeautifulNumber(1000))
print(sol.nextBeautifulNumber(3000))
print(sol.nextBeautifulNumber(748601))