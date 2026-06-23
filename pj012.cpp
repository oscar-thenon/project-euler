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

// Retourne vrai si le nombre de diviseurs de n*(n+1)/2 est supérieur à 500.
bool isOver500(int** decomposition1, int nbrFacteurs1, int **decomposition2, int nbrFacteurs2)
{

	int* decompositionp = new int [nbrFacteurs1+nbrFacteurs2];
	
	for (int k = 0; k < nbrFacteurs1; k++)
	{
		decompositionp[k] = decomposition1[1][k];
	}
	
	int nbrFacteursp = nbrFacteurs1;
	
	for (int k = 0; k < nbrFacteurs2; k++)
	{
		bool ajouter = true;
		for (int i = 0; i < nbrFacteurs1; i ++)
		{
			if (decomposition1[0][i] == decomposition2[0][k])
			{
				ajouter = false;
				decompositionp[i] = decomposition1[1][i] + decomposition2[1][k];
			}
		}
		if (ajouter)
		{
			decompositionp[nbrFacteursp] = decomposition2[1][k];
			nbrFacteursp ++;
		}
	}
	
	// On divise par 2
	if (decomposition1[0][0] == 2) decompositionp[0] -= 1; 
	else decompositionp[nbrFacteurs1] -= 1;
	
	int p = 1;
	
	for (int k = 0; k < nbrFacteursp; k++) p *= decompositionp[k]+1;
	
	delete [] decompositionp;

	return (p > 500);
}

// On copie le contenu de decomposition2 dans decomposition1
void copie(int** decomposition1, int &nbrFacteurs1, int **decomposition2, int nbrFacteurs2)
{
	// On vide decomposition1
	for (int k = 0; k < 2; k++) delete [] decomposition1[k];
	
	// On copie
	nbrFacteurs1 = nbrFacteurs2;
	for (int k = 0; k < 2; k++) decomposition1[k] = new int [nbrFacteurs1];
	for (int k = 0; k < nbrFacteurs1; k++)
	{
		decomposition1[0][k] = decomposition2[0][k];
		decomposition1[1][k] = decomposition2[1][k];
	}
}

int main()
{
	int n = 2;
	long int nTri; // nième nombre triangulaire
	
	int nbrFacteurs1; // Nbr facteurs n
	int ** decomposition1 = facteurs_premiers(2, nbrFacteurs1); // Décomposition n
	int nbrFacteurs2; // Nbr facteurs n+1
	int ** decomposition2 = facteurs_premiers(3, nbrFacteurs2); // Décomposition n+1
	
	while (not isOver500(decomposition1, nbrFacteurs1, decomposition2, nbrFacteurs2))
	{
		n++;
		copie(decomposition1, nbrFacteurs1, decomposition2, nbrFacteurs2); // n remplacé par n+1;
		
		// On vide decomposition2 avant mise à jour
		for (int k = 0; k < 2; k++) delete [] decomposition2[k];
		delete [] decomposition2;
		decomposition2 = facteurs_premiers(n+1, nbrFacteurs2); // Mise à jour de decomposition2
	}

	nTri = n*(n+1)/2;
	cout << "Answer is " << nTri << endl;
	cout << "Details : " << "reached by the " << n << "th triangular number." << endl;
	
	// Vidage final
	for (int k = 0; k < 2; k++) delete [] decomposition1[k];
	delete [] decomposition1;
	for (int k = 0; k < 2; k++) delete [] decomposition2[k];
	delete [] decomposition2;
	
	return 0;
}
