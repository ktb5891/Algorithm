from itertools import combinations as cbn

def solution(number, k):
    answer = ''
    # num_list = list(number)
    # combi = list(cbn(num_list,len(number)-k))
    # answer = ''.join(max(combi))
    
    stack = [number[0]]
    
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
        
    if k != 0:
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer