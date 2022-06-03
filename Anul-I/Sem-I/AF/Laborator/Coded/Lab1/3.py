x=float(input("lungimea initiala x="))
n=float(input("numar sarituri pana se micsoreaza cu p n="))
p=float(input("procentul cu care se micsoreaza p="))
m=float(input("numar sarituri m="))
#sa se calculeze distanta parcursa de greiere

a=m//n #numarul de micsorari

s=0.0

while m>0:
    if m>n:
        s+=n*x
    else:
        s+=m*x
    x=x/100*(100-p)
    m-=n

print(s)

# Un greiere se deplasează efectuând câte o săritură, lungimea inițială a
# săriturii fiind de xx cm. După fiecare nn sărituri, lungimea săriturii greierului se
# micșorează cu pp procente. Cunoscându-se valorile xx, nn, pp, precum și
# numărul de sărituri mm pe care le face greierele, să se scrie un program care să
# afișeze distanța parcursă de greiere. De exemplu, pentru xx = 20, nn =
# 10, pp = 10 și mm = 20 distanța parcursă de greiere este egală cu 380 cm,
# deoarece primele 10 sărituri efectuate au, fiecare, lungimea de 20 cm, iar
# următoarele 10 au, fiecare, lungimea de 18 cm.