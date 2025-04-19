// Maciej Ciepiela, 347677

#include "router.h"

void send_distance_vector(int sockfd, interface* interfaces, int num_interfaces) {
    for(int i = 0; i<num_interfaces;i++){
        struct in_addr broadcast;
        broadcast.s_addr = interfaces[i].net.s_addr | ~mask_to_bits(interfaces[i].mask);
        
        struct sockaddr_in destination;
        destination.sin_family = AF_INET;
        destination.sin_port = htons(PORT);
        destination.sin_addr = broadcast;

        for (int j = 0; j < num_routes; j++) {
            if(routing_table[j].unreachable && routing_table[j].max_send >= MAX_SEND_INFINITIES){
                if(!routing_table[j].directly){
                    for (int k = j; k < num_routes - 1; k++) {
                        routing_table[k] = routing_table[k + 1];
                    }
                    num_routes--;
                    j--;
                } 
                continue;    
            }

            uint8_t packet[9];
            memcpy(packet, &routing_table[j].net, 4);
            uint8_t mask = routing_table[j].mask;
            packet[4] = mask;
            uint32_t dist = routing_table[j].unreachable ? htonl(INFINITY_DISTANCE) : htonl(routing_table[j].distance);
            memcpy(packet + 5, &dist, 4);

            ssize_t datagram_len = sendto(sockfd, packet, sizeof(packet), 0, (struct sockaddr*)&destination, sizeof(destination));
            if (datagram_len < 0) {
                if(routing_table[j].net.s_addr == interfaces[i].net.s_addr){
                    routing_table[j].unreachable = 1;
                }
            }
            else{
                for(int k = 0; k < num_routes; k++) {
                    if(routing_table[k].net.s_addr == interfaces[i].net.s_addr){
                        routing_table[k].unreachable = 0;
                        routing_table[k].distance = interfaces[i].distance;
                        routing_table[k].max_send = 0;
                }}
            }

            if (routing_table[j].unreachable) {
                routing_table[j].max_send++;
            }
        }
    }
}