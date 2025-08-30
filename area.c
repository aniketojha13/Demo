#include <stdio.h>

int main() {
    int base , height;
    float radius,area;

    // Input base and height from the user
    printf("Enter the radius of circle: ");
    scanf("%f", &radius);
    int a = (22*(radius*radius))/49;

    printf("The area of Circle %.02f\n", a );

    printf("Enter the height of the triangle: ");
    scanf("%d", &height);

    // Calculate the area
    area = 3.14*radius*radius;

    // Output the area
    printf("The area of the circle is: %.02f\n", area);

    return 0;
}