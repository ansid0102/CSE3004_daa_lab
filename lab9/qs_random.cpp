#include<iostream>
#include<cstdlib>

using namespace std;
int PARTITION(int [],int ,int );
void R_QUICKSORT(int [],int ,int );
int R_PARTITION(int [],int,int );
void printArray(int [],int );

int main()
{
       
    int a[]= {8, 7, 6, 1, 0, 9, 2};
    int n=sizeof(a)/sizeof(a[0]);
    
    cout<<"sorting using randomized quick sort"<<endl;
    int p=0,r=n;
    cout<<"Unsorted Array:"<<endl;
    printArray(a,n);

    R_QUICKSORT(a,p,r);
    cout<<"Sorted Array"<<endl;
    printArray(a,n);
     return 0;
}
void printArray(int array[], int size) {
  int i;
  for (i = 0; i <size; i++)
    cout << array[i] << " ";
  cout << endl;
}
void R_QUICKSORT(int a[],int p,int r)
    {
        int q;
        if(p<r)
        {
         q=R_PARTITION(a,p,r);
         R_QUICKSORT(a,p,q-1);
         R_QUICKSORT(a,q+1,r);
        }
    }

 int R_PARTITION(int a[],int p,int r)
 {
        int i=p+rand()%(r-p+1);
        int temp;
        temp=a[r];
        a[r]=a[i];
        a[i]=temp;
        return PARTITION(a,p,r);
  }

 int PARTITION(int a[],int p,int r)
 {
        int temp,temp1;
        int x=a[r];
        int i=p-1;
        for(int j=p;j<=r-1;j++)
        {
            if(a[j]<=x)
            {

                i=i+1;
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
        temp1=a[i+1];
        a[i+1]=a[r];
        a[r]=temp1;
        return i+1;
  }