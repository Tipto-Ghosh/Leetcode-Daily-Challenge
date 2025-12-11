from typing import List
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        """  
        A building at position (x,y) is covered if:
          1. There exists another building at same row, left -> cordinate(x , y') where y' < y
          2. There exists another building at same row, right -> cordinate(x , y') where y < y'
          3. There exists another building at same row, above -> cordinate(x' , y) where x' < x
          4. There exists another building at same row, bellow -> cordinate(x' , y) where x' < x 
        
        For each build (x,y) task is to check if:
          a building with same x axis exists on Left and Right.
          a build with same y exists on Up and Down.
        
        So what if we store the all buildings with same rows and also same columns.
        
        row_map[x] = [all columns values(y) where buildings exist in row x]
        col_map[y] = [all rows values(x) where buildings exist in row y]
        
        Now for each building (x , y) check:
          1. in row_map[x], is there any value less than y(left)
          2. in row_map[x], is there any value greater than y(right)
          3. in col_map[y], is there any value less than x
          4. in col_map[y], is there any value greater than x
        If all these 4 condition is true for a building then building is convered otherwise not.
        
        
        This solution gives TLE for the last test case, need to optimize it.
        For a build (x , y) , We are checking 2 things:
           1. Is there any building at same y where x'< x < x" 
           2. Is there any building at same x where y' < y < y"
         So intead of storing all the values of x' and x" we can only store the min and max value.
         Same for the y values also.
        """
        
        # row_map = defaultdict(list)
        # col_map = defaultdict(list)
        
        # for x , y in buildings:
        #     row_map[x].append(y)
        #     col_map[y].append(x)
        
        # # sort values for binary searching instead of linear search
        # for key in row_map:
        #     row_map[key].sort()
        
        # for key in col_map:
        #     col_map[key].sort()
            
        # # count the covered building
        # covered = 0
        
        # for x , y in buildings:
        #     row_list = row_map[x]
        #     col_list = col_map[y]
            
        #     # check for left and right in the same column
        #     left_exists = any(c < y for c in row_list)
        #     right_exists = any(c > y for c in row_list)
            
        #     # check for above and bellow in the same row
        #     above_exists = any(c < x for c in col_list)
        #     bellow_exists = any(c > x for c in col_list)
            
        #     if left_exists and right_exists and above_exists and bellow_exists:
        #         covered += 1
            
        # return covered
        
        # --------------------------- Second Solution --------------------------------
        max_row = [0] * (n + 1)
        min_row = [n + 1] * (n + 1)
        max_col = [0] * (n + 1)
        min_col = [n + 1] * (n + 1)

        for p in buildings:
            x, y = p[0], p[1]
            max_row[y] = max(max_row[y], x)
            min_row[y] = min(min_row[y], x)
            max_col[x] = max(max_col[x], y)
            min_col[x] = min(min_col[x], y)

        covered = 0
        for p in buildings:
            x, y = p[0], p[1]
            if (x > min_row[y] and x < max_row[y] and y > min_col[x] and y < max_col[x]):
                covered += 1
        
        return covered 

sol = Solution()

print(sol.countCoveredBuildings(n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]))