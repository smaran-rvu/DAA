# include <stdio.h>

int r;
static int unin = 23;

int a(int n)
{
    if (n>0)
    {
        a(n-1);
        printf("%d",n);
        a(n-1);
    }
}

int main()
{
    int i = 23;
    scanf("%d", &i);
    a(i);
    // printf("hi");
}