#include <stdio.h>

int main() {
    int age = 25;         // Assigning an integer
    float price = 19.99;  // Assigning a float
    char grade = 'n';     // Assigning a character

    //You can also assign after declaration
    int number;
    number = 10;

    printf("Age: %d\n", age);
    printf("Price: %.2f\n", price);
    printf("Grade: %c\n", grade);
    printf("Number: %d\n", number);

    return 0;
}
