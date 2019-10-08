#Function that organizes all packets recieved and forwards link-state packets
def receive_and_forward(packets_received):
    global our_router, already_sent
    our_router.settimeout(0.1)

    try:
        data, addr = our_router.recvfrom(1024)
        data = data.decode("utf-8")

        if "?" in data:
            data = data.split("?")
            if (data[0] not in already_sent):
                for neighbor in router_direct:
                    our_router.sendto(bytes("?".join(data),"utf-8"),(local_host, int(router_direct[neighbor])))

                already_sent.append(data[0])
                if (data not in packets_received):
                    packets_received.append(data)
        elif data in heartbeat_dict:
            beat = heartbeat_dict[data] + 1
            heartbeat_dict[data] = beat

    except socket.timeout:
        our_router = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        our_router.bind((local_host, int(router_direct[router_id])))

    return packets_received
