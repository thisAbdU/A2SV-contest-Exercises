class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill = {5: 0, 10: 0, 20: 0}
        for i in range(len(bills)):
            if bills[i] == 5:
                bill[5] += 1
            elif bills[i] == 10 and bill[5] > 0:
                bill[5] -= 1
                bill[10] += 1
            elif bills[i] == 20:
                print(bill)
                if bill[10] > 0 and bill[5] > 0:
                    bill[10] -= 1
                    bill[5] -= 1
                elif bill[5] > 2:
                    bill[5] -= 3
                    bill[20] += 1
                
                else:
                    return False
            else:
                return False
        return True
