class Solution:
    def twoSum(self, array, target):
        """find the list indices that sum to a target"""
        results = {}
        for index, val in enumerate(array):
            complement = target - val
            if complement in results:
                return [results[complement], index]
            else:
                results[val] = index
        return []

    def reverse(self, x) -> int:
        """reverse the (base 10) digits of an integer
        # a pairwise swap might take n//2 steps and works in place"""
        result = 0
        is_negative = (x != abs(x))
        if is_negative:
            x = abs(x)
        array = list(str(x))
        power = len(array)-1
        for index in range(0, power+1):
            result += (10**(index)*int(array[index]))
        if is_negative:
            result = - result
        return result

    def naive_reverse(self, x) -> int:
        array = []
        result = 0
        if x != int(x):
            return result
        is_negative = (x != abs(x))
        if is_negative:
            x = abs(x)
        while x != 0:
            array.append(x % 10)
            x = x // 10
        power = len(array)-1
        for index, digit in enumerate(array):
            result += (10**(power-index)*digit)
        if is_negative:
            result = - result
        return result
        
nums = [11, 2, 7, 15]
target = 9
result = Solution().twoSum(nums, target)
print(result)
print(Solution().reverse(321))
print(Solution().naive_reverse(321))
