import heapq

class Location:
    def __init__():
        self.parent = "Fill whatever you want"
        self.f_val = 0
        self.h_val = 0
        self.g_val = 0

    def CalcActualDist():
        return

    def HeuristicFunc():
        return

    def Children():
        return

    def AStarFunc(start,end):

        open_list = []
        closed_list = set()
        heapq.heapify(open_list)
        heapq.heappush(open_list,start)

        curr_loc = start
        while open_list:
            curr_loc = heapq.heappop(open_list,key = lambda k:k.f_val)

            if curr_loc == end:
                route = []
                while curr_loc.parent:
                    route.append(curr_loc)
                    current = current.parent
                route.append(current)
                return route

            else:
                for child in curr_loc.Children():
                    if child in open_list:
                        new_g_val = curr_loc.g_val + curr_loc.CalcActualDist(child)
                        if child.g_val > new_g_val:
                            child.g_val = new_g_val
                            child.parent = curr_loc

                    elif child in closed_list:
                        new_g_val = curr_loc.g_val + curr_loc.CalcActualDist(child)
                        if child.g_val > new_g_val:
                            heapq.heappush(open_list,child)
                            closed_list.remove(child)

                    else:
                        child.h_val = curr_loc.HeuristicFunc(child)
                        heapq.heappush(open_list,child)

            closed_list.add(curr_loc)