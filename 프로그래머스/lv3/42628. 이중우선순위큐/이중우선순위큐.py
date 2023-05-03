import heapq

def solution(operations):
    que = []
    
    for ops in operations:
        op, num = ops.split()
        if op == "I":
            heapq.heappush(que,int(num))
        
        elif op == "D" and num == "1" and len(que) != 0:
            max_val = max(que)
            que.remove(max_val)
            
        elif op == "D" and num == "-1" and len(que) != 0:
            heapq.heappop(que)
            
    if len(que) == 0:
        return [0,0]
    else:
        return [max(que),heapq.heappop(que)]