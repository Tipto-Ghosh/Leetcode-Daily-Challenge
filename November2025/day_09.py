class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operation_count = 0
        
        # while one of the number is not zero
        while num1 != 0 and num2 != 0:
            # if num1 > num2
            if num1 > num2:
                # substract num2 from num1
                num1 -= num2
            else: 
                # otherwise substract num1 from num2
                num2 -= num1
                
            operation_count += 1
        
        return operation_count

sol = Solution()
print(sol.countOperations(2 , 3))
print(sol.countOperations(10 , 10))