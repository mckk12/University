#include <stdio.h>

typedef struct{
    int value;
    int weight;
}coin;

int main() {
    int f, c;
    scanf("%d", &f);
    scanf("%d", &c);
    coin coins[c];
    int v, w;
    for (int i = 0; i < c; i++) {
        scanf("%d %d", &v, &w);
        coin newCoin = {v, w};
        coins[i] = newCoin;
    }
    int dp[f + 1][4]; //min, min coin, max, max coin
    for(int i = 0; i <= f; i++){
        for(int j = 0; j < 4; j++){
            dp[i][j] = 0;
        }
    }
    for(int i = 0; i<=f; i++){
        for(int j = 0; j<c; j++){
            if(coins[j].weight <= i){
                //if weight is different and there was no max without this coin
                if(coins[j].weight != i && dp[i-coins[j].weight][2] == 0){
                    continue;
                }
                if(dp[i][2] < dp[i-coins[j].weight][2] + coins[j].value){
                    dp[i][2] = dp[i-coins[j].weight][2] + coins[j].value;
                    dp[i][3] = j;
                }
                if((dp[i][0] > dp[i-coins[j].weight][0] + coins[j].value) || dp[i][0] == 0){
                    dp[i][0] = dp[i-coins[j].weight][0] + coins[j].value;
//                    printf("dp[%d][0] = %d\n", i, dp[i][0]);
                    dp[i][1] = j;
                }
            }
        }
    }
    if(dp[f][0] != 0){
        printf("TAK\n");
        printf("%d\n", dp[f][0]);
        int temp = f;
        int minCoins[c];
        int maxCoins[c];
        for(int i = 0; i < c; i++){
            minCoins[i] = 0;
            maxCoins[i] = 0;
        }
        while(temp > 0){
            minCoins[dp[temp][1]]++;
            temp -= coins[dp[temp][1]].weight;
        }
        for(int i = 0; i < c; i++){
            printf("%d ", minCoins[i]);
        }
        printf("\n");
        printf("%d\n", dp[f][2]);
        temp = f;
        while(temp > 0){
            maxCoins[dp[temp][3]]++;
            temp -= coins[dp[temp][3]].weight;
        }
        for(int i = 0; i < c; i++){
            printf("%d ", maxCoins[i]);
        }
        printf("\n");
    }
    else{
        printf("NIE\n");
    }

    return 0;
}
