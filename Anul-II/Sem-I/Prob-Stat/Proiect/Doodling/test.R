# The probabilities used here give more dense fern.

niter<-150000
kind<-sample(1:4, niter, repl=T, prob=c(.01, .07, .07, .85))

x<-numeric(niter+1)
y<-numeric(niter+1)
x[1]<-0
y[1]<-0
for (i in 1:niter) {
  x[i+1]<- 0*(kind[i]==1)+(0.2*x[i]-0.26*y[i])*(kind[i]==2)+
    (-0.15*x[i]+0.28*y[i])*(kind[i]==3) +
    (0.85*x[i]+0.04*y[i])*(kind[i]==4)
  
  y[i+1]<- 0.16*y[i]*(kind[i]==1)+(0.23*x[i]+0.22*y[i]+1.6)*(kind[i]==2)+
    (0.26*x[i]+0.24*y[i]+.44)*(kind[i]==3) +
    (-0.04*x[i]+0.85*y[i]+1.6)*(kind[i]==4)
}

par(mar=c(0.1,0.1,0.1,0.1))
plot(x, y, pch=17, cex=.3, col="darkgreen", axes=F, ann=F)
