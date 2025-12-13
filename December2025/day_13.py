from typing import List 

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # Function for alphanumeric check
        def isValidCode(c: str) -> bool:
            if len(c) == 0:
                return False 
            
            for i in range(len(c)):
                if not (c[i].isalnum() or c[i] == '_'):
                    return False 
            
            return True 
        
        # 3 types of business 
        validBusiness = {
            "electronics" : 0,
            "grocery" : 1,
            "pharmacy" : 2,
            "restaurant": 3
        }   
        businessTypesCodes = [[] for _ in range(4)]
        n = len(code)
        
        for i in range(n):
            # check coupon is active or not. 
            # if not active then go to next one
            if not isActive[i]:
                continue
            
            # check the code is valid
            if isValidCode(code[i]) and businessLine[i] in validBusiness:
                businessTypesCodes[validBusiness[businessLine[i]]].append(code[i])
        
        # sort codes of each business and make the ans list
        ans = [] 
        for i in range(len(businessTypesCodes)):
            businessTypesCodes[i].sort()
            for c in businessTypesCodes[i]:
               ans.append(c)
        
        return ans 
                

sol = Solution()
print(sol.validateCoupons(code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [True,True,True,True]))
print(sol.validateCoupons(code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [False,True,True]))