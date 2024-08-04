def canSum(targetSum: int, numbers: list[int], memo = None):
    if memo is None: # reason for this here: https://discuss.python.org/t/why-does-the-variable-in-the-function-retain-its-value/23640
        memo = {}
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    if targetSum in memo:
        return memo[targetSum]
    
    for number in numbers:
        reminder = targetSum - number
        if canSum(reminder, numbers, memo):
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False

def main():
    print(canSum(7, [2, 3])) # true
    print(canSum(7, [5, 3, 4, 7])) # true
    print(canSum(7, [2, 4])) # false
    print(canSum(8, [2, 3, 5])) # true
    print(canSum(300, [7, 14])) # false

if __name__ == "__main__":
    main()