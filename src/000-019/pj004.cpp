#include <iostream>
#include <string>

using namespace std;

// Retourne la chaîne correspondant à n écrit à l'envers
string intostringinv(int n)
{
	if (n == 0) return "0";
	else
	{
		int reste;
		string ns = "";
		do
		{
			reste = n%10;
			ns += reste+48;
			n = (n-reste)/10;
		} while (n != 0);
	
		return ns;
	}
}

// Retourne vrai si n est un palindrome
bool ispalindrom(int n)
{
	
	string ns = intostringinv(n);
	string nsi = ns;
	int l = ns.length();
	for (int k = 0; k < l; k++) nsi[k] = ns[l-1-k];
	
	return (ns == nsi);
}

int main ()
{
	int largestPalindrom = 0;
	int min = 100, max = 999, p;
	
	for (int a = min; a <= max; a++)
	{
	
		for (int b = a; b <= max; b++)
		{
			p = a*b;
			if ((p > largestPalindrom) and ispalindrom(p))
			{
				largestPalindrom = p;
			}
		}
	}
	

	cout << "Answer is " << largestPalindrom << "." << endl;
	
	return 0;
}
