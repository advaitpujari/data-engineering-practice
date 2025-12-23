def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ''

        for i in range(n):
            for j in range(i,n):
                sub = s[i:j+1]
                if sub == sub[::-1] and len(sub) > len(result):
                    result = sub
        return result