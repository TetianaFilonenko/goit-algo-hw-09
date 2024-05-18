def find_coins_greedy(coins, amount):
    result = {}
    coins.sort(reverse=True)

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(coins, amount):
    # Initialize the dp array
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    # Track the coins used
    coin_count = [{} for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                if coin in coin_count[i]:
                    coin_count[i][coin] += 1
                else:
                    coin_count[i][coin] = 1

    return coin_count[amount] if dp[amount] != float("inf") else {}


# Testing
coins = [50, 25, 10, 5, 2, 1]
amount = 113

# Жадібний алгоритм
print("Жадібний алгоритм:", find_coins_greedy(coins, amount))

# Динамічне програмування
print("Динамічне програмування:", find_min_coins(coins, amount))


# Testing 2
coins = [4, 3, 1]
amount = 6

# Жадібний алгоритм
print("Жадібний алгоритм:", find_coins_greedy(coins, amount))

# Динамічне програмування
print("Динамічне програмування:", find_min_coins(coins, amount))
