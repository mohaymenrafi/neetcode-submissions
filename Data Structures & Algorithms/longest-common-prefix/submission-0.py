class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for idx in range(len(strs[0])):
            curr_word = strs[0][idx]
            for word in strs:
                if idx >= len(word) or curr_word != word[idx]:
                    return "".join(result)
            result.append(curr_word)
        return "".join(result)