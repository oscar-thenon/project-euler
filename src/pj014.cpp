#include <iostream>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <map>

using namespace std;

int lcollatz (unsigned long long int n, map<unsigned long long int, unsigned int> &collatz)
{
		if (collatz.count(n) == 0) 
		{
			if (n%2 == 0) collatz[n] = 1+lcollatz(n/2, collatz);
			else collatz[n] = 1+lcollatz(3*n+1, collatz);
		}
		return collatz[n];
}

int main()
{
	map<unsigned long long int, unsigned int> collatz;
	
	collatz[1] = 1;
	
	unsigned long long int nmax;
	int lmax = 0;
	int ln;
	
	for (unsigned long long int n = 1; n < 1000000; n++)
	{
		ln = lcollatz(n, collatz);
		if (ln > lmax)
		{
			nmax = n;
			lmax = ln;
			cout << "New longest chain is " << lmax << " produced by the " << nmax << "th term." << endl;
		}
	}
	
	cout << endl << "Answer is " << nmax;
	cout << endl << "Details : producing " << lmax << " terms.";
	cout << endl << collatz.size() << " terms have been stored, the highest one is " << collatz.rbegin()->first << ".";
	cout << endl;
	
	return 0;
} 
