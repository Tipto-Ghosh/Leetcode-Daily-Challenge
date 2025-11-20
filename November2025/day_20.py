from typing import List 

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # sort based on end value in ascending and if ties then start value in descending
        intervals.sort(key = lambda x: (x[1] , -x[0]))
        
        # Largest 2 chosen numbers till now
        chosen = []
        
        # track the last 2 picked numbers
        for start , end in intervals:
            # count how many chosen numbers are already inside this interval
            count = 0
            if chosen and chosen[-1] >= start:
                count += 1
            if len(chosen) >= 2 and chosen[-2] >= start:
                count += 1
            # If fewer than 2 numbers are inside the interval, add new ones
            if count == 0:
                # Add the last two values: end-1 and end
                chosen.append(end - 1)
                chosen.append(end)
            elif count == 1:
                # Add one more: end
                chosen.append(end)
            # If cnt == 2, we are already fine
        
        return len(chosen)
            
            
    
sol = Solution()
print(sol.intersectionSizeTwo([[1,3],[3,7],[8,9]]))
print(sol.intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))
print(sol.intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))
print(sol.intersectionSizeTwo([[1,4],[2,3],[1,5],[1,3]]))