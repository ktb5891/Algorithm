def solution(expression):
    answer = 0
    
    new_li = []
    def new_exp(expression):
        div = 0
        for i in range(len(expression)):
            if expression[i] in ['*','+','-']:
                new_li.append(expression[div:i])
                new_li.append(expression[i])
                div = i+1
            if i == len(expression)-1:
                new_li.append(expression[div:])
        return new_li
    n = 0
    operator = ['*','+','-']
    def cal(new_li,opera,n):
        if opera == '*':
            ans = int(new_li[n-1])*int(new_li[n+1])
            for i in range(3):
                new_li.pop(n-1)
            new_li.insert(n-1,ans)
            return new_li
        elif opera == '+':
            ans = int(new_li[n-1])+int(new_li[n+1])
            for i in range(3):
                new_li.pop(n-1)
            new_li.insert(n-1,ans)
            return new_li
        elif opera == '-':
            ans = int(new_li[n-1])-int(new_li[n+1])
            for i in range(3):
                new_li.pop(n-1)
            new_li.insert(n-1,ans)
            return new_li
    new_ans = []
    for k in range(2):
        for _ in range(3):
            new_exp(expression)
            while len(new_li) != 1:
                if new_li[n] == operator[0]:
                    cal(new_li,operator[0],n)
                    n = 0
                    continue
                elif new_li[n] == operator[1] and operator[0] not in new_li:
                    cal(new_li,operator[1],n)
                    n = 0
                    continue
                elif new_li[n] == operator[2] and operator[0] not in new_li and operator[1] not in new_li:
                    cal(new_li,operator[2],n)
                    n = 0
                    continue
                else:
                    n += 1
            new_ans.append(new_li.pop())
            operator.append(operator.pop(0))
        operator.insert(1,operator.pop(0))
    print(new_ans)
    answer = max(list(map(abs,new_ans)))
    return answer