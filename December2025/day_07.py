class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """  
        ### What question is asking ?
          we have to find the number of odd numbers from low to high both are inclusive.
          
          We know that if there is sequential pair of number then are will be pair of even and odd, 
          like(even , odd) or (odd , even). Each pair always contains one odd.
          so we have to find the pair of numbers between low to high.
          
           => pair = (high - low) // 2
          
          But here we did not consider the low and high number itself. We also need to
          consider them.
          If they are both odd then there will be an extra pair of number which contains
          one more odd number so we have to add an extra 1.
          Now the question is if low and high both are odd then should be 2 odd number but why are adding 1 only?
          Let's answer this:
          Example-01: low = 3 , high = 9 both high and low is odd.
            pair = (9 - 3) // 2 = 3 as both odd so we have to add an extra 1 so
            Final answer = 3 + 1 = 4
            odds are -> 3,5,7,9
            explaination: (high - low) = 9 - 3 = 6 => 6 // 2 = 3, this 3 represent there are 3 pairs
            4,5,6,7,8,9 => (4,5) , (6,7) , (8,9) so 3 pair has 3 odd. but this did not include the low
            itself which is also an odd. so extra 1 came. 
          Example-02: low = 4 , high = 8
            pair = (8 - 4) // 2 = 2 as both are not odd so no extra 1 addition
            Final answer = 2
            odds are -> 5 , 7
          Example-03: low = 4 , high = 9
            pair = (8 - 4) // 2 = 2 as both are not odd so no extra 1 addition
            Final answer = 2
            odds are -> 5 , 7
          Final Formula is: 
           count of odd nums = ((high - low) // 2) + 1 if both low and high are odd
           otherwise (high - low) // 2
           
           More simplified version: count = (high + 1) // 2 - (low // 2) 
        """
        
        return (high + 1) // 2 - (low // 2)
    

n1 , n2 = 8 , 10    

count = ((n2 - n1) // 2) + (n1 % 2 == 1)

print(count)