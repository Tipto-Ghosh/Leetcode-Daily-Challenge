class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """ 
        As n can only contains 1 so
        we can start from 1 and then 11,111,1111 and so on, until we got n % k == 0
        As it can overflow so we can't use this approach.
        
        We can think like this:
        
        take n or curr = 1
        Try to divide it by k and store the remainder.
        
        To possible outcomes from the division:
        1. if remainder is 0 then return length if curr
        2. if remainder is something that we got previously then return -1 cause it not going to divisible.
        
        At each iteration update curr with this: curr = remainder * 10 + 1
        """
        
        remainder_set = set() # store the remainders
        curr = 1 # current n
        length = 1 # cause 1 has a length 1: len(1) = 1
        
        while True:
            # now find the remainder
            rem = curr % k 
            # update curr: curr = curr // k 
            curr //= k
            # if rem is 0 then we go our ans
            if rem == 0:
                return length
            # if rem is already present in remainder_set
            if rem in remainder_set:
                # return -1 cause it's not going to be divisible
                return -1
            
            # otherwise store it
            remainder_set.add(rem)
            
            # update curr
            curr = rem * 10 + 1
            length += 1
                 


sol = Solution()
print(sol.smallestRepunitDivByK(2))
print(sol.smallestRepunitDivByK(3))