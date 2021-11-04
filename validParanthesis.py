class Solution:
    def isValid(self,s):
        count=0
        open=['(','{','[']
        close=[')','}',']']
        s_list=[char for char in s]
        if len(s_list)%2!=0:
            return "false"
        else:
            for i in range(0,len(s_list)-1,2):
                if s_list[i] in open and s_list[i+1] in close:
                    if open.index(s_list[i])!=close.index(s_list[i+1]):
                        count+=1
                    else:
                        return "false"
                    if count==0:
                        return "true"
                    else:
                        return "false"

                        
