#include<stdio.h>
int main()
{
	int arr[100],i,j,n,arr2[100],arr3[100],temp,last,first=1;
	printf("Enter the size of Array:\n");
	scanf("%d",&n);
	last=n;
	printf("Enter the Elements in Array:\n");
	for(i=1;i<=n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i=1;i<=n;i++)
	{
		for(j=i+1;j<=n;j++)
		{
			if(arr[i]>arr[j])
			{
				temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}	
	for(i=1;i<=n;i++)
	{
		if(i%2==0)
		{
			arr2[i]=arr[first];
			first=first+1;		
		}
		else{
			arr2[i]=arr[last];
			last=last-1;
		}
	}
	printf("\nThe final array is :\n");
	for(i=1;i<=n;i++)
	{
		printf("%d\t",arr2[i]);
	}
	//in this code i have first sorted the array and then i have arranged the them in a new array that is derived alternatively starting from first and last element of the sorted array//
    //this code is writen in C language//
	
	
	
}
