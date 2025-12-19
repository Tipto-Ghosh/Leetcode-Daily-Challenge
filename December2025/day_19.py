from typing import List 
from collections import defaultdict
import heapq

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # for every person store the meeting time and label of the person met
        graph = defaultdict(list)
        for x , y , t in meetings:
            # x to y a bidirectional path with weight t
            graph[x].append((t , y))
            graph[y].append((t , x))
        
        # Priority Queue(minHeap) for BFS. It stores (time secret learned, person)
        # It pops the person with the minimum time of knowing the secret.
        minHeap = []
        heapq.heappush(minHeap , (0, 0))
        heapq.heappush(minHeap , (0, firstPerson))
        
        # Visited array to mark if a person is visited or not.
        # We will mark a person as visited after it is dequeued
        # from the queue.
        visited = [False] * n
        
        while minHeap:
            time , person = heapq.heappop(minHeap)
            # person is already visited then skip
            if visited[person]:
                continue
            
            visited[person] = True
            for t , next_person in graph[person]:
                if not visited[next_person] and t >= time:
                   heapq.heappush(minHeap , (t , next_person))
        
        # we need to return only these people who knew the secret means visited
        ans = [person for person in range(n) if visited[person]]
        return ans  
    
sol = Solution()
print(sol.findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1))