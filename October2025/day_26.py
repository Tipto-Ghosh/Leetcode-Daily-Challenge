from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance 

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        
        # if invalid account or money
        if account1 < 0 or account1 >= self.n or account2 < 0 or account2 >= self.n:
            return False
        
        # valided money
        if money > self.balance[account1]:
            return False
        
        self.balance[account1] -= money
        self.balance[account2] += money  
        
        return True
    
    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if account < 0 or account >= self.n:
            return False
        
        self.balance[account] += money
        return True 

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        
        if account < 0 or account >= self.n:
            return False
        
        if money > self.balance[account]:
            return False
        
        self.balance[account] -= money
        
        return True 
