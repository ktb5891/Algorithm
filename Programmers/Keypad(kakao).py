def solution(numbers, hand):
    answer = ''
    num_x_y = {0:(0,0),"*":(-1,0),"#":(1,0),
              7:(-1,1),8:(0,1),9:(1,1),
              4:(-1,2),5:(0,2),6:(1,2),
              1:(-1,3),2:(0,3),3:(1,3)}
    left = (-1,0)
    right = (1,0)
    if hand == 'right':
        hands = 'R'
    else:
        hands = 'L'
    while numbers:
        num = numbers.pop(0)
        if num in [1,4,7]:
            answer += 'L'
            left = num_x_y[num]
        elif num in [3,6,9]:
            answer += 'R'
            right = num_x_y[num]
        else:
            l_len = abs(num_x_y[num][0]-left[0])+abs(num_x_y[num][1]-left[1])
            r_len = abs(num_x_y[num][0]-right[0])+abs(num_x_y[num][1]-right[1])
            if l_len == r_len:
                answer += hands
                if hands == 'L':
                    left = num_x_y[num]
                else:
                    right = num_x_y[num]
            elif l_len < r_len:
                answer += 'L'
                left = num_x_y[num]
            else:
                answer += 'R'
                right = num_x_y[num]
    return answer