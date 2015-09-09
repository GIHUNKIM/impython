#include <iostream>
using namespace std;
int main()
{
	const int SIZE = 4;
	int data[SIZE][SIZE] = { { 1, 2, 3, 4 }, { 3, 4, 5, 6 }, { 1, 2, 3, 4 }, { 3, 4, 5, 6 } };
	cout << sizeof(data) << endl;
	cout << sizeof(data[0]) << endl;

	int* pdata;
	for (int i = 0; i < SIZE; i++)
	{
		pdata = data[i];
		for (int j = 0; j < SIZE; j++)
			cout << pdata[j] << "\t";
		cout << endl;
 	}
	return 0;
}
