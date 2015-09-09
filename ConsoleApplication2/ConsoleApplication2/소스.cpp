#include<iostream>
#include<cstdlib>
#include<ctime>

using namespace std;

int main()
{

	const int SIZE = 10;
	int score[SIZE];

	srand((unsigned int)time(NULL));
	for (int i = 0; i<SIZE; i++)
	{
		score[i] = rand() % 100;
	}

	for (int i = 0; i<SIZE; i++)
	{
		cout << score[i] << endl;

	}


	return 0;

}

