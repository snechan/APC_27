# 28. Store scores of a batsman in 10 matches and calculate highest, lowest, total, average, centuries and half-centuries.

scores = [45, 100, 75, 120, 30, 55, 90, 110, 40, 60]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total:", sum(scores))
print("Average:", sum(scores) / 10)
print("Centuries:", sum(x >= 100 for x in scores))
print("Half-centuries:", sum(50 <= x < 100 for x in scores))