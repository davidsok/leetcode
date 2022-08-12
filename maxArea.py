def maxArea(height: list[int]) -> int:
        
        # Two pointers solution
        max_area = 0     # this variable store the answer
        left, right = 0, len(height) - 1        # two pointers at each side
        
        # find the max Area
        while left < right:
            
            # Area = Width x Height 
            # (width is obvs the distance between the two)
            # (height can only be the min of the 2 heights- else water would splash out)
            curArea = (right - left) * min(height[left], height[right])
            max_area = max(max_area, curArea)     # check if the new one is bigger
            
            # if left height is smaller, move it in, else move right in 
            if height[left] < height[right]:
                print('left', left, 'height', height[left])
                print('right', right, 'height', height[right])
                while(height[left+1] < height[left]):
                    left += 1
                left += 1
            else:
                print('left', left, 'height', height[left])
                print('right', right, 'height', height[right])
                while(height[right-1] < height[right]):
                    right -= 1
                right -= 1
        
        #return Answer
        print(max_area)
        return max_area

    
height = [1,8,6,2,5,4,8,3,7]
maxArea(height)