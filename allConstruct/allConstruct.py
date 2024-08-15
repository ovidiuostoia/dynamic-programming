def allConstruct(target: str, wordBank: list[str], memo = None):
    if memo is None:
        memo = {}
    if target == "":
        return [[]]
    if target in memo:
        return memo[target]
    
    res = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank, memo)
            targetWays = [el[:] for el in suffixWays] # copy every sublist
            [el.insert(0, word) for el in targetWays]
            res.extend(targetWays)

    memo[target] = res
    return res

def main():
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    print(allConstruct("", ["purp", "p", "ur", " le", "purpl"])) # [[]]
    print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))  # [['ef', 'cd', 'ab'], ['def', 'c', 'ab'], ['def', 'abc'], ['ef', 'abcd']]

if __name__ == "__main__":
    main()