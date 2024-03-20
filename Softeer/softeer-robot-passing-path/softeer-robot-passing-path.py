import copy
import sys
from typing import List, Tuple


class Point:
    """
    This is Point class
    :class variables: x (int), y (int)
    """
    def __init__(self, _x, _y):
        self.__x = _x
        self.__y = _y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, _x):
        self.__x = _x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, _y):
        self.__y = _y

    def __copy__(self):
        return Point(self.x, self.y)

    def __str__(self):
        return "[{0}] x = {1}, y = {2}".format(self.__class__.__name__, self.__x, self.__y)


class Robot:
    """
    This is Robot class
    :class variables: start point (Point), current point (Point), direction (Point), visited (List[List], optional)
    :global variables: H (int) and W (int)
    """
    global H, W

    def __init__(self, _s, _c, _d, _v=None):
        self.__start = _s # starting point (Type: Final[Point])
        self.__current = _c # current point (Type: Point)
        self.__direct = _d # starting direction (Type: Final[Point])

        if not _v:
            self.__visited = copy.deepcopy([[False for _ in range(W)] for _ in range(H)])
        else:
            self.__visited = _v

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, _s):
        self.__start = _s

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, _c):
        self.__current = _c

    @property
    def direct(self):
        return self.__direct

    @direct.setter
    def direct(self, _d):
        self.__direct = _d

    @property
    def visited(self):
        return self.__visited

    @visited.setter
    def visited(self, _v):
        self.__visited = _v

    def __copy__(self):
        return Robot(self.__start, self.__current, self.__direct, self.__visited)

    def __deepcopy__(self, memodict={}):
        return Robot(copy.copy(self.__start), copy.copy(self.__current), copy.copy(self.__direct),
                     copy.deepcopy(self.visited))

    def __str__(self):
        return "[{0}] start point = {1}, current point = {2}, direct = {3}, visited = {4}"\
            .format(self.__class__.__name__, self.__start, self.__current, self.__direct, self.__visited)


def input_data() -> Tuple[int, int, List[List]]:
    """
    This is method for given input
    :return: given height, weight, and map (Tuple)
    """
    _H, _W = map(int, sys.stdin.readline().split())
    _given_map = [list(sys.stdin.readline().rstrip()) for _ in range(_H)]
    return _H, _W, _given_map


def get_direction_string(_direct: Point) -> str:
    """
    This is method for getting direction string when direction is given
    :param _direct: robot looking direction (Point)
        when _direct is (-1, 0) means robot is looking west  ("<")
                        (0,  1) means robot is looking south ("v")
                        (1,  0) means robot is looking east  (">")
                        (0, -1) means robot is looking north ("^")
    :return: direction string (str)
    """
    _x, _y = _direct.x, _direct.y
    if _x == -1 and _y == 0:
        return "<"
    elif _x == 0 and _y == 1:
        return "v"
    elif _x == 1 and _y == 0:
        return ">"
    else:
        return "^"


def go_straight(_given_map: List[List]) -> bool:
    """
    This is method for checking whether robot can go straight
    :param _given_map: given map (List[List])
    :return: is it possible to go straight? (bool)
    """
    global robot
    _robot_copy = robot.__deepcopy__()
    _s = _robot_copy.start # instance ref
    _p = _robot_copy.current # instance ref
    _d = _robot_copy.direct # list ref
    _v = _robot_copy.visited # list ref

    for i in range(2):
        _p.x = _p.x + _d.x
        _p.y = _p.y + _d.y

        if 0 <= _p.x < len(_given_map[0]) and 0 <= _p.y < len(_given_map):
            if not _v[_p.y][_p.x] and _given_map[_p.y][_p.x] == '#':
                _v[_p.y][_p.x] = True
            else:
                return False
        else:
            return False
    else:
        robot = _robot_copy
        return True


