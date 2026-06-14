class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # store = []
        # for str in s:
        #     store.append(str)
        # for str in t:
        #     if str in store:
        #         store.remove(str)
        #     else:
        #         store.append(str)

        # return len(store) == 0        