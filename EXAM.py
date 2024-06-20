# Aditi Mishra
# Difficulty: 519
schls, stus, pStus = map(int, input().split())
tStus = schls * stus
pPcent = pStus / stus * 100

if pPcent > 50:
    print("YES")
else:
    print("NO")

