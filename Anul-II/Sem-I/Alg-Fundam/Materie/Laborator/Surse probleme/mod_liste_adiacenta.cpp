#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

void citire(int &n,vector<int> *&la,int orientat=0,const char *nume_fisier="graf.in"){
	int i,j,x,y,m;
	ifstream f(nume_fisier);
	f>>n>>m;
    la=new vector<int>[n];
 
	while(f>>x>>y){
		x--;y--;
		la[x].push_back(y);
		if (not orientat)
		    la[y].push_back(x);
	}
	f.close();
}
void afisare_liste(int n, vector<int> *la){
	int i,j;
	for(i=0;i<n;i++){
		cout<<i+1<<": ";
		for(j=0;j<la[i].size();j++)
			cout<<la[i][j]+1<<" ";
		cout<<endl;
	}
}


