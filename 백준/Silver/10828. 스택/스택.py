import sys

def process_command(stack, command):
    
    order = command[0]
    
    if order == "push":
        stack.append(int(command[1]))
        return None
    elif order == "pop":
        return stack.pop() if stack else -1
    elif order == "size":
        return len(stack)
    elif order == "empty":
        return 0 if stack else 1
    elif order == "top":
        return stack[-1] if stack else -1

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    
    result = process_command(stack, command)
    
    if result is not None:
        print(result)