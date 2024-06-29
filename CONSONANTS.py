# Aditi Mishra
#Difficulty: 1000
tc = int(input())
for i in range(0,tc):
    n = int(input())
    s = input()
    sl = list(s.lower())
    count = 0
    for j in range(0, n):
        count = count + 1
        if sl[j] in "aeiou":
            count = 0
        if count >= 4:
            print("NO")
            break
    if count < 4:
        print("YES")
            