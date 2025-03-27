// Maciej Ciepiela, 347677

#include "traceroute.h"

// funkcja z wykładu, obliczanie sumy kontrolnej nagłówka ICMP
u_int16_t compute_icmp_checksum(const void *buff, int length) {
    u_int32_t sum = 0;
    const u_int16_t* ptr = buff;
    assert(length % 2 == 0);
    for (; length > 0; length -= 2) {
        sum += *ptr++;
    }
    sum = (sum >> 16U) + (sum & 0xffffU);
    return ~(sum + (sum >> 16U));
}


// funkcja wysyłająca pakiety ICMP ECHO_REQUEST
int send_icmp_requests(int sockfd, int ttl, struct sockaddr_in recipient, int pid, struct timeval send_times[]) {
    
    if(setsockopt(sockfd, IPPROTO_IP, IP_TTL, &ttl, sizeof(ttl))){
        return 0;
    };

    for (int i = 0; i < PACKETS_PER_TTL; i++) {
        // generowanie struktury pakietu
        struct icmp packet;
        packet.icmp_type = ICMP_ECHO;
        packet.icmp_code = 0;
        packet.icmp_hun.ih_idseq.icd_id = pid;
        packet.icmp_hun.ih_idseq.icd_seq = ttl * PACKETS_PER_TTL + i;
        packet.icmp_cksum = 0;
        packet.icmp_cksum = compute_icmp_checksum(&packet, sizeof(packet));

        // zapis czasu wysłania pakietu
        if(gettimeofday(&send_times[i], NULL)){
            return 0;
        }

        // error w przypadku niepowodzenia w wysyłaniu
        if (sendto(sockfd, &packet, sizeof(packet), 0, (struct sockaddr *)&recipient, sizeof(recipient)) < 0) {
            return 0;
        }
    }
    return 1;
}
