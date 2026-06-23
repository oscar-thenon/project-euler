#include <iostream>
#include <math.h>

using namespace std;

bool est_premier(int n)
{
	if ((n == 0) or (n == 1)) return false;
	else if (n == 2) return true;
	else if (n%2 == 0) return false;
	else
	{
		int max = ceil(sqrt(n));
		for (int k = 3; k <= max; k += 2)
		{
			if (n%k == 0) return false;
		}
		return true;
	}
}

int main()
{
	int n = 1;
	for (int k = 0; k < 10001; k++)
	{
		do
		{
			n++;
		} while (!est_premier(n));
	}
	
	cout << "Answer is " << n << ".";
	
	return 0;
}
