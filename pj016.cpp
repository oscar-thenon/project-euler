#include <iostream>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <map>

using namespace std;

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
	map<int,string> dico;
	
	dico[0] = "";
	dico[1] = "one";
	dico[2] = "two";
	dico[3] = "three";
	dico[4] = "four";
	dico[5] = "five";
	dico[6] = "six";
	dico[7] = "seven";
	dico[8] = "eight";
	dico[9] = "nine";
	dico[10] = "ten";
	dico[11] = "eleven";
	dico[12] = "twelve";
	dico[13] = "thirteen";
	dico[14] = "fourteen";
	dico[15] = "fifteen";
	dico[16] = "sixteen";
	dico[17] = "seventeen";
	dico[18] = "eighteen";
	dico[19] = "nineteen";
	dico[20] = "twenty";
	dico[30] = "thirty";
	dico[40] = "forty";
	dico[50] = "fifty";
	dico[60] = "sixty";
	dico[70] = "seventy";
	dico[80] = "eighty";
	dico[90] = "ninety";
	dico[1000] = "onethousand";
	
	int answer = 0;
	
	string s;
	int reste;
	
	for (int k = 1; k <= 1000; k++)
	{
		if (dico.count(k) == 0)
		{
			s = "";
			if (k < 100)
			{
				
				reste = k%10;
				s += dico[k-reste];
				s += dico[reste];
				dico[k] = s;
			}
			else
			{
				reste = k%100;
				s += dico[(k-reste)/100];
				s += "hundred";
				if (reste != 0) s += "and";
				s += dico[reste];
				dico[k] = s;
			}
		}
		answer += dico[k].length();
	}
	
	cout << endl << "Answer is " << answer;
	cout << endl;
	return 0;
}
