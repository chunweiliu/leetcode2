"""Interview
* Ask question before coding

* Write clean code
- for reading
- for extension

* Not introduce bugs

* Submit within 3 times

# Leetcode

* 150 - 200 is good enough

* Classify the problems
- Binary Search
- Binary Tree & Divide Conquer
- Dynamic Programming I
- Dynamic Programming II
- Linked List
- Array & Numbers
- Data Structure
- Graph & Search

* Write TEMPLATE

* BFS is preferable

None -> reference = 0

Java:
[address pointer] -> [length|pointer] -> [array ...]
None                  length = 0
"""

def subsets(nums, lists=[]):
    """
    DFS: find all solutions
    """
    results = []

    if not nums:
        return results

    nums.sort()

    subset = []
    subset_helper(nums, subset, results)
    return results

def subset_helper(nums, subset, results):
    # In Java we use deep copy to clone a new subset. 
    # In Python we don't need that since the subset is a new address.
    results.append(subset)

    for i, num in enumerate(nums):
        subset.append(num)
        subset_helper(nums[i + 1:], subset, results)
        subset.pop()

print subsets([1, 2])
