#include <stdio.h>
#include <math.h>

void bubbleSort(int arr[], int length);

int main(void)
{
    // my array
    int arr[] = {7, 2, 6, 3, 1};

    // find the length of array
    int length = sizeof(arr) / sizeof(arr[0]);

    bubbleSort(arr, length);
    for (int i = 0; i < length; i++)
    {
        printf("arr[%i] = %i\n", i, arr[i]);
    }
}

void bubbleSort(int arr[], int length)
{
    // should I bubble or nah
    int continueSwap = 1;

    while (continueSwap)
    {
        // turn false until a swap occurred
        // if no swap occured then array is sorted
        continueSwap = 0;

        int currentIndex = 0;
        while (currentIndex < length - 1)
        {
            if (arr[currentIndex] > arr[currentIndex + 1])
            {
                // swap two values
                int temp = arr[currentIndex];
                arr[currentIndex] = arr[currentIndex + 1];
                arr[currentIndex + 1] = temp;

                // a swap did occur
                continueSwap = 1;
            }
            currentIndex++;
        }
    }

}
