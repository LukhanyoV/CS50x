#include <stdio.h>

int linearSearch(int arr[], int el);

int main(void)
{
    // my array
    int arr[5] = {2,3,4,6,7};

    // search element
    int el = 4;

    printf("Index: %i\n", linearSearch(arr, el));
}

int linearSearch(int arr[], int el)
{
    // get the length of the array
    // int size = sizeof(arr) / sizeof(arr[0]);
    int size = 5;

    // loop through the array
    // and return the index of the found element
    for (int i = 0; i < size; i++) if (arr[i] == el) return i;

    // return -1 if the element was not found
    return -1;
}
