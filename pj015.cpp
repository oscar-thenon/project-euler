#include <iostream>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <time.h>

using namespace std;

/* NOTE IMPORTANTE

"First" est à comprendre comme "de gauche à droite". Par exemple les 3 "first" chiffres de 123456789 sont 123
et pas 789. */

// Le résultat fait au maximum 53 chiffres.

// a et b deux tableaux représentant un nombre. Ils ont chacun 53 chiffres (0 à gauche si besoin).
void mult2(int* a)
{
	int somme;
	int retenue = 0;
	int reste;
	
	for (int k = 302; k >= 0; k--)
	{
		somme = 2*a[k] + retenue;
		reste = somme%10;
		a[k] = reste;
		retenue = (somme-reste)/10;
	}
}

void afftab(int *t)
{
	for (int k = 0; k < 303; k++) cout << t[k] << " ";
	cout << endl;
}


int main()
{
	int n [303];
	for (int k = 0; k < 302; k++) n[k] = 0;
	n[302] = 1;
	for (int k = 0; k < 1000; k++) mult2(n);
	int somme = 0;
	for (int k = 0; k < 303; k++) somme += n[k];
	cout << "Answer is " << somme;
	cout << endl;
	
	return 0;
} 
