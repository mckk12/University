// Maciej Ciepiela, 347677

#include "transport.h"

void ERROR(const char* str)
{
    fprintf(stderr, "%s: %s\n", str, strerror(errno));
    exit(EXIT_FAILURE);
}

int main(int argc, char *argv[]) {
    if (argc != 5) {
        fprintf(stderr, "Usage: %s <adres IP> <port> <nazwa pliku> <rozmiar>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int port = atoi(argv[2]);
    const char* filename = argv[3];
    int total_size = atoi(argv[4]);
    
    if (port <= 0 || port > 65535 || total_size <= 0) {
        ERROR("Invalid port or size");
    }

    struct sockaddr_in server_address = {0};
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(port);
    if (inet_pton(AF_INET, argv[1], &server_address.sin_addr) != 1) {
        ERROR("wrong IP address");
    }

    run_transport(server_address, filename, total_size);

    
    return 0;
}
