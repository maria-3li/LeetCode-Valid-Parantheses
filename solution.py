class Solution:
    def isValid(self, s: str) -> bool:
        mystack=[]
            
        for str in s:
            if (str == "(" or str == "[" or str == "{"):https://github.com/maria-3li/LeetCode-Valid-Parantheses
                mystack.append(str)
            elif (str == ")" and len(mystack)!=0 and mystack[-1]== "("):
                mystack.pop()
            elif (str == "]" and len(mystack)!=0 and mystack[-1]== "["):
                mystack.pop()
            elif (str == "}" and len(mystack)!=0 and mystack[-1]== "{"):
                mystack.pop()
            else:
                return False;
            
        if (len(mystack) != 0 ): 
            return False
        else:
            return True
                

