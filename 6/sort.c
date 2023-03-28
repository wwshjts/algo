#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include"hoare_partition.h"
#define MAX_LEN 1000000
void swap(int * a_ptr, int * b_ptr);
void sort(int * a, int l, int r, int algo);
int main(void)
{

    int n;
    int data[MAX_LEN];
    int nums[MAX_LEN];
    FILE *in;
    FILE *out;
    in = fopen("input.txt", "r");
    out = fopen("output.txt", "w");
    fscanf(in,"%d", &n);
    for(int i = 0; i < n; i++)
        fscanf(in, "%d", &data[i]);
    fclose(in);
    for(int i = 0; i < n; i++)
        nums[i] = data[i];
    clock_t start, end;
    for(int i = 0; i < 3; i++){
        start = clock();
        if(i != 2)
            sort(nums, 0, n-1, i);
        else sort_lomuto(&nums[0], &nums[n-1]);
        end = clock();
        for(int j = 0; j < n; j++)
            fprintf(out, "%d ", nums[j]);
        fprintf(out, "\n");
        for(int j = 0; j < n; j++)
            nums[j] = data[j];
        fprintf(out, "%f\n", (double)(end - start) / CLOCKS_PER_SEC);

    }
    fclose(out);
    return 0;
}

void swap(int * a_ptr, int * b_ptr){
    int tmp = *a_ptr;
    *a_ptr = *b_ptr;
    *b_ptr = tmp; 
}

void sort(int * a, int l, int r, int algo){
    if (r - l < 1)
        return;
    int p;
    if (algo == 0)
        p = hoare_partition(a, l, r);
    if (algo == 1) 
        p = lomuto_naive(a, l, r);
    sort(a, l, p - 1, algo);
    sort(a, p + 1, r, algo);

}
void sort_lomuto(int * l, int * r){
    if (r - l < 1)
        return;
    int* p;
    p = lomuto(l, r);
    sort_lomuto(l, p - 1);
    sort_lomuto(p + 1,r);

}
