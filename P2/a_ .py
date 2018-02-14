import heapq
import pickle

with open("node_hash.pickle","rb") as f:
    node_hash = pickle.load(f)
with open("adj_list.pickle","rb") as f:
    adj_list = pickle.load(f)
with open("distance_matrix.pickle","rb") as f:
    distance_matrix = pickle.load(f)

def heuristic_func(node):
    return distance_matrix[node_hash[node][0]]

def children(node):
    n = node_hash[node][0]
    return [e[0] for e in adj_list[n]]

open_list_depth={}
closed_list={}
parent={}

def AStarFunc(start,end = 2803176428):
    open_list = []
    d=0
    heapq.heappush(open_list,(heuristic_func(start),start))
    open_list_depth[start]=d

    curr_loc = start
    parent[start]=-1
    while open_list:
        _,curr_loc = heapq.heappop(open_list)
        d = open_list_depth[curr_loc]
        del open_list_depth[curr_loc]

        if curr_loc == end:
            # route = []
            # while curr_loc.parent:
            #     route.append(curr_loc)
            #     curr_loc = curr_loc.parent
            # route.append(curr_loc)
            # return route
            print(d)
            print(end)
            i=0
            node=end
            while True:
                pa=parent[node]
                if pa==-1:
                    exit()
                else:
                    print(pa)
                    node=pa


        else:
            for child in children(curr_loc):
                if child in open_list_depth:
                    if open_list_depth[child] > d+1:
                        open_list_depth[child] = d+1
                        parent[child]=curr_loc

                elif child in closed_list:
                    if closed_list[child] > d+1:
                        open_list_depth[child] = d+1
                        del closed_list[child]
                        heapq.heappush(open_list,(heuristic_func(child),child))
                        parent[child]=curr_loc

                else:
                    heapq.heappush(open_list,(heuristic_func(child),child))
                    open_list_depth[child]=d+1
                    parent[child]=curr_loc

        closed_list[curr_loc] = d


def main():
    start = 2684820160
    AStarFunc(start)


if __name__ == '__main__':
    main()
