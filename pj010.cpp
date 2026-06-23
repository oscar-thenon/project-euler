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
	int l = 2000000;
	long long int somme = 2;
	for (int k = 3; k < l; k+= 2)
	{
		if (est_premier(k)) somme += k;
	}
	cout << "Answer is " << somme << endl;
	
	return 0;
}
