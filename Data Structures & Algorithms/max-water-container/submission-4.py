class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) -1 
        maxarea = 0

        while p1<p2:
            # Initialise heights
            h1 = heights[p1]
            h2 = heights[p2]

            # Calculate area, then move based on lowest hegith.
            if h2<h1:
                max_height = h2
                current_area = max_height * (p2-p1)
                p2-=1
            else:
                max_height = h1
                current_area = max_height * (p2-p1)
                p1+=1

            if current_area > maxarea:
                maxarea = current_area

            print(maxarea)

        return maxarea
            

        