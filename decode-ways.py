class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        word_count = [0] * (len(s) + 1)
        word_count[0] = 1

        if s[0] != '0':
            word_count[1] = 1

        for i in range(2, len(s) + 1):
            if (s[i - 1] != '0'):
                word_count[i] += word_count[i - 1]

            if (int(s[i - 2] + s[i - 1]) in range(10, 27)):
                word_count[i] += word_count[i - 2]
        return word_count[len(s)]

if __name__ =="__main__":
   print( Solution().numDecodings("00"))