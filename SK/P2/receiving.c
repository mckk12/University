// Maciej Ciepiela, 347677

#include "router.h"

neighbor_info neighbors[MAX_ROUTES];
int num_neighbors = 0;

bool is_own_address(struct in_addr addr, interface* interfaces, int num_interfaces) {
    for (int i = 0; i < num_interfaces; i++) {
        if (addr.s_addr == interfaces[i].ip.s_addr) {
            return true;
        }
    }
    return false;
}

void update_neighbor_activity(struct in_addr sender_ip) {
    for (int i = 0; i < num_neighbors; i++) {
        if (neighbors[i].via.s_addr == sender_ip.s_addr) {
            neighbors[i].missed_tours = 0;
            return;
        }
    }
    if (num_neighbors < MAX_ROUTES) {
        neighbors[num_neighbors].via = sender_ip;
        neighbors[num_neighbors].missed_tours = 0;
        num_neighbors++;
    }
}

void increment_missing_and_check() {
    for (int i = 0; i < num_neighbors; i++) {
        neighbors[i].missed_tours++;
        if (neighbors[i].missed_tours >= 3) {
            for (int j = 0; j < num_routes; j++) {
                if (routing_table[j].via.s_addr == neighbors[i].via.s_addr) {
                    routing_table[j].unreachable = 1;
                    routing_table[j].distance = INFINITY_DISTANCE;
                    routing_table[j].max_send = 0;
                }
            }
        }
    }
}

void receive_distance_vector(int sockfd, int num_interfaces, interface* interfaces)
{
    struct sockaddr_in sender;
    socklen_t sender_len = sizeof(sender);
    u_int8_t buffer[9];

    while (recvfrom(sockfd, buffer, 9, MSG_DONTWAIT, (struct sockaddr*)&sender, &sender_len) == 9) {
        struct in_addr net;
        memcpy(&net, buffer, 4);
        int mask = buffer[4];
        uint32_t dist;
        memcpy(&dist, buffer + 5, 4);
        dist = ntohl(dist);

        if (is_own_address(sender.sin_addr, interfaces, num_interfaces)) {
            continue;
        }

        update_neighbor_activity(sender.sin_addr);

        struct in_addr sender_net;
        for(int i = 0; i < num_interfaces; i++) {
            sender_net.s_addr = sender.sin_addr.s_addr & mask_to_bits(interfaces[i].mask);
            if (sender_net.s_addr == interfaces[i].net.s_addr) {
                break;
            }
        }

        uint32_t total = dist;
        for (int i = 0; i < num_interfaces; i++) {
            if ((sender_net.s_addr==interfaces[i].net.s_addr)) {
                total = (dist == INFINITY_DISTANCE) ? INFINITY_DISTANCE : interfaces[i].distance + dist;
                break;
            }   
        }

        for (int i = 0; i < num_routes; i++) {
            if (routing_table[i].net.s_addr == net.s_addr && routing_table[i].via.s_addr == sender.sin_addr.s_addr && !routing_table[i].directly) {
                routing_table[i].unreachable = 0;
                routing_table[i].max_send = 0;
                break;
            }
        }

        update_routing_table(net, total, mask, sender.sin_addr, 0);
    }

    increment_missing_and_check();
}

int update_routing_table(struct in_addr net, uint32_t distance, int mask, struct in_addr curr_via, int directly){
    for(int i = 0; i<num_routes;i++){
        if(routing_table[i].net.s_addr == net.s_addr){
            if(distance == INFINITY_DISTANCE && routing_table[i].via.s_addr == curr_via.s_addr){
                routing_table[i].unreachable = 1;
                routing_table[i].distance = INFINITY_DISTANCE;
            }
            else if(routing_table[i].distance > distance){
                routing_table[i].distance = distance;
                routing_table[i].via = curr_via;
                routing_table[i].mask = mask;
                routing_table[i].unreachable = 0;
                routing_table[i].max_send = 0;
            }
            return 0;
        }
    }
    if(num_routes < MAX_ROUTES){
        routing_table[num_routes].net = net;
        routing_table[num_routes].distance = distance;
        routing_table[num_routes].via = curr_via;
        routing_table[num_routes].mask = mask;
        routing_table[num_routes].unreachable = 0;
        routing_table[num_routes].directly = directly;
        routing_table[num_routes].max_send = 0;
        num_routes++;
        return 0;
    }
    return -1;
}
