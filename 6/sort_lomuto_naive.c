#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX_LEN 1000000
void swap(int * a_ptr, int * b_ptr);
void sort(int * a, int l, int r);
int lomuto_naive(int * a, int l, int r);
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
    p = lomuto_naive(a, l, r);
    sort(a, l, p - 1);
    sort(a, p + 1, r);

}
int lomuto_naive(int * a, int l, int r){
    if (a[l] <= a[r])
        swap(&a[l], &a[r]); 
    int pivot_i = l;
    int pivot = a[l];
    l++;
    int i = l;
    for(int j = l; j <= r; j++){
        if (a[j] < pivot){
            swap(&a[i++], &a[j]);
        }
    }
    
    swap(&a[pivot_i], &a[--i]);
    return i;
}