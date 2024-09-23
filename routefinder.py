import math
from queue import PriorityQueue

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="",
                 prev_state=None, g=0,h=0):
        self.location = location
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    map = map_state()
    start = map_state(start_state, None, 0, heuristic_fn(start_state))

    print("start: ", start.f)

    search_queue = PriorityQueue()
    open_list = {}
    closed_list = {}
    
    mars_graph = read_mars_graph("marsmap.txt")
    search_queue.put(start)
    print(mars_graph)

    while search_queue.empty() == False :

        current_state = search_queue.get()

        if goal_test(current_state) == True :

            while current_state.prev_state.location != start_state:
                print(current_state.prev_state)
                current_state = current_state.prev_state
            
            print("prev_state", current_state.prev_state)
            return current_state

        for i in mars_graph[current_state.location] :
            i_state = map_state(i, current_state, current_state.g + 1, heuristic_fn(i))

            if i_state.location in closed_list and (i_state.g >= closed_list[i_state.location].g == True) :
                 continue
            
            search_queue.put(i_state)

        closed_list[current_state.location] = current_state
        

    
    # starting nodes
        # h(n) - open list contains all
        # f(n) - 

    ## you do the rest.
def goal_test(current_state) :
    return current_state.location == "1,1"

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    nums = state.split(",")
    x = int(nums[0])
    y = int(nums[1])
    return math.sqrt((x - 1) ** 2 + (y - 1) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    mars_graph = {}
    with open(filename, 'r') as file:
        for line in file:
            loc = line.split(':')
            mars_graph[loc[0]] = loc[1].strip().split()
    return mars_graph
    

final_state = "A-star: ", a_star("8,8", sld, goal_test, use_closed_list=True)
print(final_state)