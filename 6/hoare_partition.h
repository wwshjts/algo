int hoare_partition(int * a, int l, int r);

int hoare_partition(int * a, int l, int r){
    int pivot;
   // int pivot_1 =  l + rand() % (r + 1  - l);
   // int pivot_2 =  l + rand() % (pivot_1 - l);
   // int pivot_i = pivot_1 ? a[pivot_1] <= a[pivot_2] : pivot_2;
    int pivot_i = (int) ((l + r) / 2);
    //swap(&l, &pivot_i);
    //pivot_i = l;
    pivot = a[pivot_i];
    //l++;
    while (l <= r){
        while (a[l] < pivot)
            l++;
        while (a[r] > pivot)
            r--;
        if (l >= r)
            break;
        swap(&a[l++], &a[r--]);
    }
    //if (a[l] > pivot)
    //  l--;
    //swap(&a[l], &a[pivot_i]);
    return r;
}