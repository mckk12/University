// Maciej Ciepiela, 347677

#ifndef traceroute_h
#define traceroute_h

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

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

#define PACKETS_PER_TTL 3
#define MAX_TTL 30
#define TIMEOUT 1000


u_int16_t compute_icmp_checksum(const void *buff, int length);

int send_icmp_requests(int sockfd, int ttl, struct sockaddr_in recipient, int pid, struct timeval send_times[]);

int receive_icmp_replies(int sockfd, int pid, int ttl, struct timeval send_times[], char ip_strs[][INET_ADDRSTRLEN], int *time_sum);

void traceroute(int sockfd, struct sockaddr_in recipient);

#endif
