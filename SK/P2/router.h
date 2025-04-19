// Maciej Ciepiela, 347677

#ifndef router_h
#define router_h

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <stdbool.h>
#include <time.h>

#include <assert.h>
#include <poll.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/socket.h>

#include <arpa/inet.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>

#define TURA_TIME 15 //seconds
#define MAX_ROUTES 256
#define PORT 54321
#define INFINITY_DISTANCE 4294967295U //(2^32 - 1)
#define MAX_SEND_INFINITIES 3

#define MAX_NEIGHBORS 128

typedef struct{
    struct in_addr ip;
    struct in_addr net;
    uint32_t distance;
    int mask;
} interface;

typedef struct{
    struct in_addr net;
    uint32_t distance;
    int mask;
    int directly;
    int unreachable;
    struct in_addr via;
    int max_send;
} route;

typedef struct {
    struct in_addr via;
    int missed_tours;
} neighbor_info;

void ERROR(const char* str);

void start_router(interface* interfaces, int num_interfaces);
uint32_t mask_to_bits(int mask);
void show_routing_table();

void send_distance_vector(int sock_fd, interface* interfaces, int num_interfaces);

void receive_distance_vector(int sock_fd , int num_interfaces, interface* interfaces);
bool is_own_address(struct in_addr addr, interface* interfaces, int num_interfaces);
int update_routing_table(struct in_addr ip, uint32_t distance, int mask, struct in_addr curr_via, int directly);

extern int num_routes;
extern route routing_table[MAX_ROUTES];

#endif