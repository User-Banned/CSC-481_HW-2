def hBatchSum(w0,w1,dataSet):
    sum=0
    for x,y in dataSet:
        sum=sum+(y-(w0+w1*x))
    return sum

def batch(dataSet):
    w0=0.25
    w1=0.25
    alp=0.00001
    w0prev=0
    w1prev=0
    iteration=0
    while (iteration<10000000):
        if (abs(w0-w0prev)>pow(10,-10) and abs(w1-w1prev)>pow(10,-10))and(iteration<10000000):
            w0prev=w0
            w1prev=w1
            hSum=alp*hBatchSum(w0prev,w1prev,dataSet)
            w0 = w0prev + hSum
            w1 = w1prev + hSum
            iteration+=1
        else:    
            return w0,w1,iteration
    return w0,w1,iteration

def stochastic(dataSet):
    w0=0.25
    w1=0.25
    alp=0.00001
    w0prev=0
    w1prev=0
    iteration=0
    while (iteration<10000000):
        if (abs(w0-w0prev)>pow(10,-10) and abs(w1-w1prev)>pow(10,-10))and(iteration<10000000):
            for x,y in dataSet:
                w0prev=w0
                w1prev=w1
                hSto=alp*(y-(w0prev+w1prev*x))
                w0 = w0prev + hSto
                w1 = w1prev + hSto * x
                iteration+=1
        else:
            return w0,w1,iteration
    return w0,w1,iteration

dataSet=[[2,5],[4,7],[6,14],[7,14],[8,17],[10,19],[9,20]]

bW0,bW1,bIter=batch(dataSet)
sW0,sW1,sIter=stochastic(dataSet)
print('Results for Batch Gradient Descent:')
print('Iteration # :',bIter)
print('         w0 :',bW0)
print('         w1 :',bW1)
print('')
print('Results for Stochastic Gradient Descent:')
print('Iteration # :',sIter)
print('         w0 :',sW0)
print('         w1 :',sW1)
