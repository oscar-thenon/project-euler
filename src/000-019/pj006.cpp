#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int n = 100;
	int res = (n*(n-1)*(n+1)*(3*n+2))/12;
	
	cout << "Answer is " << res << "." << endl;
	
	return 0;
}
