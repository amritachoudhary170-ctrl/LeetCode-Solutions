class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)
        suf = [-1] * (m + 1)

        suf[m] = n

        i = n - 1

        for j in range(m - 1, -1, -1):

            while i >= 0 and word1[i] != word2[j]:
                i -= 1

            if i < 0:
                break

            suf[j] = i
            i -= 1

        ans = []
        i = 0
        changed = False

        for j in range(m):

            while i < n:

                if word1[i] == word2[j]:
                    ans.append(i)
                    i += 1
                    break

                elif not changed:
                    if suf[j + 1] > i:
                        ans.append(i)
                        changed = True
                        i += 1
                        break

               
                i += 1

            else:
                return []

        return ans