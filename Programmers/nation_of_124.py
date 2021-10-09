def solution(n):
    answer = ''
    num_dic = {1:'1',2:'2',0:'4'}
    
    div = 1
    remain = 1
    
    while div != 0:
        div = n//3
        remain = n%3
        
        if remain == 0:
            div -= 1
            
        n = div
        
        answer = num_dic[remain] + answer
    
    return answer