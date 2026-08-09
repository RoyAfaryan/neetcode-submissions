class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Logic:
        # 1. Create a hashmap
        # 2. Iterate through the list of strings
        # 3. Create an empty array size of 26 (a-z)
        # 4. Iterate through characters in string
        # 5. Store count of each character in the array
        # 6. This array becomes the key, and the value is the list of strings that are anagrams to that key
        # 7. Return the values of the hashmap
        
        res = defaultdict(list)
    
        for s in strs:
            count = [0] * 26 # a-z
            for c in s:
                count[ord(c) - ord("a")] += 1 # store each count (corresponds to order using ascii)

            res[tuple(count)].append(s)

        return list(res.values())




