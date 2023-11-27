class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(curr,op,prev):
            #print(curr,op,prev)
            if op=="+":
                return curr+prev
            elif op=="*":
                return curr*prev
            elif op=="/":
                return int(curr/prev)
            else:
                return curr-prev
        stack = []
        i,l = 0,len(tokens)
        while i<l:
            curr = tokens[i]
            if curr in ['+','-','/','*']: 
                #print(stack)
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(operate(op1,curr,op2))
                #print(stack)
            else:
                stack.append(int(curr))
            i += 1
        #print(stack)
        # while len(stack)>1:   
        #     #print(stack)        
        #     curr = stack.pop()
        #     prev = stack.pop()
        #     op = stack.pop()
        #     res = operate(curr,op,prev)
        #     #print(stack,res)
        #     stack.append(res)
        return stack[0]