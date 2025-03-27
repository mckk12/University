// Maciej Ciepiela, 347677

#include "traceroute.h"

// funkcja zbierająca dane z wysłania i odebrania pakietów, wypisuje wyniki
void traceroute(int sockfd, struct sockaddr_in recipient) {
    int pid = getpid() & 0xFFFF;
    int reached = 0;

    for (int ttl = 1; ttl <= MAX_TTL && !reached; ttl++) {
        struct timeval send_times[PACKETS_PER_TTL];
        char ip_strs[PACKETS_PER_TTL][INET_ADDRSTRLEN];
        int time_sum = 0;

        if(!send_icmp_requests(sockfd, ttl, recipient, pid, send_times)){
            fprintf(stderr, "Sending error: %s\n", strerror(errno));
            exit(EXIT_FAILURE);
        }
        int responses = receive_icmp_replies(sockfd, pid, ttl, send_times, ip_strs, &time_sum);

        printf("%2d. ", ttl);
        if (responses == 0) {
            printf("*\n");
            continue;
        }
        
        int already = 0;
        for(int i = 0; i < responses; i++) {
            already = 0;
            // petla aby unkiknac powtarzajacych sie adresow
            for(int j = 0; j<i;j++){
                if(strcmp(ip_strs[i],ip_strs[j])==0){
                    already = 1;
                    break;
                }
            }
            if(already) continue;
            printf("%s ", ip_strs[i]);

            //zakonczenie dzialania po osiagnieciu adresu docelowego
            char ip_current[INET_ADDRSTRLEN];
            if(inet_ntop(AF_INET, &(recipient.sin_addr), ip_current, INET_ADDRSTRLEN)==NULL){
                fprintf(stderr, "ip conversion: %s\n", strerror(errno));
                exit(EXIT_FAILURE);
            }
            if (strcmp(ip_strs[i], ip_current) == 0) {
                reached = 1;
            }
        }
        if (responses == PACKETS_PER_TTL)
            printf("%dms\n", time_sum / PACKETS_PER_TTL);
        else
            printf("???\n");
    }
}
