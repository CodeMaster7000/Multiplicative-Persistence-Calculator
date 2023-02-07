import time
def multiplicative_persistence():
    n=input('Input number: ')
    product=1
    steps=0
    result=1
    time.sleep(1)
    print('Steps:')
    time.sleep(1.5)
    if len(n)!=1:
        for i in range(0,len(n)):
            product=product*int(n[i])
        print(product)
        steps=steps+1
        while len(str(product))!=1:
            a=str(product)
            for x in range(0,len(a)):
                product=result*int(a[x])
                result=product
            print(product)
            result=1
            steps=steps+1
        print('Multiplicative persistence:',steps)
    else:
        print(int(n))
        print('Multiplicative persistence:',0)
multiplicative_persistence()
