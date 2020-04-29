# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?


# Solution
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return True if self.resulted_str(S) == self.resulted_str(T) else False

    def resulted_str(self, s):
        pointer = len(s)-1
        count_hash = 0
        c = ''
        while pointer >= 0:
            if s[pointer] == '#':
                count_hash += 1
            elif s[pointer] != '#' and count_hash == 0:
                c += s[pointer]
            else:
                count_hash -= 1
            pointer -= 1
        return c
