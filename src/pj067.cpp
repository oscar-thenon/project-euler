#include <iostream>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <fstream>

using namespace std;

// Réponse > 6477

int strtoint(string s)
{
	int res = 0;
	res += 10*(s[0]-48);
	res += s[1]-48;
	return res;
}

void aff(int ** tab, const int N)
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			cout << tab[i][j] << " ";
		}
		cout << endl;
	}
}

int aleatoire(int a, int b)
{
	int plage = b - a + 1;
	int tirage;
	tirage = (rand()%plage)+a;
	return tirage;
}

int main()
{
	srand((unsigned int)time(NULL));

	const int N = 100;
	
	int** triangle = new int* [N];
	for (int k = 0; k < N; k++) triangle[k] = new int [k+1];
	
	ifstream fichier ("pj067_triangle.txt");
	string slot;
	if (fichier.is_open())
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j <= i; j++)
			{
				fichier >> slot;
				triangle[i][j] = strtoint(slot);
			}
		}
		fichier.close();
	}
	else return EXIT_FAILURE;
	
	int** trianglecopie = new int* [N];
	for (int k = 0; k < N; k++) trianglecopie[k] = new int [k+1];
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			trianglecopie[i][j] = triangle[i][j];
		}
	}
	
	for (int k = 0; k < N-1; k++)
	{
		triangle[k+1][0] += triangle[k][0];
		triangle[k+1][k+1] += triangle[k][k];
		for (int i = 1; i < k+1; i++)
		{
			triangle[k+1][i] = fmax(triangle[k+1][i]+triangle[k][i-1],triangle[k+1][i]+triangle[k][i]);
		}
	}
	
	int imax = 0;
	int vmax = triangle[N-1][0];
	int temp;
	
	for (int k = 1; k < N; k++)
	{
		temp = triangle[N-1][k];
		if (temp > vmax)
		{
			vmax = temp;
			imax = k;
		}
	}
	cout << "Answer is " << vmax << endl;
	cout << "Details : the path is ";
	
	int lechemin [N];
	
	for (int k = N-1; k > 0; k--)
	{
		lechemin[k] = trianglecopie[k][imax];
		vmax = 0;
		
		if ((imax != 0) and (triangle[k-1][imax] < triangle[k-1][imax-1]))
		{
			imax --;
		}
	}
	lechemin[0] = trianglecopie[0][0];
	
	for (int k = 0; k < N;k++) cout << lechemin[k] << " > ";
	cout << endl;
	
	
	for (int k = 0; k < N; k++) delete [] trianglecopie[k];
	delete [] trianglecopie;
	for (int k = 0; k < N; k++) delete [] triangle[k];
	delete [] triangle;
	
	return 0;
} 
