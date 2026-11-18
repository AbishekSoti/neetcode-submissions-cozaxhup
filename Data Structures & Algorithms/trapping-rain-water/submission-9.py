class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        tallest_height_left = list()

        tallest_height_seen = 0
        for i in range(0,len(height)):
            if height[i]>tallest_height_seen:
                tallest_height_left.append(height[i])
                tallest_height_seen = height[i]
            else:
                tallest_height_left.append(tallest_height_seen)

        tallest_height_right = [0] * n   
        tallest_height_seen = 0
        # for i in range(0,len(rheight)):
        #     if rheight[i]>tallest_height_seen:
        #         tallest_height_right.append(rheight[i])
        #         tallest_height_seen = rheight[i]
        #     else:
        #         tallest_height_right.append(tallest_height_seen)

        # tallest_height_right = list(reversed(tallest_height_right))

        for i in range(len(height)-1,-1,-1):
            if height[i]>tallest_height_seen:
                tallest_height_right[i] = height[i]
                tallest_height_seen = height[i] 
            else:
                tallest_height_right[i] = tallest_height_seen
        # print(tallest_height_right)
        for i in range(0,len(height)):
            res += min(tallest_height_left[i],tallest_height_right[i])-height[i]

        return res

