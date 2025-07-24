product_price = int(input())

changes = [500, 100, 50, 10, 5, 1]
change = 1000 - product_price
count = 0

for coin in changes:
    count += change // coin
    change %= coin

print(count)