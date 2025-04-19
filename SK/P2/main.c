// Maciej Ciepiela, 347677

#include "router.h"

int num_routes = 0;
route routing_table[MAX_ROUTES];

void ERROR(const char* str)
{
    fprintf(stderr, "%s: %s\n", str, strerror(errno));
    exit(EXIT_FAILURE);
}

uint32_t mask_to_bits(int mask) {
    return htonl(~((1 << (32 - mask)) - 1));
}

int main() {
    
    int num_interfaces = 0;
    if(scanf("%d", &num_interfaces) != 1){
        ERROR("scanf error");
    }
    interface interfaces[num_interfaces];
    for(int i = 0; i < num_interfaces; i++) {
        char ip_cidr[32];
        char word[16];
        uint32_t distance;
        int mask;
        if(scanf("%s %s %u", ip_cidr, word, &distance) !=3){
            ERROR("scanf error");
        }

        char* ip_str = strtok(ip_cidr, "/");
        char* mask_str = strtok(NULL, "/");
        mask = atoi(mask_str);
        if (inet_aton(ip_str, &interfaces[i].ip) == 0) {
            ERROR("Invalid IP address");
        }
        uint32_t mask_bits = mask_to_bits(mask);
        
        interfaces[i].net.s_addr = interfaces[i].ip.s_addr & mask_bits;
        interfaces[i].mask = mask;
        interfaces[i].distance = distance;
        update_routing_table(interfaces[i].net, distance, mask, interfaces[i].ip, 1);
    }

    start_router(interfaces, num_interfaces);

    return 0;
}
