#Written by Sachin Krishnamoorthy
#Assignment for Computer Networks and Applications

import socket
import time
import math
import argparse
import ast
import copy

#Functions
###################################################################################
from get_router import get_router
from build_packet import build_packet
from broadcast import broadcast
from hearbeat import hearbeat
from receive_and_forward import receive_and_forward
from unpack import unpack
from dijkstra import dijkstra
from output_summary import output_summary
##################################################################################
#Delcare Globals
router_direct = {}
heartbeat_list = []
heartbeat_dict = {}
cost_direct = {}
packets_received = []
already_sent = []
local_host = '127.0.0.1'
ROUTE_UPDATE_INTERVAL = 30
UPDATE_INTERVAL = 1
HEARTBEAT_UPDATE_INTERVAL = 0.05
###################################################################################
#Open and read initial file
parser = argparse.ArgumentParser();
parser.add_argument('router_file', type = str, help = "Given initial router")
args = parser.parse_args()

#Get informaton from first file
router_id = get_router(args.router_file)

#Initiate socket connection
our_router = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
our_router.bind((local_host, int(router_direct[router_id])))

#Start router protocol loop
#Time counters
i = 1
j = 1
k = 1
link_packet = build_packet(router_id, cost_direct)
time_start = time.time()

while True:
    # Send out heartbeat every 0.05 seconds
    if((time.time() - time_start) / (k*HEARTBEAT_UPDATE_INTERVAL) >= 1):
        heartbeat()
        k += 1

    #Send link packet every second
    if((time.time() - time_start) // (i*UPDATE_INTERVAL) == 1):
        link_packet = build_packet(router_id, cost_direct)
        broadcast(link_packet)
        i += 1

    #Update routes every 30 seconds
    if ((time.time() - time_start) // (ROUTE_UPDATE_INTERVAL*j) == 1):
        output_summary(unpack(packets_received))
        packets_received = []
        already_sent = []
        j+= 1

    packets_received = receive_and_forward(packets_received)
