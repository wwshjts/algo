#include<stdio.h>
#include<stdlib.h>
#include"hoare_partition.h"
#define MAX_LEN 5000
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
    sort(nums, 0, n-1, 0);
    for(int i = 0; i < n; i++)
        fprintf(out,"%d ", nums[i]);
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
    int p = hoare_partition(a, l, r);
    sort(a, l, p, 0);
    sort(a, p + 1, r, 0);

}
