// Maciej Ciepiela, 347677

#include "traceroute.h"

// funkcja odbierajaca odpowiedzi na wyslane pakiety echo, mierzy czas i ilość otrzymanych odpowiedzi
int receive_icmp_replies(int sockfd, int pid, int ttl,
                         struct timeval send_times[], char ip_strs[][INET_ADDRSTRLEN],
                         int *time_sum) {
    struct pollfd ps = { .fd = sockfd, .events = POLLIN };
    struct timeval start;
    if(gettimeofday(&start, NULL)){
        fprintf(stderr, "Gettimeofday: %s\n", strerror(errno));
        exit(EXIT_FAILURE);
    }
    int responses = 0;
    
    while (responses < PACKETS_PER_TTL) {
        struct timeval now;
        if(gettimeofday(&now, NULL)){
            fprintf(stderr, "Gettimeofday: %s\n", strerror(errno));
            exit(EXIT_FAILURE);
        }

        // odejmowanie czasu od TIMEOUT zeby rozdzielic czas oczekiwania na kolejne pakiety
        // zamiast sekundy na jeden pakiet jest sekunda na wszystkie pakiety (3)
        int elapsed_ms = (now.tv_sec - start.tv_sec) * 1000 + 
                         (now.tv_usec - start.tv_usec) / 1000;
        int timeout = TIMEOUT - elapsed_ms;
        if (timeout <= 0)
            break;

        int ready = poll(&ps, 1, timeout);
        if (ready < 0) {
            fprintf(stderr, "Poll: %s\n", strerror(errno));
            return EXIT_FAILURE;
        } else if (ready == 0) {
            break;
        }
        if (!(ps.revents == POLLIN)){
            continue;
        }

        
        struct timeval recv_time;
        struct sockaddr_in sender;
        socklen_t sender_len = sizeof(sender);
        u_int8_t buffer[IP_MAXPACKET];
        ssize_t packet_len = recvfrom(sockfd, buffer, IP_MAXPACKET, 0, (struct sockaddr*)&sender, &sender_len);            
        
        if (gettimeofday(&recv_time, NULL)) {
            fprintf(stderr, "Gettimeofday: %s\n", strerror(errno));
            exit(EXIT_FAILURE);
        }

        if (packet_len < 0) {
            fprintf(stderr, "Recvfrom: %s\n", strerror(errno));
            exit(EXIT_FAILURE);
        }

        struct ip* ip_header = (struct ip*) buffer;
        ssize_t ip_header_len = ip_header->ip_hl * 4; //razy 4 zeby uzyskac dlugosc w bajtach
        struct icmp* icmp_header = (struct icmp*)(buffer + ip_header_len); //przesuwamy wskaznik na naglowek icmp

        // porownanie id i seq z pakietem wyslanym i zapisanie czasu w przypadku zgodnosci
        // Echo reply
        if (icmp_header->icmp_type == ICMP_ECHOREPLY &&
            icmp_header->icmp_hun.ih_idseq.icd_id == pid) {
            int seq = icmp_header->icmp_hun.ih_idseq.icd_seq;
            if ((seq / PACKETS_PER_TTL) == ttl) {
                int idx = seq % PACKETS_PER_TTL;
                    *time_sum += (recv_time.tv_sec - send_times[idx].tv_sec) * 1000 +
                               (recv_time.tv_usec - send_times[idx].tv_usec) / 1000;
                    if(inet_ntop(AF_INET, &(sender.sin_addr), ip_strs[idx], sizeof(ip_strs[idx]))==NULL){
                        fprintf(stderr, "ip conversion: %s\n", strerror(errno));
                        exit(EXIT_FAILURE);
                    }
                    ++responses;
                
            }
        }

        // Time exceeded
        else if (icmp_header->icmp_type == ICMP_TIME_EXCEEDED) {
            u_int8_t *inner_ip = buffer + ip_header_len + 8; //przesuwamy wskaznik o naglowek oryginalnego IP i 8 bajtow pakietu
            struct ip* orig_ip = (struct ip*) inner_ip;
            ssize_t inner_ip_header_len = orig_ip->ip_hl * 4;
            struct icmp* orig_icmp = (struct icmp*)(inner_ip + inner_ip_header_len);

            if (orig_icmp->icmp_hun.ih_idseq.icd_id == pid) {
                int seq = orig_icmp->icmp_hun.ih_idseq.icd_seq;
                if ((seq / PACKETS_PER_TTL) == ttl) {
                    int idx = seq % PACKETS_PER_TTL;
                        *time_sum += (recv_time.tv_sec - send_times[idx].tv_sec) * 1000 +
                                   (recv_time.tv_usec - send_times[idx].tv_usec) / 1000;
                        if(inet_ntop(AF_INET, &(sender.sin_addr), ip_strs[idx], sizeof(ip_strs[idx]))==NULL){
                            fprintf(stderr, "ip conversion: %s\n", strerror(errno));
                            exit(EXIT_FAILURE);
                        }
                        ++responses;
                    
                }
            }
        }
    }

    return responses;
}

