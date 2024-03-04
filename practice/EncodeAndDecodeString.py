#Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

# Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own

# Example
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

class Solution:

    # """
    # @param: strs: a list of strings
    # @return: encodes a list of strings to a single string.
    # """
    def encode(self, st):
        res = ""
        for s in st : 
            res += (str(len(s)) + "#" + s )
        return res

    # """
    # @param: str: A string
    # @return: decodes a single string to a list of strings
    # """
    def decode(self, s):
        len1 = len(s)
        i =0
        res = []
        while i < len1:
            j=i
            while s[j] != "#":
                j += 1
            print("len :" + s[i:j])
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            print(word)
            res.append(word)
            i = j+1+length
        return res

def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test data
    strs = ["hello", "world", "python", "coding"]
    
    # Encode the list of strings
    encoded_str = solution.encode(strs)
    print("Encoded string:", encoded_str)
    
    # Decode the encoded string back to a list of strings
    decoded_list = solution.decode(encoded_str)
    print("Decoded list:", decoded_list)

if __name__ == "__main__":
    main()

