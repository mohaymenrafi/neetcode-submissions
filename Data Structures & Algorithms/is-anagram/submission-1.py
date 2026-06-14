class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = []
        for str in s:
            store.append(str)
        for str in t:
            if str in store:
                store.remove(str)
            else:
                store.append(str)

        return len(store) == 0        