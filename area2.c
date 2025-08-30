#include <stdio.h>
int main(){
    float area,radius,height;
    printf("Enter the value of radius:");
    scanf("%f" , &radius);
    printf("Enter the value of height:");
    scanf("%f" , &height);
    area = (3.14*radius*(height+radius))/3;
    printf("The area of cylinder is: %.02f", area);
    return 0;






}