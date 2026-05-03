# Problem: Reverse Polish Notation
# Platform: LeetCode
# Difficulty: Medium
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        stack = []
        if (len(tokens)==1):
            result = int(tokens[-1])
        else:
            for i in tokens:
                if i not in operators:
                    stack.append(i)
                if i in operators:
                    a = int(stack[-1])
                    stack.pop()
                    b = int(stack[-1])
                    stack.pop()
                    if (i == "+"):
                        stack.append(b+a)
                    if (i == "-"):
                        stack.append(b-a)
                    if (i == "*"):
                        stack.append(b*a)
                    if (i == "/"):
                        stack.append(int(b/a))

            result = stack[-1]
        return result
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
print(sol.evalRPN(tokens))