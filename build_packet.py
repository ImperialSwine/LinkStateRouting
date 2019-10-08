#Build link-state packet
#Will check for sufficient heartbeats and build appropriate link state packet to send out

def build_packet(router_id, costs):
    cost_copy = copy.deepcopy(costs)

    for rout in heartbeat_list:
        if heartbeat_dict[rout] < 3:
            for key in costs:
                if rout in key:
                    del cost_copy[key]

        else:
            heartbeat_dict[rout] = 0

    link_packet = []
    link_packet.append(str(router_id))
    link_packet.append(str(cost_copy))
    return link_packet
