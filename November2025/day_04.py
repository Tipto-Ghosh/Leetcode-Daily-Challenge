from typing import List 
from collections import Counter
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = Counter(nums[ : k]) # find the frequency for 1st k elements
        
        def get_x_sum(freq)-> int:
            # create a max heap based on (-freq , -num)
            heap = [(-count , -val) for val , count in freq.items()]
            heapq.heapify(heap)
            
            total = 0
            count = 0
            while heap and count < x:
                f , v = heapq.heappop(heap)
                total += (-v) * (-f)
                count += 1
            
            return total
        
        ans = [get_x_sum(freq)]
        
        for i in range(k , n):
            out_element = nums[i - k]
            in_element = nums[i]
            
            freq[out_element] -= 1
            if freq[out_element] == 0:
                del freq[out_element]
            
            freq[in_element] += 1
            
            ans.append(get_x_sum(freq))
        
        return ans 

sol = Solution()
print(sol.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))