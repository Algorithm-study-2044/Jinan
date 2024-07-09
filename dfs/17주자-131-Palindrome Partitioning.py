class Solution:
    def partition(self, s: str):
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, path: list):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(start + end - start, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result