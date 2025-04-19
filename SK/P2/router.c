// Maciej Ciepiela, 347677

#include "router.h"

void show_routing_table(){
    for(int i = 0; i<num_routes;i++){
        printf("%s/%d ", inet_ntoa(routing_table[i].net), routing_table[i].mask);
        if (routing_table[i].unreachable){
            printf("unreachable ");
        }
        else{
            printf("distance %d ", routing_table[i].distance);
        }
        if(routing_table[i].directly){
            printf("connected directly\n");
        }
        else{
            printf("via %s\n", inet_ntoa(routing_table[i].via));
        }
    }    
    printf("\n");
}

void start_router(interface* interfaces, int num_interfaces){
    // open socket
    int sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        ERROR("socket error");
    }

    // bind socket to port
    struct sockaddr_in server_address;
    memset(&server_address, 0, sizeof(server_address));
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = htonl(INADDR_ANY);
    if (bind(sockfd, (struct sockaddr *)&server_address, sizeof(server_address)) < 0) {
        ERROR("bind error");
    }

    // set broadcast option
    int broadcast = 1;
    if (setsockopt(sockfd, SOL_SOCKET, SO_BROADCAST, (void *)&broadcast, sizeof(broadcast)) < 0) {
        ERROR("setsockopt error");
    }
    
    //router loop
    while(1){
        send_distance_vector(sockfd, interfaces, num_interfaces);
        receive_distance_vector(sockfd, num_interfaces, interfaces);
        show_routing_table();
        sleep(TURA_TIME);
    }

    if(close(sockfd)){
        ERROR("socket close error");
    }
    
}