import matplotlib.pyplot as plt
import random as rd
desk ="/Users/lofangyu/Desktop/"
f = open(desk + "hw3_dataset.txt", "r")
list = f.readlines()

new_list = []
for i in range(len(list)):
    n = list[i].split()
    new_list.append(n)


new_list1 = []
new_list5 = []
new_list10 = []
new_list20 = []


for h in range (len(new_list)):
    attribute = new_list[h][1] + str(rd.randrange(0, 2, 1))
    new_list1.append(attribute)

for h in range (len(new_list)):
    attribute = new_list[h][1]
    for x in range(5):
        A = str(rd.randrange(0,2,1))
        attribute += A
    new_list5.append(attribute)

for h in range (len(new_list)):
    attribute = new_list[h][1]
    for x in range(10):
        A = str(rd.randrange(0,2,1))
        attribute += A
    new_list10.append(attribute)

for h in range (len(new_list)):
    attribute = new_list[h][1]
    for x in range(20):
        A = str(rd.randrange(0,2,1))
        attribute += A
    new_list20.append(attribute)

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

def per1(w0, w1, w2, w3, w4, w5, w6, x1, x2, x3, x4, x5, x6):
    cal = w0  + w1*x1 + w2*x2 +w3*x3 + w4*x4 + w5*x5 +w6*x6
    if cal >0:
        return 1
    else:
        return 0

def per5(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    cal = w0  + w1*x1 + w2*x2 +w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + w9*x9 + w10*x10
    if cal >0:
        return 1
    else:
        return 0

def per10(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15):
    cal = w0  + w1*x1 + w2*x2 +w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + w9*x9 + w10*x10  + w11*x11 + w12*x12 +w13*x13 + w14*x14 + w15*x15
    if cal >0:
        return 1
    else:
        return 0

def per20(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25):
    cal = w0  + w1*x1 + w2*x2 +w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + w9*x9 + w10*x10  + w11*x11 + w12*x12 +w13*x13 + w14*x14 + w15*x15 + w16*x16 + w17*x17 + w18*x18 + w19*x19 + w20*x20  + w21*x21 + w22*x22 +w23*x23 + w24*x24 + w25*x25
    if cal >0:
        return 1
    else:
        return 0
init = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
init1 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
init5 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
init10 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
init20 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

h_c = [0, 0, 0, 0, 0]


for m in range (len(new_list)):
    h0 = per(init[0], init[1], init[2], init[3], init[4], init[5], eval(new_list[m][1][0]), eval(new_list[m][1][1]), eval(new_list[m][1][2]), eval(new_list[m][1][3]), eval(new_list[m][1][4]) )
    if h0 == c_train[m]:
        continue
    else:
        h_c[0] = h_c[0] + 1
    init[0] = round((init[0] +0.2*(c_train[m]-h0)*1) ,1)
    for k in range(len(new_list[m][1])):
        init[k+1] = round(init[k+1] +0.2*(c_train[m]-h0)*eval(new_list[m][1][k]), 1)

for m in range (len(new_list1)):
    h0 = per1(init1[0], init1[1], init1[2], init1[3], init1[4], init1[5], init1[6], eval(new_list1[m][0]), eval(new_list1[m][1]), eval(new_list1[m][2]), eval(new_list1[m][3]), eval(new_list1[m][4]),  eval(new_list1[m][5]))
    if h0 == c_train[m]:
        continue
    else:
        h_c[1] = h_c[1] + 1
    init1[0] = round((init1[0] +0.2*(c_train[m]-h0)*1) ,1)
    for k in range(len(new_list1[m])):
        init1[k+1] = round(init1[k+1] +0.2*(c_train[m]-h0)*eval(new_list1[m][k]), 1)

for m in range (len(new_list5)):
    h0 = per5(init5[0], init5[1], init5[2], init5[3], init5[4], init5[5], init5[6], init5[7], init5[8], init5[9], init5[10], eval(new_list5[m][0]), eval(new_list5[m][1]), eval(new_list5[m][2]), eval(new_list5[m][3]), eval(new_list5[m][4]),  eval(new_list5[m][5]), eval(new_list5[m][6]), eval(new_list5[m][7]), eval(new_list5[m][8]), eval(new_list5[m][9]))
    if h0 == c_train[m]:
        continue
    else:
        h_c[2] = h_c[2] + 1
    init5[0] = round((init5[0] +0.2*(c_train[m]-h0)*1) ,1)
    for k in range(len(new_list5[m])):
        init5[k+1] = round(init5[k+1] +0.2*(c_train[m]-h0)*eval(new_list5[m][k]), 1)

for m in range (len(new_list10)):
    h0 = per10(init10[0], init10[1], init10[2], init10[3], init10[4], init10[5], init10[6], init10[7], init10[8], init10[9], init10[10], init10[11], init10[12], init10[13], init10[14], init10[15], eval(new_list10[m][0]), eval(new_list10[m][1]), eval(new_list10[m][2]), eval(new_list10[m][3]), eval(new_list10[m][4]),  eval(new_list10[m][5]), eval(new_list10[m][6]), eval(new_list10[m][7]), eval(new_list10[m][8]), eval(new_list10[m][9]), eval(new_list10[m][10]), eval(new_list10[m][11]), eval(new_list10[m][12]), eval(new_list10[m][13]), eval(new_list10[m][14]))
    if h0 == c_train[m]:
        continue
    else:
        h_c[3] = h_c[3] + 1
    init10[0] = round((init10[0] +0.2*(c_train[m]-h0)*1) ,1)
    for k in range(len(new_list10[m])):
        init10[k+1] = round(init10[k+1] +0.2*(c_train[m]-h0)*eval(new_list10[m][k]), 1)

for m in range (len(new_list20)):
    h0 = per20(init20[0], init20[1], init20[2], init20[3], init20[4], init20[5], init20[6], init20[7], init20[8], init20[9], init20[10], init20[11], init20[12], init20[13], init20[14], init20[15], init20[16], init20[17], init20[18], init20[19], init20[20], init20[21], init20[22], init20[23], init20[24], init20[25], eval(new_list20[m][0]), eval(new_list20[m][1]), eval(new_list20[m][2]), eval(new_list20[m][3]), eval(new_list20[m][4]),  eval(new_list20[m][5]), eval(new_list20[m][6]), eval(new_list20[m][7]), eval(new_list20[m][8]), eval(new_list20[m][9]), eval(new_list20[m][10]), eval(new_list20[m][11]), eval(new_list20[m][12]), eval(new_list20[m][13]), eval(new_list20[m][14]),  eval(new_list20[m][15]), eval(new_list20[m][16]), eval(new_list20[m][17]), eval(new_list20[m][18]), eval(new_list20[m][19]), eval(new_list20[m][20]), eval(new_list20[m][21]), eval(new_list20[m][22]),  eval(new_list20[m][23]), eval(new_list20[m][24]))
    if h0 == c_train[m]:
        continue
    else:
        h_c[4] = h_c[4] + 1
    init20[0] = round((init20[0] +0.2*(c_train[m]-h0)*1) ,1)
    for k in range(len(new_list20[m])):
        init20[k+1] = round(init20[k+1] +0.2*(c_train[m]-h0)*eval(new_list20[m][k]), 1)
             
print(init)
print(init1)
print(init5)
print(init10)
print(init20)
print(h_c)




