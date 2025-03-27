// Maciej Ciepiela, 347677

#include "traceroute.h"

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <destination IP>\n", argv[0]);
        return EXIT_FAILURE;
    }

    struct sockaddr_in recipient;
    memset(&recipient, 0, sizeof(recipient));
    recipient.sin_family = AF_INET;
    if (inet_pton(AF_INET, argv[1], &recipient.sin_addr) != 1) {
        fprintf(stderr, "Invalid IP address\n");
        return EXIT_FAILURE;
    }

    int sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sockfd < 0) {
        fprintf(stderr, "Socket: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }

    traceroute(sockfd, recipient);

    if(close(sockfd)){
        fprintf(stderr, "Closing socket: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }
    
    return 0;
}
