class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # code here
        ans = ""
        d.sort(key=lambda x: (-len(x), x))

        for word in d:
            if len(word) <= len(ans):
                break

            i = 0
            len_w = len(word)
            for char in s:
                if char == word[i]:
                    i += 1
                    if i == len_w:
                        ans = word
                        break

        return ans