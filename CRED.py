# Difficulty: 539
# Aditi Mishra

x = int(input("CRED coins earned per bill: "))
y = int(input("Number of bills paid using CRED: "))

total_coins = x * y  
max_bags = total_coins // 100  

print("Maximum number of bags Chef can get:", max_bags)