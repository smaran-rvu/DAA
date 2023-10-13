#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int m1, m2, n1, n2, i, j;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    scanf("%d%d",&m1,&m2);
    int m[m1][m2];
    for(i=0;i<m1;i++)
    {
        for(j=0;j<m2;j++)
        {
            scanf("%d",&m[i][j]);
        }
    }
    scanf("%d%d",&n1,&n2);
    int n[n1][n2];
    for(i=0;i<n1;i++)
    {
        for(j=0;j<n2;j++)
        {
            scanf("%d",&n[i][j]);
        }
    }
    if(m2!=n1)
    {   
        printf("-1");
        return 0;
    }
    int res[m1][n2], add=0, mult=0, k, sum=0;
    //--------------------------------------------------------
    for(i=0;i<m1;i++)
    {
        for(j=0;j<n2;j++)
        {   
            for(k=0;k<n1;k++)
            {
                sum+=m[i][k]*n[k][j];
                mult++;
            }
            res[i][j]=sum;
            add++;
            sum=0;
        }
    }
    //----------------------------------------------------------
    for(i=0;i<m1;i++)
    {
        for(j=0;j<n2;j++)
        {
            printf("%d ",res[i][j]);
        }
        printf("\n");
    }
    printf("%d ",mult);
    printf("%d",mult-add);
}