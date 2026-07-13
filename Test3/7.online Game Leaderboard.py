scores = list(map(int, input("enter player scores: ").split()))

scores.sort(reverse=True)

print("leaderboard:")
print(scores)