// Maciej Ciepiela, 347677

#include "transport.h"

int receive_response(int sockfd, struct sockaddr_in* server_address, PacketsData *packet, int *packet_receive, int packets_to_send, int lfr) {
    struct pollfd fds[1];
    fds[0].fd = sockfd;
    fds[0].events = POLLIN;
    int ready = poll(fds, 1, 500);
    if (ready < 0) {
        ERROR("poll");
    } else if (ready == 0) {
        return 0; 
    }

    char buffer[PACKET_SIZE + 64];
    socklen_t addr_len = sizeof(*server_address);
    ssize_t len = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)server_address, &addr_len);
    if (len < 0) {
        ERROR("recvfrom");
    }else if (len == 0) {
        return 0; 
    }
    int start, length;
    int header = sscanf(buffer, "DATA %d %d\n", &start, &length);
    if (header != 2) {
        return 0;
    }

    int packet_index = start / PACKET_SIZE;
    if (packet_index <= lfr || packet_index >= packets_to_send || packet_receive[packet_index]) {
        return 0;
    }

    char *data = strstr(buffer, "\n") + 1;

    packet_receive[packet_index] = 1;
    int in_window_index = packet_index - lfr - 1;
    memcpy(packet[in_window_index].received_data, data, length);

    return 1;
}