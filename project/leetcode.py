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
        # a pairwise swap might take n//2 steps and works in place
        # NOTE: blah blah 32 bit if > 2**31 return 0"""
        result = 0
        is_negative = (x != abs(x))
        if is_negative:
            x = abs(x)
            max_value = 2**31
        else:
            max_value = 2**31-1
        array = list(str(x))
        power = len(array)-1
        for index in range(0, power+1):
            result += (10**(index)*int(array[index]))
            if result > max_value:
                return 0
        if is_negative:
            result = - result
        return result

    def simple_reverse(self, x) -> int:
        """TODO try using extended slice to reverse the string, 
        i.e. foo = x[::-1]. Note that we're using str(x) anyway"""
        result = 0
        is_negative = (x != abs(x))
        if is_negative:
            x = abs(x)
            max_value = 2**31
        else:
            max_value = 2**31-1
        power = len(str(x))-1
        while x > 0:
            result += x % 10 * 10**power
            if result > max_value:
                return 0
            x = x // 10
            power-=1
        if is_negative:
            result = - result
        return result

nums = [11, 2, 7, 15]
target = 9
result = Solution().twoSum(nums, target)
print(result)

print(Solution().simple_reverse(321))
print(Solution().simple_reverse(-321))
# -1534236469
# -2147483412
assert Solution().reverse(-1534236469) == 0
assert Solution().reverse(-2147483412) == -2143847412
