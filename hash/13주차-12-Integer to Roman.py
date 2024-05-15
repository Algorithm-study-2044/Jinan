class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping from integer values to Roman numeral symbols
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        # Resultant Roman numeral string
        roman_numeral = ""

        # Process each (value, symbol) pair
        for value, symbol in roman_map:
            # Append the symbol count times value can fit into num
            count = num // value
            roman_numeral += symbol * count
            num %= value

        return roman_numeral
