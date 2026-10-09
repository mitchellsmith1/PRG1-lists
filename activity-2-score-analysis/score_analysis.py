PASS_MARK = 40

scores = [72, 38, 55, 91, 40, 27, 66, 83, 45, 39]

passed = []
failed = []
distinction = []

for score in scores:
    if score >= PASS_MARK:
        passed.append(score)
    else:
        failed.append(score)

print(f"{len(scores)} learners sat the paper")
print(f"{len(passed)} passed, {len(failed)} did not")

average_pass = sum(passed) / len(passed)
print(f"Average: {average_pass:.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")

pass_rate = len(passed) / len(scores) * 100
print(f"Pass rate: {pass_rate:.0f}%")

print(f"Needs support: {sorted(failed)}")

for score in scores:
    if score >= 70:
        distinction.append(score)

print(f"{len(distinction)} learners got a distinction.")