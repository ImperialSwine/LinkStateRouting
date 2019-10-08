#Function to send packet to neighbors with info (should broadcast every 1s)
#Will broadcast link state every second

def broadcast(link_packet):
    global our_router

    for neighbor in router_direct:
        format_packet = bytes("?".join(link_packet), "utf-8")
        our_router.sendto(format_packet,(local_host, int(router_direct[neighbor])))
    return
