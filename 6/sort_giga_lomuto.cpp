#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include <algorithm>   
#include <cassert>
#define MAX_LEN 500000
using std::swap;
void sort(long* l, long* r);
long* lomuto(long * l, long * r);
int main(void)
{

    long n;
    long data[MAX_LEN];
    long nums[MAX_LEN];
    FILE *in;
    FILE *out;
    in = fopen("input.txt", "r");
    out = fopen("output.txt", "w");
    fscanf(in,"%ld", &n);
    for(long i = 0; i < n; i++)
        fscanf(in, "%ld", &data[i]);
    fclose(in);
    for(long i = 0; i < n; i++)
        nums[i] = data[i];
    clock_t start, end;
    start = clock();
    lomuto(nums, &nums[n - 1]);
    end = clock();
    fprintf(out, "%f\n", (double)(end - start) / CLOCKS_PER_SEC);
    for(long j = 0; j < n; j++)
        fprintf(out, "%d ", nums[j]);
    fclose(out);
    return 0;
}


long* lomuto(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first; // nothing interesting to do
    // Choose pivot.
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *first;
    printf("%ld\n", pivot);
    // Prelude.
    do {
        ++first;
        assert(first <= last);
    } while (*first < pivot);
    // Main loop.
    for (auto read = first + 1; read < last; ++read) {
        auto x = *read;
        auto less = -int(x < pivot);
        auto delta = less & (read - first);
        first[delta] = *first;
        read[-delta] = x;
        first -= less;
    }
    // Move the pivot to its final slot.
    assert(*first >= pivot);
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}
void sort(long * l, long * r){
    if (r - l < 1){
        return;
    }
    long* p;
    p = lomuto(l, r);
    sort(l, p - 1);
    sort(p + 1,r);
}