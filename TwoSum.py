class Solution:
    def twoSum(self,list1,target):
        for i in range(0,len(list1)):
	        for j in range(0,len(list1)):
		        if list1[i]+list1[j]==target and i!=j:
			        return [i,j]
                    
                    

