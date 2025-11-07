from typing import List 

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        """ 
        Since the power station in the i-th city covers the range [i-r,i+r], we can use a difference array to efficiently
        calculate the total power for each city.
        """
        cnt = [0] * (n + 1) #difference array (of size n+1 for boundary safety)
        
        # for each city i having stations[i] power stations.
        # each power station covers the range [i - r, i + r].
        # So, we increment cnt[left] and decrement cnt[right]
        
        for i in range(n):
            left = max(0 , i - r) # ensure we dont go out of bounds
            right = min(n , i + r + 1) # +1 cause right index is exclusive
            cnt[left] += stations[i]
            cnt[right] -= stations[i]
        
        def check(val: int) -> bool:
            """Helper function to check if we can ensure each city has at least val power."""
            diff = cnt.copy()
            total = 0
            remain = k # station we can add(new station we can make)
            
            for i in range(n):
                # Accumulate the prefix sum of the diff array to get the actual power
                total += diff[i]
                
                # if current city's total power is less than val
                if total < val:
                    # we need to add station
                    add = val - total
                    
                    # if we dont have enough to add then val is not possible
                    if remain < add:
                        return False
                    
                    # otherwise add these
                    remain -= add 
                    # Each new station we add at city (i + r) covers [i, i + 2r]
                    # So we reduce their contribution after the end of that range.
                    end = min(n , i + 2*r + 1)
                    diff[end] -= add 
                    # update total since we added new stations
                    total += add 
            
            return True 
        
        # Binary Search for the Maximum Minimum Power
        low , high = min(stations) , sum(stations) + k 
        ans = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            is_possible = check(val = mid)
            
            if is_possible:
                ans = mid 
                low = mid + 1
            else:
                high = mid - 1
        
        return ans 


sol = Solution()

print(sol.maxPower(stations = [1,2,4,5,0], r = 1, k = 2))