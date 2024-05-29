class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_num = 0
        current_str = ''

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + \
                    int(char)  # Build the full number
            elif char == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num = 0
                current_str = ''
            elif char == ']':
                repeat_count = num_stack.pop()
                last_str = str_stack.pop()
                current_str = last_str + current_str * repeat_count
            else:
                current_str += char

        return current_str
