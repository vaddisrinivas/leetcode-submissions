# https://leetcode.com/problems/keys-and-rooms
# https://leetcode.com/problems/871-keys-and-rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def v(room):
            nonlocal rooms, visited
            # print(room,visited)
            if room in visited:
                return
            else:
                visited.add(room)
                for i in rooms[room]:
                    if i not in visited:
                        v(i)
        v(0)
        # print(visited)
        return len(visited)==len(rooms)
        