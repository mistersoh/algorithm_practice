from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks_on_bridge = deque([0] * bridge_length)
    weights_on_bridge = 0
    waiting_trucks = deque(truck_weights)
    
    while waiting_trucks:
        time += 1
        weights_on_bridge -= trucks_on_bridge.popleft()
        
        if waiting_trucks and weights_on_bridge + waiting_trucks[0] <= weight:
            current_truck = waiting_trucks.popleft()
            trucks_on_bridge.append(current_truck)
            weights_on_bridge += current_truck
        else:
            trucks_on_bridge.append(0)
            
    return time + bridge_length