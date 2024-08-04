# Memoization Recipe

## 1. Make it work
* visualize the problem as a tree
* implement the tree using recursion
* test it

## 2. Make it efficient
* add a memo object
* add a base case to return memo values
* store return values into the memo object

Python does not support function overloading and using a default empty dict for the `memo` object is not feasible because the default assignment is made only the first time the function is called. See more info [here](https://discuss.python.org/t/why-does-the-variable-in-the-function-retain-its-value/23640).  Instead use this way:

```python
def canSum(targetsum: int, numbers: list[int], memo = None):
    if memo is None:
        memo = {}
    # rest of the code here
```