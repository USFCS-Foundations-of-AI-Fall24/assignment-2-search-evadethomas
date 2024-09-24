from routefinder import a_star, goal_test, h1, sld
from search_algorithms import breadth_first_search, depth_first_search
import mars_planner
import antenna_freq

# Eva DeThomas

def question2():

    s = mars_planner.RoverState()

    # Mission complete results

    action_list = mars_planner.return_action_list()

    try:
        bfs_result, bfs_count = breadth_first_search(s, action_list, mars_planner.mission_complete)

    except TypeError:
        print("No solution found for bfs")
        dfs_count = "No result found"

    try:
        dfs_result, dfs_count = depth_first_search(s, action_list, mars_planner.mission_complete)
    except TypeError:
        print("No solution found for dfs")
        dfs_count = "No result found"

    try:
        ldfs_result, ldfs_count = depth_first_search(s, action_list, mars_planner.mission_complete, limit=6)
    except TypeError:
        print("No solution found for dfs")
        ldfs_count = "No result found"

    print("\n")
    print("Final mission complete DFS result count: ", dfs_count)
    print("Final mission complete BFS result count: ", bfs_count)
    print("Final mission complete LDFS result count: ", ldfs_count, "limit is 6")

    print("\n")
    print("Final mission complete DFS result: ", dfs_result)
    print("Final mission complete BFS result: ", bfs_result)
    print("Final mission complete LDFS result : ", ldfs_result)
    print("\n")

    # Partitioned function results

    functions = [mars_planner.go_to_sample, mars_planner.remove_sample, mars_planner.return_to_charger]
    
    s1 = mars_planner.RoverState()
    s2 = mars_planner.RoverState()
    s3 = mars_planner.RoverState()

    for i in functions:

        try:
            bfs_result, bfs_count = breadth_first_search(s1, action_list, i)
        except TypeError:
            print("No solution found for bfs")
            dfs_count = "No result found"

        try:
            dfs_result, dfs_count = depth_first_search(s2, action_list, i)
        except TypeError:
            print("No solution found for dfs")
            dfs_count = "No result found"

        try:
            ldfs_result, ldfs_count = depth_first_search(s3, action_list, i, limit=8)
        except TypeError:
            print("No solution found for dfs")
            ldfs_count = "No result found"

        
        print("\n")
        print(str(i), ":")
        print("\n")
        print(i, "Final DFS result count: ", dfs_count)
        print(i, "Final BFS result count: ", bfs_count)
        print(i, "Final LDFS result count: ", ldfs_count, "limit is 8")
        print("\n")

        print(i, "Final DFS result: ", dfs_result)
        print(i, "Final BFS result: ", bfs_result)
        print(i, "Final LDFS result : ", ldfs_result, "limit is 8")
        print("\n")

        # reseting the states (could be slightly different and still meet conditions)
        s1 = bfs_result[0]
        s2 = dfs_result[0]
        s3 = ldfs_result[0]

def question3():
    print("A-star path: ", a_star("8,8", sld, goal_test, use_closed_list = True))
    print("\n")
    print("Uniform-cost path: ", a_star("8,8", h1, goal_test, use_closed_list = True))

def question4():

    # Seemed unneccessary to break down over here - refer to antenna_freq.py

    antenna_freq.question4_main()

if __name__=="__main__" :

    # Note there are also main functions called "function_main" that I left in each file because it seemed like a waste to delete them

    print("Eva DeThomas\n")
    print("Question 2: \n")
    question2() # mars_planner
    print("\n")
    print("Question 3: \n")
    question3() # routefinder
    print("\n")
    print("Question 4: \n")
    question4()
    print("\n")
    

