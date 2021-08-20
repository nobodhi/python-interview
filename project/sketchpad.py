import time
start = time.time()

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        max_len = 1
        print(s, len(s))
        for idx_s in range(0, len(s)):
            print("idx_s", s[idx_s])
            uniques = set(s[idx_s])
            if max_len > len(s) - idx_s:
                print("bailing, max_len has been found", idx_s, max_len)
                return max_len
            for idx_cmp in range(idx_s+1, len(s)):
                print("idx_cmp", s[idx_cmp], idx_cmp - idx_s + 1)
                if s[idx_cmp] in uniques:
                    print("duplicate found, resetting")
                    break
                uniques.add(s[idx_cmp])
            if len(uniques) > max_len:
                print("voila, a new max has been found at ", idx_s , "with length", len(uniques))
                max_len = len(uniques)
        return max_len


start = time.time()
# print('lengthOfLongestSubstring', Solution().lengthOfLongestSubstring(''))
# print('lengthOfLongestSubstring', Solution().lengthOfLongestSubstring('aa'))
# print('lengthOfLongestSubstring', Solution().lengthOfLongestSubstring('ab'))
# print('lengthOfLongestSubstring', Solution().lengthOfLongestSubstring('bwf'))
# print('lengthOfLongestSubstring', Solution().lengthOfLongestSubstring('abcadef'))
print('lengthOfLongestSubstring', Solution().lengthOfLongestSubstring('abcaaaaaaaaa'))


print(round(time.time() - start, 2), "seconds elapsed")
