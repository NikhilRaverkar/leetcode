class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        visited.add(0)
        self.visit(rooms[0], rooms, visited)
        if len(visited) == len(rooms):
            return True

        return False

    def visit(self, key, rooms, visited):
        for accessible in key:
            if accessible not in visited:
                visited.add(accessible)
                self.visit(rooms[accessible], rooms, visited)



