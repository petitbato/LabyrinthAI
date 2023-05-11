import Communication

state = {"players": ["1", "2"], "current": 0, "positions": [1, 48], "board": [{"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": 17}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 1}, {"N": False, "E": False, 
"S": True, "W": True, "item": 16}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 18}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, 
"E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 12}, {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": False, "S": True, "W": True, "item": 13}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 4}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": 
True, "item": 5}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 23}, {"N": True, "E": False, "S": True, "W": True, "item": 21}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": True, "E": True, "S": False, 
"W": False, "item": 14}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": True, "S": 
False, "W": True, "item": 20}, {"N": True, "E": False, "S": True, "W": True, 
"item": 9}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 15}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 22}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": False, "E": True, "S": True, "W": True, "item": 19}, {"N": True, "E": False, "S": False, "W": True, "item": None}], "tile": {"N": True, "E": False, "S": True, "W": False, "item": None}, "target": 17, "remaining": [4, 4]}



def test_localize() :
    assert Communication.localize(3) == (3, 0)
    assert Communication.localize(47) == (5, 6)

def test_inv_localize() :
    assert Communication.inv_localize((6, 6)) == 48
    assert Communication.inv_localize((1, 2)) == 15

def test_BFS() :
    assert Communication.BFS((0,0), (3,1)) == 9
    assert Communication.BFS((2, 4), (6, 4)) == 27

def test_boardUpdate() :
    assert Communication.state["positions"] == [8, 48]

def test_canCross() :
    assert Communication.canCross(state["board"][3]) == ["E", "S"]

def test_distance() :
    assert Communication.distance((0,0), (3,4)) == 5
    assert Communication.distance((0,0), (50, 0)) == 50

def test_findNewPos():
    assert Communication.findNewPos("N", (0,0)) == None
    assert Communication.findNewPos("N", (0,2)) == (0,1)

def test_slideTiles() :
    assert Communication.slideTiles(state["board"], state["tile"], "A") != [{"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": 17}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 1}, {"N": False, "E": False, 
"S": True, "W": True, "item": 16}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 18}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, 
"E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 12}, {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": False, "S": True, "W": True, "item": 13}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 4}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": 
True, "item": 5}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 23}, {"N": True, "E": False, "S": True, "W": True, "item": 21}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": True, "E": True, "S": False, 
"W": False, "item": 14}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": True, "S": 
False, "W": True, "item": 20}, {"N": True, "E": False, "S": True, "W": True, 
"item": 9}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 15}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 22}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": False, "E": True, "S": True, "W": True, "item": 19}, {"N": True, "E": False, "S": False, "W": True, "item": None}]

def test_successors() :
    assert Communication.successors((0,0)) == [(0,1), (1,0)]