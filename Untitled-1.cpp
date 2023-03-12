#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    int c1,c2,z1,n,i;
    while(t>0)
    {
     cin>>n;
     int b[n];
     for(i=0;i<n;i++)
     {
         cin>>b[i];
         if(b[i]==1)
         {
             c1++;
         }
         if(b[i]==0)
         {
             c2++;
         }
     }
     z1=c1+c2+c2;
     if((n%2)==0 && (z1%2)==0)
     {
      cout<<"YES";
     }
     else if(z1==n)
     {
      cout<<"YES"; 
     }
     else cout<<"NO";
     t--;
    }
    
	return 0;
}
