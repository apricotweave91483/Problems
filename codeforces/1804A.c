#include <stdio.h>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int total = 0;

        int a, b;
        scanf("%d%d", &a, &b);
        if (a < 0) a *= -1;
        if (b < 0) b *= -1;
        int both = (a > b) ? b : a;

        total += both * 2;
        b -= both; a -= both;
        if (a > 0) total += a + a - 1;
        if (b > 0) total += b + b - 1;

        printf("%d\n", total);
    }
}
