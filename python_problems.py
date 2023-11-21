from typing import List


class DuplicateSolution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for x in nums:
            if x in seen:
                return True
            seen.add(x)

        return False

class AnagramSolution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = list(s)
        y = list(t)

        x.sort()       
        y.sort()

        return x==y


class TwoSumSolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j and x+y == target:
                    return [i,j]
        
        return None


class GroupAnagramsSoulution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(s)

            else:
                anagrams[sorted_word] = [s]

        result = list(anagrams.values())

        return result


class TopKSolutions(object):
    def topKFrequent(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []
        
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
        sorted_count = sorted(counts.items(), key = lambda x: x[1], reverse=True)

        result = [num for num, count in sorted_count[:k]]

        return result

class ProductExceptSelfSolution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        if not nums:
            return []

        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        right = 1

        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result

class IsValidSudokuSolution(object):
    def isValidSudoku(self, board: List[List[str]]):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (
                    board[i][j] in rows[i] or
                    board [i][j] in cols[j] or
                    board[i][j] in squares[(i // 3, j // 3)]
                ):
                    return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
        return True


class LongestConsecutiveSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)

        longest_streak = 0
        for n in nums:
            if n-1 not in numbers:
                length = 0
                while n + length in numbers:
                    length += 1
                longest_streak = max(longest_streak, length)
        
        return longest_streak

class IsPalindromeSolution:
    def isPalindrome(self, s: str) -> bool:
        result =''.join(sq.lower() for sq in s if sq.isalnum())
        return result == result[::-1]
