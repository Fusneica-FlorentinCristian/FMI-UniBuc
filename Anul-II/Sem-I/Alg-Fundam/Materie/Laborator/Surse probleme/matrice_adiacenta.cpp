#include<iostream>
#include<fstream>
using namespace std;
void afisare_matrice(int n,int **a){
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++)
			cout<<a[i][j]<<" ";
		cout<<endl;	
	}
}
void citire(int &n, int**&a, int orientat=0, const char* nume_fisier="graf.in"){
	int i,x,y,j,m;
	ifstream f(nume_fisier);
	f>>n>>m;
	a=new int*[n];
	for(i=0;i<n;i++)
	    a[i]=new int[n];
	for(i=0;i<n;i++)
	    for(j=0;j<n;j++)
		    a[i][j]=0;    
 
	while(f>>x>>y){
		x--; y--;
		a[x][y]=1;
		if(not orientat)
		    a[y][x]=1;
	}
	f.close();
}


int main(){
	int **a,n;
	citire(n,a);
	afisare_matrice(n,a);
	
}
