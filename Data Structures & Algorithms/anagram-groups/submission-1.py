class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Logic:
        # 1. Create a dictionary 
        # 2. Iterate through entire list of strs
        # 3. Iterate through each character in each str
        # 4. Create an empty array of size 26 and fill it with 0s
        # 5. Store frequency of each letter in this array (position determines letter: a=0, b=1)
        # 6. Store that frequency as a KEY in the dictionary.
        # 7. Append any values that correspond to that key to the dictionary
        # 8. Return the values.

        res = defaultdict(list)

        for s in strs:
            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord("a")] += 1

            res[tuple(counts)].append(s)

        
        return list(res.values())


