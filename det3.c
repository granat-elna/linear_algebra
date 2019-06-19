#include <stdio.h>
#include <stdlib.h>
#define NTH 3

extern void det3(double **);                        // 3次正方行列の行列式を返す
extern double det2(double, double, double, double); // 2次正方行列の行列式を返す
extern void display_mat(double **);

void det3(double **x)
{
  int i;
  double d = 0;
  for (i = 0; i < 3; i++)
  {
    d += x[0][i] * det2(
      x[1][(i + 1) % NTH],
      x[1][(i + 2) % NTH],
      x[2][(i + 1) % NTH],
      x[2][(i + 2) % NTH]);
  }
  printf("Determinant: %.4lf\n", d);
}

double det2(double x11, double x12, double x21, double x22)
{
  return x11 * x22 - x12 * x21;
}

void display_mat(double **x)
{
  int i, j;
  printf("[\n");
  for(i = 0; i < NTH; i++)
  {
    printf(" [");
    for(j = 0; j < NTH; j++)
    {
      printf(" %.4lf.", x[i][j]);
    }
    printf("]\n");
  }
  printf("]\n");
}

int main(void)
{
  int i, j;
  double **x = malloc(sizeof(double *) * NTH);
  for (i = 0; i < NTH; i++)
  {
    x[i] = malloc(sizeof(double) * NTH);
    for (j = 0; j < NTH; j++)
    {
      printf("X[%d][%d] >>> ", i+1, j+1);
      scanf("%lf", &x[i][j]);
    }
  }
  display_mat(x);
  det3(x);
  return (EXIT_SUCCESS);
}