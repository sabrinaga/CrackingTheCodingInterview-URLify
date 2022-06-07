// Function to fiind the roots of the quadratic equation

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void find_roots(double a, double b, double c, double *root1, double *root2)
{
  double discriminant = b * b - 4 * a * c;
  
    if (discriminant > 0) 
    {
        *root1 = (-b + sqrt(discriminant)) / (2 * a);
        *root2 = (-b - sqrt(discriminant)) / (2 * a);
    }
  
    else if (discriminant == 0) 
    {
        *root1 = *root2 = -b / (2 * a);
    }
    
}


int main()
{
    double root1, root2;
    find_roots(2, 10, 8, &root1, &root2);
    printf("Roots: %f, %f\n", root1, root2);
  
  double root3, root4;
    find_roots(1, 2, 1, &root3, &root4);
    printf("Roots: %f, %f\n", root3, root4);
}
