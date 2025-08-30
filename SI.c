#include <stdio.h>
int main(){
    printf("***WELCOME TO INTERET CALCULATOR***\n");
    float principal , rate , time , si;
    printf("Enter the Principle amount: ");
    scanf("%f" , &principal);
    printf("Enter the Rate of interest: ");
    scanf("%f" , &rate);
    printf("Enter the Time period:");
    scanf("%f" , &time);
    si = (principal*rate*time)/100;
    printf("Total interest rate is: %.02f " , si);
    return 0;

}