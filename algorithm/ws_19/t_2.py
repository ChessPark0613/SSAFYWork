maxv = 1730
coins = [500, 100, 50, 10]
ans = 0

for coin in coins:
    ans += maxv // coin
    maxv %= coin

print(ans)

