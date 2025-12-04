class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        ### What the problem actually wants?

        We have n cars on a straight infinite road.
        Each car:
            - moves Left   ('L')
            - moves Right  ('R')
            - stays still  ('S')
        All moving cars have the SAME speed.

        A collision happens when:
            1) 'R' meets 'L'  -> 2 collisions (because both were moving)
            2) moving car ('L' or 'R') hits 'S' -> 1 collision
        After a collision:
            -> cars become 'S' (stop permanently)
            -> no further movement for those cars

        Our task: count total collisions.

        ### Key Observations
        A car moving LEFT ('L') will only collide 
        if something moving RIGHT ('R') is before it.

        Example:   R R L These 2R hit the L -> collisions happen

        A stationary car ('S') will stop any RIGHT-moving group before it.
        Example:  R R S => both R hit S -> 2 collisions

        A RIGHT-moving streak ('R R R ...') is what can collide later.
        Let's call:
            flag = number of active right-moving cars ('R') seen so far that have not collided yet
        Behavior:
            - When we see an 'R': increment flag
            - When we see an 'L':
                    all active R's collide with this L
            - When we see an 'S':
                all active Rs collide with this S
            After collision: flag becomes 0 cause they stop moving
        
        ans = total collisions  
        flag = number of pending 'R' cars that are still moving

            flag = -1  means no active moving streak exists yet
            flag = 0   everything so far is stationary / stopped
            flag > 0   have a streak of 'R's waiting to collide

        ### Steps of the Algorithm

        Loop through every character c in directions:

           Case 1: c == 'L'
                If there are active R-cars (flag >= 0):
                    They collide with this L:
                        collisions = flag (each R hits L -> 2 collisions?)
                    But careful:
                            Problem says: R-L collision = 2 collisions
                                ans += flag + 1
                            Why increment 1 instead of 2?
                                - flag collisions from R hitting L
                                - +1 for L stopping itself
                    After collision -> flag = 0 (all stopped)

                If no active R cars (flag < 0):
                    'L' just moves left and never hits anything -> ignore
                    
            Case 2: c == 'S'
                If active R's exist:
                    all R's crash into S  -> + flag collisions
                Set flag = 0 (all become stop again)

            Case 3: c == 'R'
                If flag >= 0:
                    We are building / extending an R-streak
                    flag += 1
                Else:
                    First R encountered -> start streak
                    flag = 1

        ### Time Complexity:  O(n)
        ### Space Complexity: O(1)
        """
        ans = 0
        flag = -1

        for c in directions:
            # Case: 'L' moves left
            if c == "L":
                if flag >= 0: # check right moving cars
                    ans += flag + 1 # all Rs + this L collide
                    flag = 0 # all now become stationary
            # Case: 'S' stationary
            elif c == "S":
                if flag > 0: # pending Rs hit this S
                    ans += flag
                flag = 0 # all become stationary
            # Case: 'R' moves right
            else:
                if flag >= 0: # existing streak
                    flag += 1
                else: # first R seen
                    flag = 1

        return ans 

sol = Solution()
print(sol.countCollisions("RLRSLL"))