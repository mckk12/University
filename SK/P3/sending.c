// Maciej Ciepiela, 347677

#include "transport.h"

int send_packet(int sockfd, struct sockaddr_in* server_address, int start, int length) {
    char buf[64];
    int n = snprintf(buf, sizeof(buf), "GET %d %d\n", start, length);
    fflush(stdout);
    if (n < 0) {
        ERROR("snprintf");
    }
    if (sendto(sockfd, buf, n, 0, (struct sockaddr*)server_address, sizeof(*server_address)) < 0) {
        return -1;
    }
    return 0;
}

int send_requests(int sockfd, struct sockaddr_in* server_address, int packet_amount, int lfr, int total_size, int packet_receive[]) {
    for (int i = 0; i < packet_amount; i++) {
        int current_index = lfr + 1 + i;
        int start = current_index * PACKET_SIZE;
        int length = (start + PACKET_SIZE > total_size) ? total_size % PACKET_SIZE : PACKET_SIZE;
        if (length <= 0) continue;
        if (packet_receive[current_index]) {
            continue;
        }
        if (send_packet(sockfd, server_address, start, length) < 0) {
            return -1;
        }
        packet_receive[current_index] = 0;  
    }
    return 0;
}