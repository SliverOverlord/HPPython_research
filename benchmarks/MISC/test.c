#include <stdio.h>
#include <stdlib.h>

int main()
{
    
    int *num;
    int arr[5] = {1, 2, 3, 4, 5};

    num = (int *) malloc(sizeof(int) * 5);

    num = arr;
    printf("%d\n", num[2]);

    return 0;
}
