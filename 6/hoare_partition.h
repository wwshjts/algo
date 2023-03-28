int hoare_partition(int * a, int l, int r);
int lomuto_naive(int * a, int l, int r);
int* lomuto(int * l, int * r);

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
int lomuto_naive(int * a, int l, int r){
    if (a[l] <= a[r])
        swap(&a[l], &a[r]); 
    int pivot_i = l;
    pivot = a[l];
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