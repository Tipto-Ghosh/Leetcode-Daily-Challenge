class Solution:
    def smallestNumber(self, n: int) -> int:
        
        binary_val = []
        decimal = n 
        while decimal != 0:
            b_digit = decimal % 2
            decimal //= 2
            binary_val.append(b_digit)
        
        # print(binary_val)
        
        # make all the 0 bit to 1
        
        for i in range(len(binary_val)):
            if binary_val[i] == 0:
                binary_val[i] = 1
        
        # print(binary_val)
        
        # now rebuild the decimal val
        ans = 0
        power = 0
        for b in range(len(binary_val) - 1 , -1 , -1):
            ans += (binary_val[i] * pow(2 , power))
            power += 1
        
        return ans 
            
        
        

sol = Solution()
print(sol.smallestNumber(5))
print(sol.smallestNumber(10))
print(sol.smallestNumber(3))