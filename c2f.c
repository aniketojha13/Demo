#include <stdio.h>
int main(){
    float celcius , fahrenheit ;
    printf("Enter the Celcius Temperature: ");
    scanf("%f" , &celcius);
    fahrenheit = (celcius*9/5)+32;
    printf("Temperature in fahrenheit is: %.02f" , fahrenheit);
    return 0;
}