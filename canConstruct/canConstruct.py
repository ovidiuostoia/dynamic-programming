def canConstruct(target: str, wordBank: list[str], memo = None):
    if memo is None:
        memo = {}
    if target == "":
        return True
    if target in memo:
        return memo[target]

    for word in wordBank:
        if target.startswith(word):
            reminder = target[len(word):]
            if canConstruct(reminder, wordBank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False

def main():
    print(canConstruct("aaa", ["a", "b", "c"])) # true
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # true
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false

if __name__ == "__main__":
    main()