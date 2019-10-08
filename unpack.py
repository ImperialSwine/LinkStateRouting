#Will unpack link state packets and add their router dictionaries to an overall topology dictionary
def unpack(all_packets):
    topology = {}

    for packet in all_packets:
        topology[packet[0]] = ast.literal_eval(packet[1])

    return topology
