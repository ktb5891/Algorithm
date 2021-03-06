def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    # length, weight, truck_weight
    while len(bridge) != 0:
        answer += 1
        # 1초 지남
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer