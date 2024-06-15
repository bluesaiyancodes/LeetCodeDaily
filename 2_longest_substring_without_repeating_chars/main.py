
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        highest = 0
        for i in range(0, len(s)):
            char = s[i]
            if char == " ":
                char = ".l."


            if char in arr:
                
                if len(arr)>highest:

                    highest = len(arr)
                    arr = []
                    arr.append(char)

            else:
                
                arr.append(char)
            
            if i==len(s)-1:
                if len(arr)>highest:
                    highest = len(arr)

        return highest

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the last positions of each character
        char_map = {}
        # Start of the current window
        start = 0
        # Length of the longest substring found
        max_length = 0

        for end in range(len(s)):
            # If the character is already in the dictionary and its index is within the current window
            if s[end] in char_map and char_map[s[end]] >= start:
                # Move the start to the right of the previous index of s[end]
                start = char_map[s[end]] + 1
            # Update the last index of the character to the current index
            char_map[s[end]] = end
            # Update the maximum length found
            max_length = max(max_length, end - start + 1)

        return max_length


if __name__ == '__main__':
    sol = Solution()
    A = "dvdf"
    res = sol.lengthOfLongestSubstring(A)
    print(res)