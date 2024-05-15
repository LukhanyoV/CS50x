#include <stdio.h>
#include <math.h>

int binarySearch(int arr[], int length, int el);

int main(void)
{
    // my array
    int arr[] = {2, 3, 4, 6, 7};

    // find the length of array
    int length = sizeof(arr) / sizeof(arr[0]);

    // search element
    int el = 2;

    int results = binarySearch(arr, length, el);
    printf("Index: %i\n", results);
}

int binarySearch(int arr[], int length, int el)
{
    // set the start
    int start = 0;
    // set the end
    int end = length - 1;
    // get the middle element
    int mid = (end + start) / 2;

    // find the number
    while (start <= end)
    {
        // if mid element is target
        if (el == arr[mid])
        {
            return mid;
        }
        // if target is bigger than middle number
        else if (el > arr[mid])
        {
            start = mid + 1;
            mid = (end + start) / 2;
        }
        // if the target is less than middle number
        else if (el < arr[mid])
        {
            end = mid - 1;
            mid = (end + start) / 2;
        }
        // sub array of 0 elements
        else if (start > end)
        {
            return -1;
        }
    }

    // return -1 if the element was not found
    return -1;
}
