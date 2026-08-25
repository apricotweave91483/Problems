#include <stdio.h>
#include <stdlib.h>

int icmp(const void *a, const void *b) {
    const int lhs = *(const int *)a;
    const int rhs = *(const int *)b;
    return (lhs > rhs) - (lhs < rhs);
}

int in(int* arr, int* tar_poi, int len) {
    return (bsearch(tar_poi, arr, len, sizeof(int), icmp) == NULL) ? 0 : 1;
}

int solve(int* nums, int t, int k) {
    qsort(nums, t, sizeof(int), icmp);
    int* tar = malloc(sizeof(int)); *tar = k;

    int curr = 1;

    while (1) {
        *tar *= curr;
        if (*tar > 100) break;

        if (!(in(nums, tar, t)))
            return *tar;
        else {
            *tar /= curr;
            curr += 1;
        }
    }

    return *tar;
}

int main() {
    int t; scanf("%d", &t);
    int arr[t]; for (int i = 0; i < t; ++i) scanf("%d", arr + i);

    int k; scanf("%d", &k);

    printf("%d\n", solve(arr, t, k));

}
