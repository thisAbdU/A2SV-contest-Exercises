class Solution:
    def average(self, salary: List[int]) -> float:
        sumSalary = 0
        for i in range(len(salary)):
            sumSalary += salary[i]
            
        return (sumSalary - (min(salary) + max(salary)))/(len(salary) - 2)
        