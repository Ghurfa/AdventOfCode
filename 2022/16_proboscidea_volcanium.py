class Room:
    def __init__(self, name: str, flow_rate: int, neighbors: list[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors

class MetaRoom:
    def __init__(self, name: str, flow_rate: int, neighbor_dists: list):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbor_dists = neighbor_dists

def score(current: MetaRoom, visited_rooms: dict[MetaRoom, bool], moves_left: int): # moves_left assumes that valve has already been opened
    if moves_left < 1:
        return 0
    score_from_curr = current.flow_rate * moves_left
    best_neighbor = 0
    visited_rooms[current] = True
    for (neighbor, neighbor_dist) in current.neighbor_dists:
        if neighbor_dist + 1 >= moves_left:
            break
        if not(visited_rooms[neighbor]):
            neighbor_score = score(neighbor, visited_rooms, moves_left - neighbor_dist - 1) # minus one to open
            best_neighbor = max(best_neighbor, neighbor_score)
    visited_rooms[current] = False
    return score_from_curr + best_neighbor

# in_transit_amt_left includes turning on valve
def score_two_player(arrived_pos: MetaRoom, in_transit_goal: MetaRoom, in_transit_amt_left: int, visited_rooms: dict[MetaRoom, bool], moves_left: int): 
    if moves_left < 1:
        return 0
    
    score_from_curr = arrived_pos.flow_rate * moves_left
    best_neighbor = score(in_transit_goal, visited_rooms, moves_left - in_transit_amt_left)
    visited_rooms[in_transit_goal] = True
    
    good_neighbors = 0 # only pick from the 4 closest neighbors. Trades accuracy for reduced runtime
    for (neighbor, neighbor_dist) in arrived_pos.neighbor_dists:
        neighbor_dist += 1 # plus one to open
        if neighbor_dist >= moves_left or good_neighbors > 4:
            break
        if not(visited_rooms[neighbor]):
            neighbor_score = 0
            visited_rooms[neighbor] = True
            good_neighbors += 1
            if neighbor_dist < in_transit_amt_left:
                neighbor_score = score_two_player(neighbor, in_transit_goal, in_transit_amt_left - neighbor_dist, visited_rooms, moves_left - neighbor_dist)
            else:
                neighbor_score = score_two_player(in_transit_goal, neighbor, neighbor_dist - in_transit_amt_left, visited_rooms, moves_left - in_transit_amt_left)
            best_neighbor = max(best_neighbor, neighbor_score)
            visited_rooms[neighbor] = False

    return score_from_curr + best_neighbor

# Breadth-first traversal to get all distances from a start room
def get_dists(start_node: Room, name_to_room: dict) -> list[(Room, int)]:
    dists = dict()
    dists[start_node] = 0
    queued = set()
    queue = [start_node]
    while len(queue) > 0:
        curr = queue.pop(0)
        for neighbor in curr.neighbors:
            if not(neighbor in queued):
                queued.add(neighbor)
                dists[name_to_room[neighbor]] = dists[curr] + 1
                queue.append(name_to_room[neighbor])
    
    return dists

def main():
    # target_line_num = 10
    rooms = dict()
    with open("16input.txt", encoding='UTF-8') as file:
        for line in file:
            parts = line.strip().split(' ')
            name = parts[1]
            flow_rate = int(parts[4].split('=')[1].split(';')[0])
            neighboring_rooms = [part.split(',')[0] for part in parts[9:]]
            rooms[name] = Room(name, flow_rate, neighboring_rooms)

    meta_rooms = {room_name: MetaRoom(room_name, rooms[room_name].flow_rate, dict()) for room_name in rooms if rooms[room_name].flow_rate > 0}
    for meta_room_name in meta_rooms:
        room_dists = get_dists(rooms[meta_room_name], rooms)
        meta_neighbors = [(meta_rooms[neighbor_room.name], room_dists[neighbor_room]) for neighbor_room in room_dists if neighbor_room.flow_rate > 0]
        meta_neighbors.sort(key=lambda x: x[1])
        meta_rooms[meta_room_name].neighbor_dists = meta_neighbors


    # rooms_v2 = [Room(rooms[room_name].flow_rate, get_dists(rooms[room_name], rooms)) for room_name in rooms.keys() if rooms[room_name].flow_rate > 0]

    # start_room = rooms_v2
    start_name = 'AA'
    start_room = rooms[start_name]

    # assume start room has flow rate zero
    dists_from_start = get_dists(rooms[start_name], rooms)
    start_meta_neighbors = [(meta_rooms[neighbor_room.name], dists_from_start[neighbor_room]) for neighbor_room in dists_from_start if neighbor_room.flow_rate > 0]
    start_meta_room = MetaRoom(start_name, start_room.flow_rate, start_meta_neighbors)
    meta_rooms[start_name] = start_meta_room
    moves_left = 26

    scr = score(start_meta_room, {meta_rooms[x]: False for x in meta_rooms}, moves_left)
    for (close_room, close_dist) in start_meta_neighbors:
        for (far_room, far_dist) in start_meta_neighbors:
            if (far_dist >= close_dist) and (far_room != close_room):
                visited = {meta_rooms[x]: False for x in meta_rooms}
                visited[far_room] = True
                visited[close_room] = True
                new_score = score_two_player(close_room, far_room, far_dist - close_dist, visited, moves_left - close_dist - 1)
                scr = max(scr, new_score)
    print(scr)
    global iter_count
    # print(iter_count)

if __name__ == "__main__":
    main()
