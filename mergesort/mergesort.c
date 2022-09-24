#include <cs50.h>
#include <stdio.h>

void merge(int arr[], int l, int m, int r);
void mergeSort(int arr[], int l, int r);
void printArray(int arr[], int len);

//testing sorting
int main()
{
    //test array
    int A[] = { 12, 11, 13, 5, 6, 7 };
    int arr_len = sizeof(A) / sizeof(A[0]);

    printf("Given array is \n");
    printArray(A, arr_len);

    mergeSort(A, 0, arr_len - 1);

    printf("\nSorted array is \n");
    printArray(A, arr_len);
    return 0;
}

void merge(int arr[], int l, int m, int r)
{
    // Creates variables with the length of each half of the original array
    // add 1 to the lenght of left array because we have to account
    // for the middle element of the array (this could also be done in the other side)
    int lenL = m - l + 1;
    int lenR = r - m;

    // Creates two temporary arrays to hold the values of the left and right arrays
    // First/Left subarray is arr[l..m]
    // Second/Right subarray is arr[m+1..r]
    int L[lenL], R[lenR];

    for (int i = 0; i < lenL; i++)
    {
        L[i] = arr[l + i];
    }
    for (int j = 0; j < lenR; j++)
    {
        R[j] = arr[m + 1 + j];
    }

    // This variables are used to store the indexes while merging the two sides of the array
    // i -> current index on the left side array
    // j -> current index on the right side array
    // k -> current index on the merged array
    int i = 0, j = 0, k = l;

    // While loop that lasts until we reach the end of one of the subarrays
    // in every iteration we compare the current values of each subarray
    // the smallest goes to the main array
    while (i < lenL && j < lenR)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            k++;
            i++;
        }
        else
        {
            arr[k] = R[j];
            k++;
            j++;
        }

    }

    // After we reach the end of one of the subarray we need to
    // put the rest of the values of the subarray that is still left
    // in the main array
    // Only one of this loops is ran
    while (i < lenL)
    {
        arr[k] = L[i];
        k++;
        i++;
    }

    while (j < lenR)
    {
        arr[k] = R[j];
        k++;
        j++;
    }
    return;

}

void mergeSort(int arr[], int l, int r)
{
    // This checks if array is just one value
    if (l < r)
    {
        int m = l + (r - l) / 2; // mesma coisa que (l + r)/2
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
    return;
}

void printArray(int arr[], int len)
{
    int i;
    for (i = 0; i < len; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return;
}
