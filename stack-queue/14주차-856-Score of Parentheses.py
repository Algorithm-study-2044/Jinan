class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Initialize stack with a 0 to handle the score calculation

        for char in s:
            if char == '(':
                stack.append(0)  # Push a placeholder for a new level
            else:
                v = stack.pop()
                # Compute the score and add it to the previous level
                stack[-1] += max(2 * v, 1)

        return stack.pop()  # The final score
