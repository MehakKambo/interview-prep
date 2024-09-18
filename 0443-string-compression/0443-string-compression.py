class Solution:
    def compress(self, chars: List[str]) -> int:
        # output_string = ""
        # prev_char = ''
        # counter = 0
        # for char in chars:
        #     if (prev_char != char):
        #         output_string += prev_char + (str(counter) if counter > 1 else "")
        #         counter = 1
        #     else:
        #         counter += 1
        #     prev_char = char
        # output_string += prev_char + (str(counter) if counter > 1 else "")
        # for i in range(len(output_string)):
        #     chars[i] = output_string[i]
        
        # chars = chars[:len(output_string)]
        # return len(chars)
        
        write = 0  # Pointer to write the compressed result
        i = 0  # Pointer to read through chars

        while i < len(chars):
            char = chars[i]
            count = 0

            # Count occurrences of the current character
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            
            # Write the character to the chars array
            chars[write] = char
            write += 1

            # If the count is greater than 1, write the count digits
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # Return the length of the compressed list
        return write



