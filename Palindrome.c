// Given an integer x, return true if x is palindrome integer.
// An integer is a palindrome when it reads the same backward as forward.


#include <stdbool.h>
#include <stdio.h>

bool isPalindrome(int x) {
    if (x == 0) // 0 is a palindrome
    {
        return true;
    }
    if (x < 0) // negative numbers can not be palindromes
    {
        return false;
    }
    if (x != 0 && x%10 == 0) //if the last number is 0 then the integer can not be a palindrome 
    {
        return false;
    }
    
    long reverse = 0;
    long num = x;
    while (num > 0) {
        reverse = reverse*10 + num%10;
        num /= 10;
    }
    return (reverse == x);
}

int main()
{
    bool result1;
    result1 = isPalindrome(10164);
    printf("%s", result1 ? "result1: true\n" : "result1: false\n");
  
    bool result2;
    result2 = isPalindrome(1001);
    printf("%s", result2 ? "result2: true\n" : "result2: false\n");
    
    
    bool result3;
    result3 = isPalindrome(0);
    printf("%s", result3 ? "result3: true\n" : "result3: false\n");
  
    bool result4;
    result4 = isPalindrome(150);
    printf("%s", result4 ? "result4: true\n" : "result4: false\n");
  
}
