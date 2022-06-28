n = int(input())
score = [int(x) for x in input().split(' ')]
max_score = max(score)
new_score = [m/max_score*100 for m in score]
print(sum(new_score)/n)