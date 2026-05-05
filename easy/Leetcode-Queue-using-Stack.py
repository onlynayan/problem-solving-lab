# Problem: Implement Queue using Stacks
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, x:int) -> None:
        self.in_stack.append(x)
    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    commands = ["push", "push", "peek", "pop", "empty"]
    args = [[1], [2], [], [], []]
    results = [None]

    for cmd, arg in zip(commands, args):
        if cmd == "push":
            q.push(arg[0])
            results.append(None)
        elif cmd == "pop":
            results.append(q.pop())
        elif cmd == "peek":
            results.append(q.peek())
        elif cmd == "empty":
            results.append(q.empty())

    print(results)