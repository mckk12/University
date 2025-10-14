#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct{
    int x, y;
}Point;

Point result[3];
double minDist = INFINITY;

Point middlePoint(Point p1, Point p2) {
    Point p = {(p1.x + p2.x) / 2, (p1.y + p2.y) / 2};
    return p;
}

double distance(Point p1, Point p2) {
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

double perimeter(Point p1, Point p2, Point p3) {
    return distance(p1, p2) + distance(p2, p3) + distance(p3, p1);
}
int compareX(const void* a, const void* b)
{
    Point *p1 = (Point *)a,  *p2 = (Point *)b;
    return (p1->x - p2->x);
}
int compareY(const void* a, const void* b)
{
    Point *p1 = (Point *)a,   *p2 = (Point *)b;
    return (p1->y - p2->y);
}

void brute(int n, Point points[]) {
    if (n < 3) {
        return;
    }
    for (int a = 0; a < n; a++) {
        for (int b = a + 1; b < n; b++) {
            for (int c = b + 1; c < n; c++) {
                double l = perimeter(points[a], points[b], points[c]);
                if (l < minDist) {
                    result[0] = points[a];
                    result[1] = points[b];
                    result[2] = points[c];
                    minDist = l;
                }
            }
        }
    }
}
void solve(int n, Point points[]) {
    if (n < 3) {
        return;
    }
    int l = n / 2;
    int r = n - l;
    Point left[l];
    Point right[r];

    Point midX = middlePoint(points[l], points[l+1]);
    for(int i = 0; i < l; i++) {
        left[i] = points[i];
    }
    for(int i = 0; i < r; i++) {
        right[i] = points[i + l];
    }
    solve(l, left);
    solve(r, right);
    double dist = perimeter(result[0], result[1], result[2]);
    if (dist < minDist) {
        minDist = dist;
    }
    double rangeToCheck = minDist / 2;

    //wybranie punktow w poblizu po X
    Point strip[n];
    int size = 0;
    for (int i = 0; i < n; i++) {
        if (abs(points[i].x - midX.x) <= rangeToCheck) {
            strip[size] = points[i];
            size++;
        }
    }
    qsort(strip, size, sizeof(Point), compareY);

    //wybranie po odleglosci miedzy Y
    for(int i = 0; i < size; i++) {
        Point near[size];
        int k = 0;
        near[k] = strip[i];
        k++;
        int help = i+1;
        while(help < size && strip[help].y - strip[i].y <= rangeToCheck) {
            near[k] = strip[help];
            k++;
            help++;
        }
        brute(k, near);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    Point points[n];
    int x,y;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x, &y);
        Point p = {x, y};
        points[i] = p;
    }

    qsort(points, n, sizeof(Point), compareX);

    result[0] = points[0];
    result[1] = points[1];
    result[2] = points[2];

    solve(n, points);
    qsort(result, 3, sizeof(Point), compareX);
    printf("%d %d\n%d %d\n%d %d\n", result[0].x, result[0].y, result[1].x, result[1].y, result[2].x, result[2].y);

    return 0;
}