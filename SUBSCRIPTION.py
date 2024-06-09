#Aditi Mishra
#Difficulty: 504

ppl, cost = map(int, input().split())
share = int(ppl / 6)
if share == 0:
    print(cost)
else:
    if (ppl%6 != 0):
        share = share + 1
        tCost = share*cost
        print(tCost)
