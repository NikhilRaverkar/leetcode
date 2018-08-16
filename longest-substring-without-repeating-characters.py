class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet={}
        length=0
        i=0
        while(i<len(s)):
            if ord(s[i]) not in charSet:
                charSet[ord(s[i])]=i
                i+=1
            else:
                i=charSet.get(ord(s[i]))+1
                charSet.clear()
            length = len(charSet) if length < len(charSet) else length
        return length
        """
        :type s: str
        :rtype: int
        """


if __name__ =="__main__":
   print( Solution().lengthOfLongestSubstring("dvdf"))
