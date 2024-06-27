#Aditi Mishra
#Difficulty: 532
tc = int(input())
for i in range(0,tc):
    wkhrs, fHrs = map(int, input().split())
    tWrk = wkhrs*4 + fHrs
    print(tWrk)