import matplotlib.pyplot as plt
desk ="/Users/lofangyu/Desktop/"
f = open(desk + "hw3_dataset.txt", "r")
list = f.readlines()

new_list = []
for i in range(len(list)):
    n = list[i].split()
    new_list.append(n)


c_train = []

for j in range(len(new_list)):
    c = new_list[j][1].count("1")
    if c >= 3:
        c_train.append(1)
    else:
        c_train.append(0)

def per(w0, w1, w2, w3, w4, w5, x1, x2, x3, x4, x5):
    cal = w0  + w1*x1 + w2*x2 +w3*x3 + w4*x4 + w5*x5
    if cal >0:
        return 1
    else:
        return 0

init = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
learn = [0.2, 0.4, 0.6, 0.8] 

h_c = [0, 0, 0, 0]

for p in range (len(learn)):
    for m in range (len(new_list)):
        h0 = per(init[0], init[1], init[2], init[3], init[4], init[5], eval(new_list[m][1][0]), eval(new_list[m][1][1]), eval(new_list[m][1][2]), eval(new_list[m][1][3]), eval(new_list[m][1][4]) )
        if h0 == c_train[m]:
            continue
        else:
            h_c[p] = h_c[p] + 1
        init[0] = round((init[0] +learn[p]*(c_train[m]-h0)*1) ,1)
        for k in range(len(new_list[m][1])):
            init[k+1] = round(init[k+1] +learn[p]*(c_train[m]-h0)*eval(new_list[m][1][k]), 1)

            
    print(init)
print(h_c)
plt.plot([0.2, 0.4, 0.6, 0.8], [h_c[0], h_c[1], h_c[2], h_c[3]])
plt.xlabel('learning rate')
plt.ylabel('the number of example-presentations')
plt.show()


