#include<stdio.h>
void main()
{
    int num[20];
    int key,n,high,i,low,mid;
    printf("Enter the number od array ");
    scanf("%d",&n);
    printf("enter the array");
    for(i=0;i<n;i++);
    scanf("%d",&num);
    printf("Enter the key");
    scanf("%d",&key);
    low=0;
    high=n-1;
    while(low<=high)
    {
        mid=(low+high)/2;
        if(key==num[mid])
        break;
        if(key>num[mid])
        low=mid+1;
        else
        high=mid-1;
    }
    if(low<=high)
    printf("The %d is found at positon %d",key,mid+1)
}