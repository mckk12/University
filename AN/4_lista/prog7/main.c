#include <stdio.h>
#include <math.h>

double a = 1.0; // Przykładowa wartość a
int maxIterations = 10; // Maksymalna liczba iteracji

double f(double x) {
    return x * x - a;
}

double df(double x) {
    return 2 * x;
}


int main() {
    double x0 = (double)2/3;
    double x = x0;
    printf("%lf\n", x);
    for(int i = 0; i<maxIterations; i++){
        x = x - f(x) / df(x);
        printf("%.15lf\n", x);
    }

    return 0;
}
