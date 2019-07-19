###### EASY ######

### 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = 0
        for i in nums:
            k += 1
            if target - i in nums[k:]:
                return(k - 1, nums[k:].index(target - i) + k)
# The use of [k:], w.index, and how to def/class in python

### 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        num = 0
        x = abs(x)
        while x > 0:
            d = x % 10 
            x = x // 10
            num = num * 10 + d
        if (num < (-2 ** 31) or num > (2 ** 31) - 1):
            return 0
        return num * sign
# The use of %, // and if/while

### 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        if n < 0:
            return False
        if (n < (-2 ** 31) or n > (2 ** 31) - 1):
            return 0
        num1 = 0
        num2 = 0
        while n > 0:
            d = n % 10
            n = n // 10
            num1 = num1 * 10 + d
            num2 = num1
        if num2 == x:
            return True
        else:
            return False
# w.r.t Q2

### 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[-1::-1]:
            symbol = 1
            if (i in ['I', 'X', "C"] and result >= 5 * dic[i]):
                symbol = -1
            result += dic[i] * symbol
        return result

### 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in zip(*strs):
            bags = set(i)
            if len(bags) == 1:
                prefix += bags.pop()
            else:
                break
        return prefix
# The use of zip(join 2 tuples together), set,
# * before var(could be multiple input), pop(jump out)

### 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack, match = [], {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in match:
                if not (stack and stack.pop() == match[ch]):
                    return False
            else:
                stack.append(ch)
        return not stack
# The use of pop and list/bool

### 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
# Iterations

### 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            i, j = 1, 1
            while j < len(nums):
                if nums[i-1] != nums[j]:
                    nums[i] = nums[j]
                    i += 1
                j += 1
            return i
# Iterations

### 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start

### 28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1

### 35. Search Insert Position

## 35.1 Duplicate

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def searchInsert(self, nums, target):
            l , r = 0, len(nums)-1
            while l <= r:
                mid=(l+r)/2
                if nums[mid]== target:
                    return mid
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return l

## 35.2 w/o Duplicate

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def searchInsert(self, nums, target):
            l , r = 0, len(nums)-1
            while l <= r:
                mid=(l+r)/2
                if nums[mid] < target:
                    l = mid+1
                else:
                    if nums[mid]== target and nums[mid-1]!=target:
                        return mid
                    else:
                        r = mid-1
            return l

### 38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s

### 53. Maximum Subarray

