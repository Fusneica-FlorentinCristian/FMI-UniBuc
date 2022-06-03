// Exemplu seminar 1.cpp : Defines the entry point for the console application.

#include "stdafx.h"
#include <iostream>
using namespace std;

class punct {
	int x, y;
public:
	punct(){
		x = 0;
		y = 0;
	}
	punct(int a, int b) {
		x = a;
		y = b;
	}
	punct(punct &p) {
		x = p.x;
		y = p.y;
	}
	~punct() {
		cout << "\nPunct distrus";
	}
protected:
	void f(int a, int b)
	{
		cout << a + b;
	}
}p;

class punct2 : public punct
{
public:
	punct2(int ceva) {
		int a = 5, b = 6;
		f(a, b);
	}
};



int main()
{
	punct z, a(5,6), b(a),c(z);
	cout << "ceva";
	
}