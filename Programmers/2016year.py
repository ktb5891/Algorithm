def solution(a, b):
    day_list = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    mon_day_dic = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    day_count = 0
    if a != 1:
        for i in range(1,a):
            day_count += mon_day_dic[i]
        day_count += b
        day_count %= 7
        answer = day_list[day_count]
    else:
        day_count += b
        day_count %= 7
        answer = day_list[day_count]
    return answer