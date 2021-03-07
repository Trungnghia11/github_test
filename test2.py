import matplotlib.pyplot as plt
print('----LINE CODING----')
print("")
print('1.NRZ-UNIPOLAR')
print('2.NRZ-L')
print('3.NRZ-I')
print('4.MANCHESTER')
print('5.DIFFERENTIAL-MANCHESTER')
print('')
##choice=int(input('Enter your choice:')) 



def chon(choice,x,y,num):
    
    if choice==1:
        ### NRZ,Unipolar
        for j in range(num):
            x.append(int(j))
    
        x = x*2
        x.sort()
        x.remove(x[0])
        x.append(num)
        m = []
        for k in y:
            m.extend([k, k])
        y = m
        zeros = list()
        for i in range(2 * num):
            zeros.append(int(0))
    
        l = list()
        for i in range(1, num + 1):
            l.append(int(i))
    
        print(zeros)
        print(x)
        print(y)
    
        plt.plot(x, y, linewidth=5.0)
        plt.plot(x, zeros, linewidth=1.0)
        plt.grid()
        plt.plot([0, 0], [0, 1.5])
        plt.title("NRZ-UNIPOLAR")
        plt.savefig("NRZ-UNIPOLAR.png")
     ##   plt.close('all')
        plt.show()
        ############
    if choice==2:
        ### NRZL,Polar
    
        for j in range(num):
            x.append(int(j))
    
        for i in range(num):
            if y[i] == 0:
                y[i] = 1
            else:
                y[i] = -1
    
        x=x*2
        x.sort()
        x.remove(x[0])
        x.append(num)
        m = []
        for k in y:
            m.extend([k, k])
        y = m
    
        print(x)
        print(y)
    
        zeros = list()
        for i in range(2 * num):
            zeros.append(int(0))
    
        print(zeros)
    
        plt.plot(x, y, linewidth=5.0)
        plt.plot(x, zeros, linewidth=1.0)
        plt.plot([0, 0, 0], [0, 1.5, -1.5])
        plt.grid()
        plt.title("NRZ-L")
        plt.savefig("NRZ-L.png")
    ##    plt.close('all')
        plt.show()
        ##########
    if choice==3:
        ### NRZ-I
        for j in range(num):
            x.append(int(j))
    
    
        for i in range(num - 1):
            if i == 0:
                y[i] = 1
            if y[i + 1] == 1:
                if y[i] == 1:
                    y[i + 1] = -1
                elif y[i] == -1:
                    y[i + 1] = 1
            elif y[i + 1] == 0:
                if y[i] == 1:
                    y[i + 1] = 1
                elif y[i] == -1:
                    y[i + 1] = -1
    
        print(y)
        print(x)
        x = x*2
        x.sort()
        x.remove(x[0])
        x.append(num)
        m = []
        for k in y:
            m.extend([k, k])
        y = m
        zeros = list()
        for i in range(2 * num):
            zeros.append(int(0))
    
        plt.plot(x, y, linewidth=5.0)
        plt.plot(x, zeros, linewidth=1.0)
        plt.plot([0, 0, 0], [0, 1.5, -1.5])
        plt.grid()
        plt.title("NRZ-I:-POLAR")
        plt.savefig("NRZ-I.png")
      ##  plt.close('all')
        plt.show()
        ##############
    if choice==4:
        ## Manchester
    
        yaxis = list()
        for i in range(0, num):
            if y[i] == 1:
                yaxis.append(-1)
                yaxis.append(1)
            if y[i] == 0:
                yaxis.append(1)
                yaxis.append(-1)
        print(yaxis)
    
        x = []
        for i in range(2 * num):
            x.append(i)
        x = x * 2
        x.sort()
        x.remove(x[0])
        x.append(2 * num)
    
        m = []
        for i in yaxis:
            m.extend([i, i])
        yaxis = m
        print(yaxis)
        print(x)
    
        zeros = list()
        for i in range(0, 4 * num):
            zeros.append(int(0))
    
        print(zeros)
    
        plt.plot(x, yaxis, linewidth=5.0)
        plt.plot(x, zeros, linewidth=1.0)
        plt.plot([0, 0, 0], [0, 1.5, -1.5])
        plt.grid()
        plt.title("MANCHESTER")
        plt.savefig("MANCHESTER.png")
       ## plt.close('all')
        plt.show()
        #######
    if choice==5:
        ## Manchester vi sai (D-Manchester )
    
        print(y)
        yaxis = list()
        for i in range(num - 1):
            if i == 0:
                if y[i] == 1:
                    yaxis.append(1)
                    yaxis.append(-1)
                elif y[i] == 0:
                    yaxis.append(-1)
                    yaxis.append(1)
            if y[i + 1] == 0:
                if yaxis[-1] == -1:
                    yaxis.append(1)
                    yaxis.append(-1)
                elif yaxis[-1] == 1:
                    yaxis.append(-1)
                    yaxis.append(1)
            if y[i + 1] == 1:
                if yaxis[-1] == -1:
                    yaxis.append(-1)
                    yaxis.append(1)
                elif yaxis[-1] == 1:
                    yaxis.append(1)
                    yaxis.append(-1)
    
        print(yaxis)
        m = []
        for i in yaxis:
            m.extend([i, i])
        yaxis = m
        for i in range(2 * num):
            x.append(i)
        x = x * 2
        x.sort()
        x.remove(x[0])
        x.append(2 * num)
        print(x)
        print(yaxis)
    
        zeros = list()
        for i in range(0, 4 * num):
            zeros.append(int(0))
    
        plt.plot(x, yaxis, linewidth=5.0)
        plt.plot(x, zeros, linewidth=1.0)
        plt.plot([0, 0, 0], [0, 1.5, -1.5])
        plt.grid()
        plt.title("DIFFERENTIAL-MANCHESTER")
        plt.savefig("D-MANCHESTER.png")
       ## plt.close('all')
        plt.show()
        #######
x = list()
y = list()
str = input("Enter Bits:")
num = len(str)

for i in range(num):
    y.append(int(str[i]))
chon(1,x,y,num)
x = list()
y = list()
for i in range(num):
    y.append(int(str[i]))
chon(2,x,y,num)
x = list()
y = list()
for i in range(num):
    y.append(int(str[i]))
chon(3,x,y,num) 
x = list()
y = list()
for i in range(num):
    y.append(int(str[i]))
chon(4,x,y,num)   
x = list()
y = list()
for i in range(num):
    y.append(int(str[i]))
chon(5,x,y,num)    
    
    
    