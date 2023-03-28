#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX_LEN 1000000
void swap(int * a_ptr, int * b_ptr);
void sort(int * a, int l, int r);
int hoare_partition(int * a, int l, int r);
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
    start = clock();
    sort(nums, 0, n - 1);
    end = clock();
    fprintf(out, "%f\n", (double)(end - start) / CLOCKS_PER_SEC);
    for(int j = 0; j < n; j++)
        fprintf(out, "%d ", nums[j]);
    fclose(out);
    return 0;
}

void swap(int * a_ptr, int * b_ptr){
    int tmp = *a_ptr;
    *a_ptr = *b_ptr;
    *b_ptr = tmp; 
}

void sort(int * a, int l, int r){
    if (r - l < 1)
        return;
    int p;
    p = hoare_partition(a, l, r);
    sort(a, l, p - 1);
    sort(a, p + 1, r);

}

int hoare_partition(int * a, int l, int r){
    int pivot_1 = r;
    int pivot_2 = l;
    int pivot_i = a[pivot_1] <= a[pivot_2] ? pivot_1 : pivot_2;
    int pivot = a[pivot_i];
    swap(&a[l], &a[pivot_i]);
    pivot_i = l;
    l++;
    while (l <= r){
        while (a[l] < pivot)
            l++;
        while (a[r] > pivot)
            r--;
        if (l >= r)
            break;
        swap(&a[l++], &a[r--]);
    }
    if (a[l] > pivot)
        l--;
    swap(&a[l], &a[pivot_i]);
    return l;
}