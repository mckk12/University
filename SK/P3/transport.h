// Maciej Ciepiela, 347677

#ifndef TRANSPORT_H
#define TRANSPORT_H

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/poll.h>
#include <sys/time.h>

#define PACKET_SIZE 1000
#define WINDOW_SIZE 500
#define TIMEOUT_MS 2000

typedef struct{
    char received_data[PACKET_SIZE];
} PacketsData;

void ERROR(const char* str);
void run_transport(struct sockaddr_in server_address, const char* filename, int total_size);
int send_packet(int sockfd, struct sockaddr_in* server_address, int start, int length);
int send_requests(int sockfd, struct sockaddr_in* server_address, int packet_amount, int lfr, int size, int packet_receive[]);
int receive_response(int sockfd, struct sockaddr_in* server_address, PacketsData *data, int packet_receive[], int packets_to_send, int lfr);

#endif
