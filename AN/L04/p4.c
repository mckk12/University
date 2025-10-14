#include <stdio.h>
#include <math.h>

// Definicja funkcji f(x)
double f(double x) {
    return (double) pow(x, 4) - log(x+4);
}

double oszacowane(double n, double a, double b){
    return pow(2, -n-1)*(b-a);
}

int main() {
    double a = -2.0;  // Lewa granica przedziału
    double b = -1.0;  // Prawa granica przedziału
    int maxIter = 26; // Liczba kroków

    double m, fm, blad;
    double a0 = a;  // Lewa granica przedziału
    double b0 = b;
    for (int i = 1; i <= maxIter; i++) {

        m = (a + b) / 2;
        fm = f(m);
        blad = oszacowane(i, a0, b0);

        printf("Krok %d: a = %.9lf, b = %.9lf, m = %.9lf, f(m) = %.9lf,   oszacowany blad <= %.9lf\n", i, a, b, m, fm, blad);


        if (fm > 0) {
            a = m;
        } else {
            b = m;
        }
    }


    return 0;
}

