class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping from digit to corresponding characters
        digit_to_char = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        # Result list to store the combinations
        result = []

        # Helper function for recursive backtracking
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return

            # Get the letters that the current digit can represent
            letters = digit_to_char[digits[index]]

            # Go through all the letters, appending them to the current combination and recurse
            for letter in letters:
                backtrack(index + 1, current_combination + letter)

        # Start the backtracking with the first digit
        backtrack(0, "")

        return result
