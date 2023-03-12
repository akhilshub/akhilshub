#include <iostream>
using namespace std;

int main() {
	int n,i,h;
	cin>>n;
	for(int i=0;i<5;i++)
	{
	    cin>>h;
	    if(h>=67 && h<=45001)
	    {
	        cout<<("YES\n");
	    }
	    else{
	        cout<<("NO\n");
	    }
	}
	
	return 0;
}
