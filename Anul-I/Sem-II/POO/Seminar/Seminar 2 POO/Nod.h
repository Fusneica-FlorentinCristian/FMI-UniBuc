#pragma once
#ifndef NOD_H
#define NOD_H

class Nod
{
	int info;
	Nod* next;
public:
	Nod(int x):info(x),next(NULL){}
};

#endif //NOD_H