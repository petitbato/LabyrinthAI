import socket
import json
import sys
import math
import Strategy


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

request = json.dumps(d, indent='\t').encode()

s.send(request)

ans = s.recv(2048).decode()
ans = json.loads(ans)

if ans['response'] != 'ok':
    print(ans)
    sys.exit()

# Définitions de variables et de fonctions utiles
directions = ['N', 'E', 'S', 'W']
def localize(tile):
    y = 0
    while tile > 6:
        tile -= 7
        y+= 1
    x = tile
    return (x, y)

def findNewPos(card, pos):
    if ((card == 'N') and (pos[1]-7 >= 0)):
        np = (pos[0], pos[1]-7)
    elif ((card == 'S') and (pos[1]+7 <= 48)):
        np = (pos[0], pos[1]+7)
    elif ((card == 'W') and (pos[0] not in [0, 7, 14, 21, 28, 35, 42])) :
        np = (pos[0]-1, pos[1])
    elif ((card == 'E') and (pos[0] not in [6, 13, 20, 27, 34, 41, 48])) :
        np = (pos[0]+1, pos[1])
    return np

def inv_localize(pos):
    tile = pos[0] + pos[1]*7
    return tile

def distance(pos1, pos2):
    D = math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)
    return D
     
def canCross(tile):
    poss = []
    for i in directions :
        if tile[i] :
            poss.append(i)
    return poss

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
    targetObtainable = False
    q = Queue()
    distances = []
    parent = {}
    parent[start] = None
    q.enqueue(start)
    while not q.isEmpty():
        node = q.dequeue()
        if node == localize(target):
            targetObtainable = True
            break
        for successor in successors(node):
            # se rapprocher au max de la target
            if successor not in parent:
                distances.append((distance(successor, localize(target)), successor))
                parent[successor] = node
                q.enqueue(successor)
        node = None
    if targetObtainable :
        return target
    minDistance = 100
    for i in distances :
        if i[0] < minDistance :
            minDistance = i[0]
            bestTile = inv_localize(i[1])
    return bestTile
    
#    path = []
#    while node is not None:
#        path.append(node)
#        node = parent[node]
#    return node


def successors(current_tile):
    res = []
    for i in directions:
        if i in canCross(current_tile):
            np = findNewPos(i, current_tile)
            res.append(np)
    return res


print(BFS((8, 1), successors, [(1, 9)]))

with socket.socket() as s:
    s.bind(('', port))
    s.settimeout(1)
    s.listen()
    alive = True
    while alive:
        try:
            client, address = s.accept()
            message = client.recv(20480).decode()
            if message != "{\"request\": \"ping\"}" :
                print(message)
                answer = json.loads(message)
                print(answer["state"])
                state = answer["state"]
                playerID = state["players"].index("boby-{}".format(port))
                playerPos = state["positions"][playerID]
                targetPos = 0
                for tile in state["board"] :
                    if tile["item"] == state["target"] :
                        targetPos = localize(state["board"].index(tile))
                        print(targetPos)
                if targetPos == 0 :
                    targetPos = "Free Tile"
                move = {
                    "tile": answer["state"]["tile"],
                    "gate": "A",
                   "new_position": 45
                  }
                print(move)
                client.send(json.dumps(move).encode())
            else :
                client.send(json.dumps({'response': 'pong'}).encode())
                print('OK')
        except socket.timeout:
            pass