#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE * fptr;
    char * line = NULL;
    size_t len = 0;
    size_t read;

    fptr = fopen("input.txt", "r");
    if (fptr == NULL)
        exit(EXIT_FAILURE);

    int sections[] = malloc(sizeof(int)); 

    while ((read = getline(&line, &len, fptr)) != -1) {
        
    }

    fclose(fptr);
    if (line)
        free(line);

    return 0;
}