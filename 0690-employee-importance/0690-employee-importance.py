"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        hashmap=dict()
        for employee in employees:
            hashmap[employee.id]=employee
            
        def dfs(id):
            temp = hashmap[id].importance
            for subordinate in hashmap[id].subordinates:
                temp+=dfs(subordinate)            
            return temp

        return dfs(id)

