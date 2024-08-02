def gridTraveler(m: int, n: int, memo: dict = {}):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    
    key = (min(m, n), max(m, n))
    if key in memo:
        return memo[key]
    
    down = gridTraveler(m - 1, n, memo)
    right = gridTraveler(m, n - 1, memo)
    memo[key] = down + right

    return memo[key]

def main():
    print(gridTraveler(1, 1)) # 1
    print(gridTraveler(2, 3)) # 3
    print(gridTraveler(3, 2)) # 3
    print(gridTraveler(3, 3)) # 6
    print(gridTraveler(18, 18)) # 2333606220

if __name__ == "__main__":
    main()