arr = [list(input().split()) for _ in range(20)]

cnt = 0
total = 0


def to_score(grade):
    if grade == "A+":
        return 4.5
    elif grade == "A0":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B0":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C0":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D0":
        return 1.0
    elif grade == "F":
        return 0


for _, credit, grade in arr:
    if grade == "P":
        continue
    total += float(credit) * to_score(grade)
    cnt += float(credit)

print(f"{total / cnt:.6f}")