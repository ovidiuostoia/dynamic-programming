import sys

def bestSum(targetSum: int, numbers: list[int], memo = None):
    if memo is None:
        memo = {}
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    if targetSum in memo:
        return memo[targetSum]
    
    minSize = sys.maxsize
    shortestRes = None
    for number in numbers:
        reminder = targetSum - number
        res = bestSum(reminder, numbers, memo)
        if res is not None and len(res) < minSize:
            minSize = len(res)
            shortestRes = [*res, number] # "*" is spread (or ... in js)
    
    memo[targetSum] = shortestRes
    return shortestRes

def main():
    print(bestSum(7, [5, 3, 4, 7])) # [7]
    print(bestSum(8, [2, 3, 5])) # [5, 3]
    print(bestSum(8, [1, 4, 5])) # [4, 4]
    print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]

if __name__ == "__main__":
    main()