/*#include<iostream>
#include<string.h>
using namespace std;
struct student{
	char name[10];
	int kor;
	int eng;
	void showData(){
		cout << name << " " << kor << " " << eng << " " << endl;
	}
	void setData(char * pname, int _kor, int _eng)
	{
		kor = _kor;
		eng = _eng;
		strcpy(name, pname);

	}
};

int main()
{
	student std1; //�л���ü 1�� ����
	std1.setData("greenjoa", 5, 1);
	std1.showData();
	student std2;
	std2.setData("greenjoa2", 5, 5);
	std2.showData();
	
	std1.showData();

	return 0;
}
*/


/*#include<iostream>
using namespace std;
void printData(int(&pnum)[2][5])//reference Ÿ���� ������ ���� �ּҰ� �־���Ѵ�
	{
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < 5; j++)
				cout << pnum[i][j] << " ";
		cout << endl;
	}
	int main()
	{
		cout << "201511216 �̾���" << endl;
		int num[2][5] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		printData(num);
		cout << printData << endl;// �Լ� �̸� ��� �Լ��������: �ߺ� �ڵ带 ���ֱ� ���ؼ�
		return 0;
	}

	*/
/*#include<iostream>
using namespace std;
//void printData(int *pnum)
//void printData(int pnum[])
//void printData(int(&pnum)[10])
//void printData(int pnum[][5]) ������ �����ּҴ� �� ���� �����ּ�
//void printData(int(*pnum)[5]) // int 5�� �ش��ϴ� �ּҰ�
void printData(int(&pnum)[2][5])//reference Ÿ���� ������ ���� �ּҰ� �־���Ѵ�
{
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 5; j++)
			cout << pnum[i][j] << " ";
		cout << endl;
}
int main()
{
	cout << "201511216 �̾���" << endl;
	int num[2][5] = { 1, 2, 3, 4, 5 , 6, 7, 8, 9, 10 };
	printData(num);
	return 0;
}*/

/*#include<iostream>
using namespace std;
int main()
{
	cout << "201511216 �̾���" << endl;
	int a = 10; 
	int& b = a;
	b += 20;

	cout << a << " " << b <<" " << &a << " " << &b << endl;


	return 0;
}*/
#include<iostream>
using namespace std;
int main()
{
	int a = 10;
	int *b = &a;
	int**c = &b;
	cout << "201511216 �̾���" << endl;
	cout <<a<<" "<<b<<" "<<*b <<" " << **c<< " "<<endl;
	return 0;
}