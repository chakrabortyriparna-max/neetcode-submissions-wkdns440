class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Combine position and speed into pairs and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for p, s in cars:
            # Calculate time to reach the target
            time = (target - p) / s
            
            # If the stack is empty, or this car takes LONGER than the 
            # fleet ahead, it starts a new fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
        
        # The number of unique arrival times in the stack is the number of fleets
        return len(stack)