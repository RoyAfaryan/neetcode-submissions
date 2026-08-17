class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        size = len(position)
        combined = [0]*size
        fleets = 0

        for i in range(size):
            time = (target - position[i]) / speed[i]     
            combined[i] = (position[i], speed[i], time)

        combined.sort(reverse=True)
        stack = []

        for i in range(size):
            stack.append(combined[i][2])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        

        return len(stack)