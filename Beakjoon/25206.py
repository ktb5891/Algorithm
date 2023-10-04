grade_point = {'A+': 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}
final_grade = []
sum_ratio = 0
for _ in range(20):
    sub, ratio, grade = input().split()
    try:
        final_grade.append(float(ratio)*grade_point[grade])
        sum_ratio += float(ratio)
    except:
        pass

print(sum(final_grade)/sum_ratio)

