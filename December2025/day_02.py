from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """ 
        ### What the problem actually want?
            A horizontal trapezoid is any quadrilateral that 
            has at least one pair of opposite sides parallel to the 
            x-axis -> meaning both of those sides are horizontal.
            
            * A side is horizontal to x-axis when both points have the 
              same y-coordinate.
            
            * So the problem becomes:
              Pick 4 points such that:
              - 2 points lie on some height y1(making to top/bottom horizontal edge)
              - 2 points line on some different height y2(making another horizontal edge)
            
        ### Observations:
          1. If a height y contains p points, how many horizonatal segments can we make from that height?
                 
            edges count = (p*(p-1)) / 2
            Let's call it edges[y] means count of edges at height y
          
          2. How 2 horizontal edges form a Trapezoid
            A trapezoid requires two horizontal edges from two different heights:
               - choose one horizontal edge from height y1
               - choose one horizontal edge from another height y2
            
            Total trapezoids = edges[y1] * edges[y2] for all pair of heights (y1,y2)
        
        ### Steps need to do:
            1. Count points per height
            2. For each height find number of horizontal edges
            3. Add trapezoids formed with all previous heights means find
               edges count = (p*(p-1)) / 2
            4. Update total for next pair of heights(iteration)
        
        ### Time Complexity: O(n) cause traversing all the points
        ### Space Complexity: O(n) cause storing all the points in a map
        """
        mod = 10**9 + 7 
        point_num = defaultdict(int) # num of edges at height y
        ans = 0  
        total_sum = 0 # count of total number of horizontal edges formed at all heights so far
        
        # step-1: count points per height: means count of points that has same y
        for x , y in points:
            point_num[y] += 1 # count of points at height y
        
        # step-2: For each height y, compute horizontal egdes
        for point_count in point_num.values(): # point_count-> count of points at height y
            # count the num of edges at height y with p points
            edges_count = point_count * (point_count-1) // 2
            # step-3: find the trapezoid that can be formed with these edges
            # Total trapezoids = edges[y1] * edges[y2] for all pair of heights (y1,y2)
            total_trapezoids = edges_count * total_sum
            # add trapezoids formed with all previous heights
            ans = (ans + total_trapezoids) % mod 
            # step-4: Update total sum
            total_sum = (total_sum + edges_count) % mod 
        
        return ans 
    
sol = Solution()

print(sol.countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]]))            