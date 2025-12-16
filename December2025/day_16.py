from typing import List 

class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):

        # Build tree (0-indexed)
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            g[u - 1].append(v - 1)

        def dfs(u):
            # Normal and discounted price of u
            cost = present[u]
            dCost = present[u] // 2

            # dp0[b]: max profit if parent NOT bought, budget = b
            # dp1[b]: max profit if parent IS bought, budget = b
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)

            # Temporary arrays for merging children
            # subProfit0: u not bought → children no discount
            # subProfit1: u bought → children get discount
            subProfit0 = [0] * (budget + 1)
            subProfit1 = [0] * (budget + 1)

            # Maximum possible cost in this subtree
            uSize = cost

            # Process children
            for v in g[u]:
                child_dp0, child_dp1, vSize = dfs(v)
                uSize += vSize

                # Knapsack merge
                for i in range(budget, -1, -1):
                    for sub in range(min(vSize, i) + 1):
                        subProfit0[i] = max(
                            subProfit0[i],
                            subProfit0[i - sub] + child_dp0[sub]
                        )
                        subProfit1[i] = max(
                            subProfit1[i],
                            subProfit1[i - sub] + child_dp1[sub]
                        )

            # Decide whether to buy u
            for i in range(budget + 1):
                # Don't buy u
                dp0[i] = subProfit0[i]
                dp1[i] = subProfit0[i]

                # Buy u with full price
                if i >= cost:
                    dp0[i] = max(
                        dp0[i],
                        subProfit1[i - cost] + future[u] - cost
                    )

                # Buy u with discounted price
                if i >= dCost:
                    dp1[i] = max(
                        dp1[i],
                        subProfit1[i - dCost] + future[u] - dCost
                    )

            return dp0, dp1, uSize

        # CEO has no parent → parent not bought
        return dfs(0)[0][budget]
