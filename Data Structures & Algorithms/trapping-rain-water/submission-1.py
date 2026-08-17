class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = []
        suffix = []
        size = len(height)
        total = 0

        # fill prefix
        for i in range(size):
            if not prefix:
                prefix.append(height[i])
            elif prefix[-1] > height[i]:
                prefix.append(prefix[-1])
            else:
                prefix.append(height[i])

        # fill suffix
        for i in range(size - 1, -1, -1):
            if not suffix:
                suffix.append(height[i])
            elif suffix[-1] > height[i]:
                suffix.append(suffix[-1])
            else:
                suffix.append(height[i])
        suffix.sort(reverse=True)
    
        for i in range(size):
            total += min(prefix[i], suffix[i]) - height[i]

        return total
                
