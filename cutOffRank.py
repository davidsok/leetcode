def countLevelUpPlayers(cutOffRank, num, scores):
    output = 0
    ranks = [1] * num
    scores = sorted(scores, reverse = True)
    for i in range(len(scores)):
        for j in range(i+1, len(scores)):
            if scores[j] < scores[i]:
                ranks[j] += 1
    for val in ranks:
        if val <= cutOffRank and cutOffRank <= num:
            output += 1
    print(scores)
    print('cutOffRank', cutOffRank)
    print('ranks', ranks)
    return output


scores= [100, 90, 80, 70, 60]
cutOffRank = 2
num = 5
# output = 2

scores= [50, 100, 80, 70, 100]
cutOffRank = 4
num = 5
#output = 4

scores= [2, 2, 3, 4, 5]
cutOffRank = 4
num = 5
#output = 5

scores= [2, 2, 2, 2, 2]
cutOffRank = 2
num = 5
# output = 5
print(countLevelUpPlayers(cutOffRank, num, scores))