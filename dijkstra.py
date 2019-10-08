#Function when recieved all packets
def dijkstra(layout, goal):
    costs = {}
    path_tracker = {}

    unchecked_routers = copy.deepcopy(layout)
    for router in unchecked_routers:
        if router == router_id:
            costs[router] = 0
        else:
            costs[router] = 100000

    try:
        while unchecked_routers:
            best_rout = None
            for router in unchecked_routers:
                if best_rout == None:
                    best_rout = router
                elif costs[router] < costs[best_rout]:
                    best_rout = router

            for neighbor, cost in layout[best_rout].items():
                if float(cost) + costs[best_rout] < costs[neighbor]:
                    costs[neighbor] = float(cost) + costs[best_rout]
                    path_tracker[neighbor] = best_rout

            unchecked_routers.pop(best_rout)

        present_router = goal
        path = []
        while present_router != router_id:
            path.append(present_router)
            present_router = path_tracker[present_router]
        path.append(present_router)
        path.reverse()

    except KeyError:
        path = []
        pass

    return round(costs[goal],1) , path
