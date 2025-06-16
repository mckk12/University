// Maciej Ciepiela, 347677

#include "transport.h"

void print_progress(int received, int packets_to_send) {
    float progress = (float)received * 100.0 / (float)packets_to_send;
    printf("%.3f%% done\n", progress);
    fflush(stdout);
}

void run_transport(struct sockaddr_in server_address, const char* filename, int total_size) {
    FILE *file = fopen(filename, "wb");
    if (!file) {ERROR("fopen");}

    int sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {ERROR("socket");}    

    int lfr = -1;
    int packets_to_send = (total_size % PACKET_SIZE == 0) ? total_size / PACKET_SIZE : total_size / PACKET_SIZE + 1;
    int packet_receive[packets_to_send];
    for (int i = 0; i < packets_to_send; i++) {
        packet_receive[i] = 0;
    }
    PacketsData data[WINDOW_SIZE];

    struct timeval start_time, curr_time;

    while(lfr + 1 < packets_to_send) {

        // wyslanie pakietow bedacych w oknie
        int window = (WINDOW_SIZE > packets_to_send - lfr - 1) ? packets_to_send - lfr - 1 : WINDOW_SIZE;
        for(int i = 0; i<2; i++){
            if (send_requests(sockfd, &server_address, window, lfr, total_size, packet_receive) < 0) {
                ERROR("send_requests");
            }
        }

        int curr_recv = 0;
        int elapsed_time = 0;
        for (int i = lfr + 1; i < lfr + 1 + window; i++) {
            if (packet_receive[i]) {
                curr_recv++;
            }
        }
        // czekanie na odebranie pakietow z okna
        if (gettimeofday(&start_time, NULL) < 0) {
            ERROR("gettimeofday");
        }
        while (elapsed_time < TIMEOUT_MS) {
            curr_recv += receive_response(sockfd, &server_address, data, packet_receive, packets_to_send, lfr);

            if(curr_recv == window){
                curr_recv = 0;
                break;
            }

            if (gettimeofday(&curr_time, NULL) < 0) {
                ERROR("gettimeofday");
            }
            elapsed_time = (curr_time.tv_sec - start_time.tv_sec) * 1000 + (curr_time.tv_usec - start_time.tv_usec) / 1000;

        }

        //przesuniecie poczatku okna
        int wrote_count = 0;
        while (lfr + 1 < packets_to_send && packet_receive[lfr + 1]) {
            lfr++;
            long unsigned int length = (lfr == packets_to_send - 1 && total_size % PACKET_SIZE != 0) ? (total_size % PACKET_SIZE) : PACKET_SIZE;

            if (fwrite(data[wrote_count].received_data, 1, length, file) != length) {
                ERROR("fwrite");
            }
            wrote_count++;
        }
        for (int i = wrote_count; i < WINDOW_SIZE; i++) {
            data[i - wrote_count] = data[i];
        }

        print_progress(lfr + 1, packets_to_send);
    
    }


    if(fclose(file)){ERROR("close");}
    if(close(sockfd)){ERROR("close");}
}
