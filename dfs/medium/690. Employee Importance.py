from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {}
        for employee in employees:
            emp_map[employee.id] = employee

        def dfs(emp_id) -> int:
            curr = emp_map[emp_id]
            importance = curr.importance
            for sub in curr.subordinates:
                importance += dfs(sub)
            return importance

        return dfs(id)
