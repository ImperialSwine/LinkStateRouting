#Read file and get router information

def get_router(req_file):
    with open(req_file) as file:
        lines = file.readlines()
        lines[1] = int(lines[1].replace("\n","")) + 2

        for i in range(lines[1]):
            if i == 0:
                router0 = lines[i].split()
                if router0[0] not in router_direct:
                    router_direct[router0[0]] = router0[1]
            elif i == 1:
                pass
            else:
                router = lines[i].split()
                if router[0] not in router_direct:
                    router_direct[router[0]] = router[2]
                if  "%s" % (router0[0]) not in cost_direct:
                    cost_direct["%s" % (router[0])] = router[1]

    #Build hearbeat list and heartbeat_dict
    #Router knows which routers it needs to look out for when listening for heartbeats
    for _ in router_direct:
        if _ == router0[0]:
            pass
        else:
            heartbeat_list.append(_)

    for _ in heartbeat_list:
        heartbeat_dict[_] = 3

    return router0[0]
