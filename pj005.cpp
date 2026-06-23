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

string intostring(int n)
{
	if (n == 0) return "0";
	
	else
	{
		string s = "", si = ""; // Strings résultat, la seconde inversée

		while (n > 0)
		{
			si += (n%10)+48;
			n = floor(n/10);
		}
		
		for (int k = si.length()-1; k >= 0; k--) s += si[k]; // Renverse la chaine
	
		return s;
	}
}


int ** facteurs_premiers(int n, int &nbrFacteurs)
{
	// Majoration du nombre de facteurs premiers et donc la taille des tableaux.
	int maj;
	maj = ceil(log2(n));
	
	int ** decomposition = new int* [2];
	for (int k = 0; k < 2; k++) decomposition[k] = new int [maj];
	

	int facteur = 1;
	int mult;
	nbrFacteurs = 0;
	
	while (n != 1)
	{
		do
		{
			facteur++;
		} while (!est_premier(facteur));
		mult = 0;
		while (n%facteur == 0)
		{
			mult ++;
			n /= facteur;
		}
		if (mult != 0)
		{
			decomposition[0][nbrFacteurs] = facteur;
			decomposition[1][nbrFacteurs] = mult;
			nbrFacteurs ++;
		}
	}
	
	return decomposition;
	
}

int ppcm(int a, int b)
{
	// Décomposition de a et de b
	
	int nbrFacteurs1, nbrFacteurs2;
	int ** decomposition1 = facteurs_premiers(a, nbrFacteurs1);
	int ** decomposition2 = facteurs_premiers(b, nbrFacteurs2);
	
	// Calcul du tableau résultat

	int** decomposition3 = new int* [2];
	
	for (int k = 0; k < 2; k++) decomposition3[k] = new int [nbrFacteurs1+nbrFacteurs2];
	
	for (int k = 0; k < nbrFacteurs1; k++)
	{
		decomposition3[0][k] = decomposition1[0][k];
		decomposition3[1][k] = decomposition1[1][k];
	}
	
	int nbrFacteurs3 = nbrFacteurs1;
	
	for (int k = 0; k < nbrFacteurs2; k++)
	{
		bool ajouter = true;
		for (int i = 0; i < nbrFacteurs1; i ++)
		{
			if (decomposition3[0][i] == decomposition2[0][k])
			{
				ajouter = false;
				decomposition3[1][i] = fmax(decomposition3[1][i], decomposition2[1][k]);
			}
		}
		if (ajouter)
		{
			decomposition3[0][nbrFacteurs3] = decomposition2[0][k];
			decomposition3[1][nbrFacteurs3] = decomposition2[1][k];
			nbrFacteurs3 ++;
		}
		
	}
	
	int res = 1;
	for (int k = 0; k < nbrFacteurs3; k++) res *= pow(decomposition3[0][k], decomposition3[1][k]);
	
	for (int k = 0; k < 2; k++) delete decomposition3[k];
	delete [] decomposition3;
	for (int k = 0; k < 2; k++) delete decomposition2[k];
	delete [] decomposition2;
	for (int k = 0; k < 2; k++) delete decomposition1[k];
	delete [] decomposition1;
	
	return res;
}

int pgcd(int a, int b)
{
	// Décomposition de a et de b
	
	int nbrFacteurs1, nbrFacteurs2;
	int ** decomposition1 = facteurs_premiers(a, nbrFacteurs1);
	int ** decomposition2 = facteurs_premiers(b, nbrFacteurs2);
	
	// Calcul du tableau résultat

	int** decomposition3 = new int* [2];
	
	for (int k = 0; k < 2; k++) decomposition3[k] = new int [nbrFacteurs1+nbrFacteurs2];
	
	for (int k = 0; k < nbrFacteurs1; k++)
	{
		decomposition3[0][k] = decomposition1[0][k];
		decomposition3[1][k] = decomposition1[1][k];
	}
	
	int nbrFacteurs3 = nbrFacteurs1;
	
	for (int k = 0; k < nbrFacteurs2; k++)
	{
		bool ajouter = true;
		for (int i = 0; i < nbrFacteurs1; i ++)
		{
			if (decomposition3[0][i] == decomposition2[0][k])
			{
				ajouter = false;
				decomposition3[1][i] = fmin(decomposition3[1][i], decomposition2[1][k]);
			}
		}
		if (ajouter)
		{
			decomposition3[0][nbrFacteurs3] = decomposition2[0][k];
			decomposition3[1][nbrFacteurs3] = decomposition2[1][k];
			nbrFacteurs3 ++;
		}
		
	}
	
	int res = 1;
	for (int k = 0; k < nbrFacteurs3; k++) res *= pow(decomposition3[0][k], decomposition3[1][k]);
	
	for (int k = 0; k < 2; k++) delete decomposition3[k];
	delete [] decomposition3;
	for (int k = 0; k < 2; k++) delete decomposition2[k];
	delete [] decomposition2;
	for (int k = 0; k < 2; k++) delete decomposition1[k];
	delete [] decomposition1;
	
	return res;
}

void aff_decomposition(int ** decomposition, int nbrFacteurs)
{
	for (int k = 0; k < 2; k++)
	{
		for (int i = 0; i < nbrFacteurs; i++)
		{
			cout << decomposition[k][i] << " ";
		}
		cout << endl;
	}
}



int main()
{
	int res = 1;
	
	for (int k = 1; k <= 20; k++)
	{
		res = ppcm(res, k);
	}
	
	cout << "Answer is " << res << "." << endl;

	return 0;
}
