#include <stdio.h>
#include <math.h>

// Definicja funkcji f(x)
double f(double x) {
    return (double)x - 0.49;
}

double oszacowane(double n, double a, double b){
    return pow(2, -n-1)*(b-a);
}

int main() {
    double a = 0.0;  // Lewa granica przedziału
    double b = 1.0;  // Prawa granica przedziału
    int maxIter = 5; // Liczba kroków

    double m, fm, e, blad;

    for (int i = 0; i <= maxIter; i++) {

        m = (a + b) / 2;
        fm = f(m);
        e = fabs(0.49 - m);
        blad = oszacowane(i, 0, 1);

        printf("Krok %d: a = %lf, b = %lf, m = %lf, f(m) = %lf,\n blad = %lf, oszacowany blad <= %lf\n", i, a, b, m, fm, e, blad);

        if (fm > 0) {
            b = m;
        } else {
            a = m;
        }
    }

    return 0;
}

