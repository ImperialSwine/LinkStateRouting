def output_summary(topology):
    print("I am router %s" % (router_id))
    for key in topology:
        cost, path = dijkstra(topology, key)

        if key == router_id or cost == 100000:
            pass
        else:
            print("Least cost path to router " + str(key) + ":" + "".join(path) + " and the cost is " + str(cost))
    return
