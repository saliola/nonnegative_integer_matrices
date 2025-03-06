#include <stdio.h>
#include <stdlib.h>

// print an array
void printArray(int* array, int length) {
    printf("[");
    for (int i = 0; i < length; i++) {
        if (i == length - 1) {
            printf("%d", array[i]);
        } else {
            printf("%d, ", array[i]);
        }
    }
    printf("]");
    printf("\n");
}


// copy an array
int* copyArray(int* array, int length) {
    int* newArray = (int*) malloc(length * sizeof(int));

    // check if memory allocation was successful
    if (newArray == NULL) {
        printf("Memory allocation failed\n");
        return NULL;
    }

    // copy contents of the original array to the new array
    for (int i = 0; i < length; i++) {
        newArray[i] = array[i];
    }

    return newArray;
}


// create an array of ints of the given length initialized with 0s
int* createArray(int length) {
    int* array = (int*) calloc(length, sizeof(int));

    // check if memory allocation was successful
    if (array == NULL) {
        printf("Memory allocation failed\n");
        return NULL;
    }

    return array;
}


void generate_nonneg_int_vectors(int* composition, int length, int index, int sum, int n, int* maxValues) {
    // given a composition of length `length` whose parts sum to `sum`, and
    // with nonzero parts in positions 0, 1, ..., index - 1,
    // generate all compositions obtained by modifying the element in position `index`
    // subject to the constraints that the total sum is at most `n`,
    // and that the new part is bounded by maxValues[index].

    if (index == length - 1) {
        if (n - sum <= maxValues[index]) {
            composition[index] = n - sum;
            // printArray(composition, length);
        }
        free(composition);
        return;
    } else {
        int maxValue;
        if (n - sum <= maxValues[index]) {
            maxValue = n - sum;
        } else {
            maxValue = maxValues[index];
        }

        for (int i = 0; i <= maxValue; i++) {
            int* newComposition = copyArray(composition, length);
            newComposition[index] = i;
            generate_nonneg_int_vectors(newComposition, length, index + 1, sum + i, n, maxValues);
        }
    }
}

int main () {

    int n = 4;
    int length = n;
    int* composition = createArray(length);
    int sum = 0;
    int index = 0;
    int* maxValues = createArray(length);
    for (int i = 0; i < length; i++) {
        maxValues[i] = n;
    }
    generate_nonneg_int_vectors(composition, length, sum, index, n, maxValues);

    return 0;
}
