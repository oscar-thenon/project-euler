#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int c;
	
	for (int a = 1; a <= 500; a++)
	{
		for (int b = a; b <= 1000; b++)
		{
			c = 1000-a-b;
			if ((c >= 1) and (c*c == a*a+b*b))
			{
				cout << "Answer is " << a*b*c << endl;
			}
		}
	} 
	
	return 0;
}
