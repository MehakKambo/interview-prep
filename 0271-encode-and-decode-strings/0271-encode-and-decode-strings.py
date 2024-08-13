class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + '#' + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strings = []

        i = 0
        
        # "4#Hello4#World"
        #. 
        while i < len(s):
            j = i

            
            while s[j] != '#':
                j += 1
            
            word_length = int(s[i:j])

            word = s[j+1:j+1+word_length]
            decoded_strings.append(word)

            i = j + 1 + word_length
        return decoded_strings

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))