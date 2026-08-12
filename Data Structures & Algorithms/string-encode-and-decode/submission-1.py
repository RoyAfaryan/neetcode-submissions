class Solution:

    def encode(self, strs: List[str]) -> str:

        # Logic:
        # 1. Iterate through the loop
        # 2. Add the length of the string, a "#", then the actual string to the big string
        
        encoded_strs = ""

        for s in strs:
            encoded_strs += "1#"+s

        return encoded_strs


    def decode(self, s: str) -> List[str]:

        # Logic:
        # 1. Take in string
        # 2. Use the .split() functino to turn back into list

        return s.split('1#')[1:]