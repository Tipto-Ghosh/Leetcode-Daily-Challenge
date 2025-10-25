class Solution:
    def totalMoney(self, n: int) -> int:
        prev_monday_money = 1
        prev_day_money = 1
        next_monday = 7
        
        total_money = 0
        
        for day in range(n):
            # check if monday
            if day == next_monday:
                prev_day_money = prev_monday_money + 1
                next_monday += 7
                prev_monday_money += 1
            # add 1 dollar extra each day
            
            total_money += prev_day_money
            prev_day_money += 1
        
        return total_money
        
        
    
sol = Solution()
print(sol.totalMoney(4))
print(sol.totalMoney(10))
print(sol.totalMoney(20))