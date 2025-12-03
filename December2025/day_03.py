from typing import List 
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """ 
        ### What the problem actually wants?
        A trapezoid is a convex quadrilateral that has at least one pair of parallel sides.
        It does NOT need to be horizontal.The parallel sides can have any slope.

        A trapezoid is formed by:
          - Choosing two line segments that have:
                - same slope  (parallel)
                - different intercepts (not collinear)
          - Connecting their endpoints (4 distinct points)

        BUT:
        Parallelograms must NOT be counted
        Parallelograms also have a pair of parallel sides, but they
        must be excluded.

        The major idea:
          1) Count all pairs of segments that are parallel.
          2) Subtract all parallelograms.

        ============================================================
        ### Observations

        ------------------------------------------------------------
        1. Counting trapezoid candidates (parallel non-collinear segments)
        ------------------------------------------------------------
        For any slope k:

            Segments with the SAME SLOPE are parallel.

        But we only want segments that do NOT lie on the same infinite line.
        So we also compare their **intercept b**.

        If a slope k has b groups with counts:
            c1, c2, c3, ...

        Then number of parallel pairs from this slope:
            sum over i < j:  c_i * c_j

        This counts all pairs of parallel non-collinear edges.
        Each such pair → exactly one trapezoid.

        ------------------------------------------------------------
        2. How to detect and subtract parallelograms?
        ------------------------------------------------------------
        A quadrilateral is a parallelogram **iff** its diagonals
        share the same midpoint.

        That means:
            If two segments have same midpoint but different slope,
            they are diagonals of a parallelogram.

        For each midpoint M, slopes occur with counts:
            d1, d2, d3, ...

        Parallelograms = sum over i < j: d_i * d_j

        We subtract this amount from our trapezoid count.

        ============================================================
        ### Steps Needed:
        ------------------------------------------------------------
        1. For every pair of points:
              - compute slope k
              - compute intercept b
              - compute midpoint key

           Store:
              slope_to_intercept[k].append(b)
              mid_to_slope[midpoint].append(k)

        2. For each slope k:
              group by intercepts (b values)
              count trapezoid candidates

        3. For each midpoint:
              group by slopes
              count parallelograms and subtract

        ============================================================
        ### Time Complexity: 
            O(n^2)    (all point pairs)

        ### Space Complexity:
            O(n^2)    (store slopes/intercepts for each pair)
        ============================================================
        """

        n = len(points)
        INF = 10**9 + 7  # for vertical slope
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        ans = 0

        # STEP 1: Build all possible segments
        for i in range(n):
            x1 , y1 = points[i]

            for j in range(i + 1, n):
                x2 , y2 = points[j]
                
                # Find the dx and dy 
                dx = x1 - x2
                dy = y1 - y2

                # slope and intercept of the line
                if x1 == x2:
                    k = INF           # vertical slope
                    b = x1           # x-intercept (unique)
                else:
                    k = (y2 - y1) / (x2 - x1)
                    # same as y = kx + b  =>  b = y - kx
                    b = (y1 * dx - x1 * dy) / dx

                # midpoint key
                # (x1+x2, y1+y2) uniquely defines midpoint
                mid = (x1 + x2) * 10000 + (y1 + y2)

                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)

        # STEP 2: Count trapezoid candidates
        #   (pairs of parallel non-collinear segments)
        for intercept_list in slope_to_intercept.values():

            if len(intercept_list) == 1:
                continue  # only 1 segment -> cannot form pair

            # count how many segments share same intercept
            freq = defaultdict(int)
            for b in intercept_list:
                freq[b] += 1

            # freq contains something like:
            #    b1: c1 segments
            #    b2: c2 segments
            #    b3: c3 segments
            #
            # trapezoid pairs = sum_{i<j} c_i * c_j

            total_sum = 0
            for count in freq.values():
                ans += total_sum * count   # pairs with previous groups
                total_sum += count

        # STEP 3: Subtract parallelograms
        #   (pairs of segments sharing midpoint but differing slopes)
        for slope_list in mid_to_slope.values():

            if len(slope_list) == 1:
                continue

            # count slopes for this midpoint
            freq = defaultdict(int)
            for slope in slope_list:
                freq[slope] += 1

            # parallelograms = sum_{i<j} d_i * d_j
            total_sum = 0
            for count in freq.values():
                ans -= total_sum * count
                total_sum += count

        return ans


sol = Solution()

print(sol.countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]]))