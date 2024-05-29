class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a position map from the order string
        position_map = {char: index for index, char in enumerate(order)}

        # Sort the characters in s based on their position in the order string
        sorted_s = sorted(
            s, key=lambda char: position_map.get(char, len(order)))

        # Join the sorted characters to form the result string
        return ''.join(sorted_s)
