#include <stdio.h>
#include<math.h>
int main(){
    printf("***WELCOME TO  COMPOUND INTERET CALCULATOR***\n");
    float principal , rate , time , interest , ir,ci;
    printf("Enter the Principle amount: ");
    scanf("%f" , &principal);
    printf("Enter the Rate of interest: ");
    scanf("%f" , &rate);
    printf("Enter the Time period:");
    scanf("%f" , &time);
    interest = (1+rate/100);
    ir = pow(interest,time);
    ci = principal*ir;
    printf("Total interest rate is: %.02f " , ci);
    return 0;

}