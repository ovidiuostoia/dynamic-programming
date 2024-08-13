def countConstruct(target: str, wordBank: list[str], memo = None) -> int:
    if memo is None:
        memo = {}
    if target == "":
        return 1
    if target in memo:
        return memo[target]
    
    res = 0
    for word in wordBank:
        if target.startswith(word):
            reminder = target[len(word):]
            res += countConstruct(reminder, wordBank, memo)

    memo[target] = res
    return res

def main():
    print(countConstruct("aaa", ["a", "b", "c"])) # 1
    print(countConstruct("aaa", ["a", "aa", "b", "c"])) # 3
    print(countConstruct("aaaz", ["a", "b", "c"])) # 0
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 0
    print(countConstruct("eeeeee", 
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 32

if __name__ == "__main__":
    main()