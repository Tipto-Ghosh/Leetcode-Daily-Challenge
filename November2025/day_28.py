from typing import List 
from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """ 
        # Observations:
          1. It's a tree so no cycle and also it's not a binary tree.
          2. Sum of all node values are divisible by k
        
        # Thought:
          we can think like this: Take a sub-tree and check is sum of all the nodes of the subtree
          is divisible by k? If yes then we got a component now check rest of the tree.
          
          But how to pick a sub-tree? Well we can take like this:
          go deeper of the tree and when the node is a leaf node,
          ask the child are you divisible by k? if yes-> then it's a sub-tree.
          If child is not a sub-tree then pass the value to it's parent.
          Now check for the parent and do so on.
        
        # Algorithm:
          1. make a adjaceny list as all the graph algorithm
          2. as no cycle so no need of visited list
          3. make a helper function now:
             Helper Function (curr_node , parent_node):
               1. Find the total sum of all the child including curr_node value
               2. If total sum is divisible by k then increament the count of components 
               3. otherwise pass the total sum to upper level means curr_nodes parent
        
        # Time Complexity: O(n) cause we are visiting all the n nodes once
        # Space Complexity: O(n) cause storing all the n-1 edges and each edge length 2 so O([n-1] * 2) => O(n)
        """
        
        # make the adjacency list
        adj_list = defaultdict(list)
        for a , b in edges:
            # as it's a undirected graph so a <-> b
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        total_components = 0 # total possible valid split count
        
        # helper function
        def dfs(curr_node: int , parent_node: int) -> int:
            # if curr_node is a leaf  => then just it's value will be the sum
            total_sum = values[curr_node]
            
            # if leaf then no child no more values will be added
            # but if not a leaf node then go to all it's child nodes
            for child in adj_list[curr_node]:
                # if child node is parent of curr_node then skip it to avoid revisiting
                if child == parent_node:
                    continue
                
                # otherwise visit the child and get the total
                total_sum += dfs(curr_node = child , parent_node = curr_node)
            
            # now check is it a valid split?
            if total_sum % k == 0:
                # it's a valid split so increament the count
                nonlocal total_components
                total_components += 1
                return 0 # as valid split so no total left so pass to upper level
            else: # otherwise pass the total sum to the parent node
                return total_sum
        
        # starts with 0-th node and it has no parent so -1
        dfs(0 , -1)
        return total_components
    
sol = Solution()
print(sol.maxKDivisibleComponents(n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6))
print(sol.maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3))