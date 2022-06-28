dice = [int(x) for x in input().split()]
dice = sorted(dice)
answer = 0
set_dice = set(dice)

if len(set_dice) == 1:
    answer = 10000 + dice[0]*1000
elif len(set_dice) == 2:
    if dice[0] == dice[1]:
        answer = 1000 + dice[0]*100
    else:
        answer = 1000 + dice[1]*100
else:
    answer = max(dice)*100

print(answer)