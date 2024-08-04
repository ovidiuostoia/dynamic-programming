def howSum(targetSum: int, numbers: list[int], memo = None):
    if memo is None:
        memo = {}
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    if targetSum in memo:
        return memo[targetSum]
    
    for number in numbers:
        reminder = targetSum - number
        res = howSum(reminder, numbers, memo)
        if res is not None:
            res.append(number)
            memo[targetSum] = res
            return res
    
    memo[targetSum] = None
    return None

def main():
    print(howSum(7, [5, 3, 4, 7])) # [4, 3]
    print(howSum(8, [2, 3, 5])) # [2, 2, 2, 2]
    print(howSum(7, [2, 4])) # None
    print(howSum(0, [5, 3])) # []
    print(howSum(300, [7, 14])) # None

if __name__ == "__main__":
    main()