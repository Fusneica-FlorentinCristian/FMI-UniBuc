#include <cstdio>

int X,Y,Z;

int main()
{

    int x=1,y=2,z=3;
    printf("x=%d\n",x);
    printf("y=%d\n",y);
    printf("z=%d\n",z);

    printf("\n");
    printf("&x=%X\n",&x);
    printf("&y=%X\n",&y);
    printf("&z=%X\n",&z);

    int *p;
    int * q;
    int* r;

    p=&x;
    q=&y;
    r=&z;

    printf("\n");
    printf("p=%X\n",p);
    printf("q=%X\n",q);
    printf("r=%X\n",r);

    printf("\n");
    printf("&p=%X\n",&p);
    printf("&q=%X\n",&q);
    printf("&r=%X\n",&r);

    *p=15;
    *q=16;
    *r=17;

    printf("\n");
    printf("x=%d\n",x);
    printf("y=%d\n",y);
    printf("z=%d\n",z);


    printf("\n");
    printf("&x=%X\n",&x);
    printf("&y=%X\n",&y);
    printf("&z=%X\n",&z);


    int * pointerLaAdresaZero = NULL;

    ///*pointerLaAdresaZero=3333; ///aici crapa codul

    int * pointer;

    pointer = new int;

    printf("\n");
    printf("pointer=%X\n",pointer);
    *pointer = 333;
    printf("pointer=%d\n",*pointer);

    printf("\n");
    printf("&X=%X\n",&X);
    printf("&Y=%X\n",&Y);
    printf("&Z=%X\n",&Z);

    return 0;
}