def go_straight_after_turn_left(_given_map: List[List]) -> bool:
    """
    This is method for checking whether robot can go straight after turning left
    :param _given_map: given map (List[List])
    :return: is it possible to go straight after turning left? (bool)
    """
    global robot
    _robot_copy = robot.__deepcopy__()
    _s = _robot_copy.start  # instance ref
    _c = _robot_copy.current  # instance ref
    _d = _robot_copy.direct # instance ref
    _v = _robot_copy.visited  # list ref

    if _d.x == -1 and _d.y == 0: _d = Point(0, 1)
    elif _d.x == 0 and _d.y == 1: _d = Point(1, 0)
    elif _d.x == 1 and _d.y == 0: _d = Point(0, -1)
    elif _d.x == 0 and _d.y == -1: _d = Point(-1, 0)
    _robot_copy.direct = _d

    for i in range(2):
        _c.x = _c.x + _d.x
        _c.y = _c.y + _d.y

        if 0 <= _c.x < len(_given_map[0]) and 0 <= _c.y < len(_given_map):
            if not _v[_c.y][_c.x] and _given_map[_c.y][_c.x] == '#':
                _v[_c.y][_c.x] = True
            else:
                return False
        else:
            return False
    else:
        robot = _robot_copy
        return True


def go_straight_after_turn_right(_given_map: List[List]) -> bool:
    """
    This is method for checking whether robot can go straight after turning right
    :param _given_map: given map (List[List])
    :return: is it possible to go straight after turning right? (bool)
    """
    global robot
    _robot_copy = robot.__deepcopy__()
    _s = _robot_copy.start  # instance ref
    _c = _robot_copy.current  # instance ref
    _d = _robot_copy.direct # instance ref
    _v = _robot_copy.visited  # list ref

    if _d.x == -1 and _d.y == 0: _d = Point(0, -1)
    elif _d.x == 0 and _d.y == -1: _d = Point(1, 0)
    elif _d.x == 1 and _d.y == 0: _d = Point(0, 1)
    elif _d.x == 0 and _d.y == 1: _d = Point(-1, 0)
    _robot_copy.direct = _d

    for i in range(2):
        _c.x = _c.x + _d.x
        _c.y = _c.y + _d.y

        if 0 <= _c.x < len(_given_map[0]) and 0 <= _c.y < len(_given_map):
            if not _v[_c.y][_c.x] and _given_map[_c.y][_c.x] == '#':
                _v[_c.y][_c.x] = True
            else:
                return False
        else:
            return False
    else:
        robot = _robot_copy
        return True


def check_all_visited(_visited: List[List], _given_map: List[List]) -> bool:
    """
    This is method whether robot visits all nodes in given map
    :param _visited: robot visited map (List[List])
    :param _given_map: given map (List[List])
    :return: whether robot visits all nodes in given map? (bool)
    """
    for _y in range(len(_given_map)):
        for _x in range(len(_given_map[0])):
            if _given_map[_y][_x] == '#':
                if not _visited[_y][_x]: return False
    return True


if __name__ == '__main__':
    H, W, given_map = input_data()
    directions = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]

    # start points which consist of the starting point which can go straight at least twice for reducing complexity
    robots = []
    for h in range(H): # y direction
        for w in range(W): # x direction
            for d in range(len(directions)):
                sp = Point(w, h) # set starting point
                if given_map[sp.y][sp.x] == '#':
                    robot = Robot(_s=sp, _c=copy.copy(sp), _d=directions[d])
                    if go_straight(given_map):
                        robot.visited[sp.y][sp.x] = True
                        robots.append(robot)

    cnt = 0
    for rb in robots:
        stack = [rb]
        command = 'A'

        while stack:
            robot = stack.pop(0)

            if go_straight(given_map):
                command += "A"
                stack.append(robot)

            elif go_straight_after_turn_left(given_map):
                command += "LA"
                stack.append(robot)

            elif go_straight_after_turn_right(given_map):
                command += "RA"
                stack.append(robot)

        if check_all_visited(robot.visited, given_map):
            y, x = robot.start.y+1, robot.start.x+1
            directStr = get_direction_string(robot.direct)

            print(y, x)
            print(directStr)
            print(command)
            cnt += 1

        if cnt == 1: break
