class Solution:
    def compress(self, chars: List[str]) -> int:
        output_string = ""
        prev_char = ''
        counter = 0
        for char in chars:
            if (prev_char != char):
                output_string += prev_char + (str(counter) if counter > 1 else "")
                counter = 1
            else:
                counter += 1
            prev_char = char
        output_string += prev_char + (str(counter) if counter > 1 else "")
        for i in range(len(output_string)):
            chars[i] = output_string[i]
        
        # chars = chars[:len(output_string)]
        while len(chars) > len(output_string):
            chars.pop()
        return len(chars)


