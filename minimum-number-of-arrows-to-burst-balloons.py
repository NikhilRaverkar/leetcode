class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)>0:
            points.sort(key=lambda x: x[1])
            arrows=1
            first_node=points[0][1]
            for point in points:
                if(point[0]>first_node):
                    first_node=point[1]
                    arrows+=1

            return arrows
        else:
            return 0
if __name__ =="__main__":
   print( Solution().findMinArrowShots([]))