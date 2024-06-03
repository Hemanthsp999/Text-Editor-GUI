#include <stdio.h>

int main() {
  int a = 10;
  int b = 20;
  printf("Before Swaping %d and %d\n ", a, b);

  int temp = a;
  a = b;
  b = temp;

  printf("After Swaping %d and %d\n", a, b);

  return 0;
}

