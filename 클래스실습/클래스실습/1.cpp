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
	student std1; //학생객체 1개 만듬
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
void printData(int(&pnum)[2][5])//reference 타입은 공간에 대한 주소가 있어야한다
	{
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < 5; j++)
				cout << pnum[i][j] << " ";
		cout << endl;
	}
	int main()
	{
		cout << "201511216 이아현" << endl;
		int num[2][5] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		printData(num);
		cout << printData << endl;// 함수 이름 출력 함수사용이유: 중복 코드를 없애기 위해서
		return 0;
	}

	*/
/*#include<iostream>
using namespace std;
//void printData(int *pnum)
//void printData(int pnum[])
//void printData(int(&pnum)[10])
//void printData(int pnum[][5]) 이차원 시작주소는 각 층의 시작주소
//void printData(int(*pnum)[5]) // int 5에 해당하는 주소값
void printData(int(&pnum)[2][5])//reference 타입은 공간에 대한 주소가 있어야한다
{
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 5; j++)
			cout << pnum[i][j] << " ";
		cout << endl;
}
int main()
{
	cout << "201511216 이아현" << endl;
	int num[2][5] = { 1, 2, 3, 4, 5 , 6, 7, 8, 9, 10 };
	printData(num);
	return 0;
}*/

/*#include<iostream>
using namespace std;
int main()
{
	cout << "201511216 이아현" << endl;
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
	cout << "201511216 이아현" << endl;
	cout <<a<<" "<<b<<" "<<*b <<" " << **c<< " "<<endl;
	return 0;
}