#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX_LEN 1000000
void swap(int * a_ptr, int * b_ptr);
void sort(int* l, int* r);
int* lomuto(int * l, int * r);
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
    sort(nums, &nums[n - 1]);
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
int* lomuto(int* l, int* r){
    if(*l > *r)
        swap(l, r);
    int pivot = *l; 
    int * pivot_i = l;
    int * i = ++l;
    while((*i < pivot) && (i <= r)) i++;
    for (int * j = i; j <= r; j++){
        int x = *j;
        int smaller = -(x < pivot);
        int delta = smaller & (j - i);
        i[delta] = *i;
        j[-delta] = x;
        i -= smaller;
    }
    swap(pivot_i, --i);
    return i;
}
void sort(int * l, int * r){
    if (r - l < 1)
        return;
    int* p;
    p = lomuto(l, r);
    sort(l, p - 1);
    sort(p + 1,r);

}