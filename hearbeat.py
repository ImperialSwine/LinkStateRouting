#Sends heartbeat to all neighbors
#Will send out heartbeat packet every _ seconds (specified in main program)
def heartbeat():
    global our_router

    for neighbor in heartbeat_list:
        our_router.sendto(bytes(router_id,"utf-8"),(local_host, int(router_direct[neighbor])))
    return
