class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # convert str digit into int digit
        arr = [ord(num) - ord('0') for num in s]
        
        while len(arr) != 2:
            temp = []
            for i in range(1 , len(arr)):
                num = (arr[i - 1]) + arr[i]
                num %= 10
                temp.append(num)
            arr = temp
        
        return arr[0] == arr[1]

sol = Solution()

print(sol.hasSameDigits('3902'))
print(sol.hasSameDigits('34789'))