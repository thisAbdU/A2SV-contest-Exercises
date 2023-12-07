class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        no_of_days = n % 7
        total_amount = 0
        
        for i in range(full_weeks):
            total_amount += sum(range(i + 1, i + 8)) 
            
        total_amount += sum(range(full_weeks + 1, full_weeks + no_of_days + 1))  
        
        return total_amount
