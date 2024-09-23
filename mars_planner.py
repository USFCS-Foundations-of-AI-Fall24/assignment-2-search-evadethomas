## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search, depth_first_search

class RoverState :
    def __init__(self, loc="station", sample_extracted=False, holding_sample=False, holding_tool=False, charged=False):
        self.loc = loc
        self.sample_extracted=sample_extracted
        self.holding_sample = holding_sample
        self.holding_tool = holding_tool
        self.charged=charged
        self.prev = None

    ## you do this.
    def __eq__(self, other):
      return (self.loc == other.loc and
                self.sample_extracted == other.sample_extracted and
                self.holding_sample == other.holding_sample and
                self.charged == other.charged and
                self.holding_tool == other.holding_tool)


    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}\n" +
                f"Holding Tool? {self.holding_tool}\n")

    def __hash__(self):
        return self.__repr__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev=state
    return r2

def move_to_station(state) :
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2
# add tool functions here

def pick_up_tool(state) :
    r2 = deepcopy(state)
    if state.loc == "station":
        r2.holding_tool = True
    r2.prev = state
    return r2

def drop_tool(state) :
    r2 = deepcopy(state)
    if state.loc == "station" and state.holding_tool == True:
        r2.holding_tool = False
    r2.prev = state
    return r2

def use_tool(state) :
    if state.holding_tool == True:
        return pick_up_sample(state)
    return state

def pick_up_sample(state) :
    r2 = deepcopy(state)
    r2.sample_extracted = True
    if state.sample_extracted and state.loc == "sample" and state.holding_tool == True:
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "station" and state.holding_tool == True:
        r2.holding_sample = False
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.charged = True
    r2.prev = state
    return r2


action_list = [charge, drop_sample, pick_up_sample, pick_up_tool, drop_tool, use_tool,
               move_to_sample, move_to_battery, move_to_station]

def battery_goal(state) :
    return state.loc == "battery"
## add your goals here.

def mission_complete(state) :
    return state.loc == "battery" and state.charged == True and state.sample_extracted == True and state.holding_sample == False and state.holding_tool == False

def go_to_sample(state) :
    return state.loc == "sample" and state.holding_tool == True and state.charged == True and state.holding_sample == False

def remove_sample(state) :
    return state.holding_sample == True and state.holding_tool == True and state.charged == True and state.sample_extracted == True and state.loc == "sample"

def return_to_charger(state) :
    return mission_complete(state)

if __name__=="__main__" :
    s = RoverState()

    # Mission complete tests:

    # try:
    #     bfs_result, bfs_count = breadth_first_search(s, action_list, mission_complete)
    #     print("BFS state count: ", bfs_count)

    # except TypeError:
    #     print("No solution found for bfs")
    #     dfs_count = "No result found"

    # try:
    #     dfs_result, dfs_count = depth_first_search(s, action_list, mission_complete)
    #     print("DFS state count: ", dfs_count)
    # except TypeError:
    #     print("No solution found for dfs")
    #     dfs_count = "No result found"

    # try:
    #     ldfs_result, ldfs_count = depth_first_search(s, action_list, mission_complete, limit=2)
    #     print("DFS state count: ", dfs_count)
    # except TypeError:
    #     print("No solution found for dfs")
    #     ldfs_count = "No result found"

    # print("Final DFS result count: ", dfs_count)
    # print("Final BFS result count: ", bfs_count)
    # print("Final LDFS result count: ", ldfs_count)

    # print("Final DFS result: ", dfs_result)
    # print("Final BFS result: ", bfs_result)
    # print("Final LDFS result : ", ldfs_result)

    # Partitioned function tests

    functions = [go_to_sample, remove_sample, return_to_charger]
    
    s1 = RoverState()
    s2 = RoverState()
    s3 = RoverState()

    for i in functions:

        print(i, "starting states: ", "s1: ", s1, "s2: ", s2, "s3: ", s3)

        try:
            bfs_result, bfs_count = breadth_first_search(s1, action_list, i)
            print("BFS state count: ", bfs_count)
        except TypeError:
            print("No solution found for bfs")
            dfs_count = "No result found"

        try:
            dfs_result, dfs_count = depth_first_search(s2, action_list, i)
            print("DFS state count: ", dfs_count)
        except TypeError:
            print("No solution found for dfs")
            dfs_count = "No result found"

        try:
            ldfs_result, ldfs_count = depth_first_search(s3, action_list, i, limit=10)
            print("DFS state count: ", dfs_count)
        except TypeError:
            print("No solution found for dfs")
            ldfs_count = "No result found"

        

        print(str(i), ":")
        print("Final DFS result count: ", dfs_count)
        print("Final BFS result count: ", bfs_count)
        print("Final LDFS result count: ", ldfs_count)

        print("Final DFS result: ", dfs_result)
        print("Final BFS result: ", bfs_result)
        print("Final LDFS result : ", ldfs_result)

        s1 = bfs_result[0]
        s2 = dfs_result[0]
        s3 = ldfs_result[0]

   


