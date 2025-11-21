def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    keys = [x for x in rooms[0]]
    rooms[0] = True
    while keys:
        room_num = keys.pop()
        if rooms[room_num] != True:
            for key in rooms[room_num]:
                if key not in keys:
                    keys.append(key)
            rooms[room_num] = True
    for room in rooms:
        if room != True:
            return False
    return True

def canVisitAllRooms_v_2(self, rooms: List[List[int]]) -> bool:
    n = len(rooms)
    visited = [False] * n
    stack = [0]
    visited[0] = True

    while stack:
        room = stack.pop()
        for key in rooms[room]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
