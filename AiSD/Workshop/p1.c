#include <stdio.h>
#include <stdlib.h>


struct node {
    int parent;
    int child;
    int last;
    int next;
    int timeIn;
    int timeOut;
};

struct tree {
    struct node nodes[1000001];
};



void addEdge(struct tree* tree, int a, int b) {
    tree->nodes[b].parent = a;
    if(tree->nodes[a].child == 0) {
        tree->nodes[a].child = b;
    }
    else {
        tree->nodes[tree->nodes[a].last].next = b;
    }
    tree->nodes[a].last = b;
}

void dfs2(struct tree* tree, int node, int n) {
    int time = 0;
    while(time < n) {
        if(tree->nodes[node].child != 0) {
            time++;
            int child = tree->nodes[node].child;
            tree->nodes[node].child = 0;
            node = child;
            tree->nodes[node].timeIn = time;
        }
        else if(tree->nodes[node].next != 0) {
            int next = tree->nodes[node].next;
            tree->nodes[node].timeOut = time;
            time++;
            tree->nodes[node].next = 0;
            node = next;
            tree->nodes[node].timeIn = time;
        }
        else if(tree->nodes[node].parent != 0) {
            int parent = tree->nodes[node].parent;
            tree->nodes[node].parent = 0;
            tree->nodes[node].timeOut = time;
            node = parent;
        }
        else {
            tree->nodes[node].timeOut = time;
            break;
        }
    }
//    for(int i = 1; i<=n; i++) {
//        printf("Node: %d, timeIn: %d, timeOut: %d\n", i, tree->nodes[i].timeIn, tree->nodes[i].timeOut);
//    }
}


int main() {
    int n, q, a, b;
    scanf("%d %d", &n, &q);
    struct tree* tree = (struct tree*)malloc(sizeof(struct tree));


    tree->nodes[1] = (struct node){0, 0, 0, 0, 0, 0};
    for(int i = 2; i<=n;i++) {
        tree->nodes[i] = (struct node){0, 0, 0, 0, 0, 0};
        scanf("%d", &a);
        b = i;
        tree->nodes[b].parent = a;
        if(tree->nodes[a].child == 0) {
            tree->nodes[a].child = b;
        }
        else {
            tree->nodes[tree->nodes[a].last].next = b;
        }
        tree->nodes[a].last = b;
    }

//    dfs2(tree, 1, n);
    int node = 1;
    int time = 0;
    while(time < n) {
        if(tree->nodes[node].child != 0) {
            time++;
            int child = tree->nodes[node].child;
            tree->nodes[node].child = 0;
            node = child;
            tree->nodes[node].timeIn = time;
        }
        else if(tree->nodes[node].next != 0) {
            int next = tree->nodes[node].next;
            tree->nodes[node].timeOut = time;
            time++;
            tree->nodes[node].next = 0;
            node = next;
            tree->nodes[node].timeIn = time;
        }
        else if(tree->nodes[node].parent != 0) {
            int parent = tree->nodes[node].parent;
            tree->nodes[node].parent = 0;
            tree->nodes[node].timeOut = time;
            node = parent;
        }
        else {
            tree->nodes[node].timeOut = time;
            break;
        }
    }


    for(int i = 0; i<q; i++){
        scanf("%d%d", &a, &b);
        if (tree->nodes[a].timeIn < tree->nodes[b].timeIn && tree->nodes[a].timeOut >= tree->nodes[b].timeOut){
            printf("TAK\n");
        }
        else{
            printf("NIE\n");
        }
    }

    free(tree);


    return 0;

}
