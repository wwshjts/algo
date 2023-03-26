
int hoare_partition(int * a, int l, int r){
    int pivot;
    int pivot_1 = (l + 1) + (rand() % (r - l));
    int pivot_2 =  l + ((rand()) % (l - pivot_1));
    int pivot_i = a[pivot_1] <= a[pivot_2] ? pivot_1 : pivot_2;
    pivot = a[pivot_i];
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