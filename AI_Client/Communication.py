import socket
import json
import sys
import math
import copy


# Connexion au serveur de parties
s = socket.socket()
address = ('localhost', 3000)
s.connect(address)

port = int(sys.argv[1])

d ={
   "request": "subscribe",
   "port": port,
   "name": "boby-{}".format(port),
   "matricules": ["20278", "00000", port]
}
print(json.dumps(d))

request = json.dumps(d, indent='\t').encode()

s.send(request)

ans = s.recv(2048).decode()
ans = json.loads(ans)

if ans['response'] != 'ok':
    print(ans)
    sys.exit()

# Définitions de variables et de fonctions utiles

# Importé depuis le fichier game.py
Gates = {
    "A": {"start": 1, "end": 43, "inc": 7},
    "B": {"start": 3, "end": 45, "inc": 7},
    "C": {"start": 5, "end": 47, "inc": 7},
    "D": {"start": 13, "end": 7, "inc": -1},
    "E": {"start": 27, "end": 21, "inc": -1},
    "F": {"start": 41, "end": 35, "inc": -1},
    "G": {"start": 47, "end": 5, "inc": -7},
    "H": {"start": 45, "end": 3, "inc": -7},
    "I": {"start": 43, "end": 1, "inc": -7},
    "J": {"start": 35, "end": 41, "inc": 1},
    "K": {"start": 21, "end": 27, "inc": 1},
    "L": {"start": 7, "end": 13, "inc": 1},
}

def slideTiles(board, free, gate):
    start = Gates[gate]["start"]
    end = Gates[gate]["end"]
    inc = Gates[gate]["inc"]
    new_board = copy.deepcopy(board)
    dest = end
    src = end - inc
    while dest != start:
        new_board[dest] = new_board[src]
        dest = src
        src -= inc
    new_board[start] = free
    return new_board

def onTrack(index, gate):
    return index in range(
        Gates[gate]["start"],
        Gates[gate]["end"] + Gates[gate]["inc"],
        Gates[gate]["inc"],
    )

directions = ['N', 'E', 'S', 'W']

def localize(tile):
    return (tile % 7, tile // 7)

def test_localize() :
    assert localize(3) == (3, 0)

def findNewPos(card, pos):
    if ((card == 'N') and (pos[1]-1 >= 0)):
        np = (pos[0], pos[1]-1)
    elif ((card == 'S') and (pos[1]+1 <= 6)):
        np = (pos[0], pos[1]+1)
    elif ((card == 'W') and (pos[0] != 0)) :
        np = (pos[0]-1, pos[1])
    elif ((card == 'E') and (pos[0] != 6)) :
        np = (pos[0]+1, pos[1])
    else :
        return None
    return np

def inv_localize(pos):
    return pos[0] + pos[1]*7

def distance(pos1, pos2):
    D = math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)
    return D
     
def canCross(tile):
    poss = []
    ways = []
    for i in directions :
        print(state["board"][tile])
        if state["board"][tile][i] :
            poss.append(i)
    for j in poss :
        if j == 'N' :
            try :
                if state["board"][tile-7]['S'] :
                    ways.append(j)
            except :
                pass
        if j == 'E' :
            try :
                if state["board"][tile+1]['W'] :
                    ways.append(j)
            except :
                pass
        if j == 'S' :
            try :
                if state["board"][tile+7]['N'] :
                    ways.append(j)
            except :
                pass
        if j == 'W' :
            try :
                if state["board"][tile-1]['E'] :
                    ways.append(j)
            except :
                pass    
    return ways

gate = "C"

class Queue:
	def __init__(self):
		self.data = []

	def enqueue(self, value):
		self.data.append(value)

	def dequeue(self):
		return self.data.pop(0)

	def isEmpty(self):
		return len(self.data) == 0

def BFS(start, target):
    if target == None :
        return start
    targetObtainable = False
    q = Queue()
    distances = []
    parent = {}
    parent[start] = None
    q.enqueue(start)
    while not q.isEmpty():
        node = q.dequeue()
        print(node)
        print(node)
        print(target)
        print("NODE")
        if node == localize(target):
            targetObtainable = True
            break
        for successor in successors(node):
            # se rapprocher au max de la target
            if successor not in parent:
                distances.append((distance(successor, localize(target)), successor))
                parent[successor] = node
                q.enqueue(successor)
    if targetObtainable :
        return target
    if node != None :
        minDistance = 100
        bestTile = playerPos
        for i in distances :
            print(i)
            if i[0] < minDistance :
                minDistance = i[0]
                bestTile = inv_localize(i[1])
        return bestTile
    return playerPos
#    path = []
#    while node is not None:
#        path.append(node)
#        node = parent[node]
#    return node


def successors(current_tile):
    res = []
    for i in directions:
        if i in canCross(inv_localize(current_tile)):
            np = findNewPos(i, current_tile)
            if np != None :
                res.append(np)
    return res


with socket.socket() as s:
    s.bind(('', port))
    s.settimeout(1)
    s.listen()
    alive = True
    while alive:
        try:
            client, address = s.accept()
            message = client.recv(20480).decode()
            answer = json.loads(message)
            print(answer)
            if answer["request"] == "play" :
                answer = json.loads(message)
                print(answer["state"])
                state = answer["state"]
                targetPos = None
                state["board"] = slideTiles(state["board"], state["tile"], gate)
                new_positions = []
                for position in state["positions"]:
                    if onTrack(position, gate):
                        if position == Gates[gate]["end"]:
                            new_positions.append(Gates[gate]["start"])
                            continue
                        new_positions.append(position + Gates[gate]["inc"])
                        continue
                    new_positions.append(position)
                state["positions"] = new_positions
                playerID = state["current"]
                playerPos = state["positions"][playerID]
                print(state["board"])
                print(playerPos)
                for tile in state["board"] :
                    if tile["item"] == state["target"] :
                        targetPos = state["board"].index(tile)
                        print(targetPos)
                        print('HELLO')
                if targetPos == None :
                    new_position = BFS(localize(playerPos), None)
                else :
                    new_position = BFS(localize(playerPos), targetPos)
                move = {'move' :{'tile': state["tile"],'gate': gate,'new_position': int(new_position)}}
                print(json.dumps(move, indent='\t') + 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZz')
                print(state['tile'])
                client.send(json.dumps(move).encode())
            elif message == "{\"request\": \"ping\"}" :
                client.send(json.dumps({'response': 'pong'}).encode())
                print('OK')
        except socket.timeout:
            pass