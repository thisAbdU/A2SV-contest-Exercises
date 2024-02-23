class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total_Y, current_Y, total_N, current_N = 0, 0, 0, 0
        penalty = []
        for customer in customers:
            if customer == 'Y':
                total_Y += 1
            else:
                total_N += 1
        
        #before current -> open and if No customer +1 penalty
        #after current -> closed and if Yes customer +1 penalty
        
        for i in range(len(customers)):
            if customers[i] == "Y":
                penalty.append(current_N + (total_Y - current_Y))
                current_Y += 1
            else:
                penalty.append(current_N + (total_Y - current_Y))
                current_N += 1
        penalty.append(current_N + (total_Y - current_Y))
        
        return penalty.index(min(penalty))
        
                
                
        
        
        