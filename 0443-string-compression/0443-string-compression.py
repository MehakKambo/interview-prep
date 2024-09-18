class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        input array can have lowercase and uppercase chars, symbols, 
        we need to treat them separately
        returning the length of the input array after we are done modifying it
        test cases:
        1. ["a"] -> 1
        2. ["A", "A", "A", "a", "a", "a"] -> ["A", "3", "a", "3"] -> 3
        3. ["A", "a", "a", "1", "1"] -> ["A", "a", "1", "0", "1", "2"] -> 5 
        4. ["a"]

        """

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
        print(output_string)
        
        for i in range(len(output_string)):
            chars[i] = output_string[i]
        
        chars = chars[:len(output_string)]




        return len(chars)


