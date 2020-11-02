from math import exp
from random import random
from random import seed
import csv as c
import matplotlib.pyplot as plt


def csv_file(x):
    with open(x) as cs:
        cr = c.reader(cs,delimiter = ',')
        value = []
        for z in cr:
            data = []
            for v in z:
                data.append(float(v))
            value.append(data)
    return value


def init_network(input,hidden,output):
    network = []
    hi = [{'weights':[random() for z in range(input+1)]} for z in range(hidden)]
    network.append(hi)
    o = [{'weights':[random() for z in range(hidden+1)]} for z in range(output)]
    network.append(o)
    return network

def add_weights(w,i):
    sum = w[-1]
    for z in range(len(i)):
        sum += w[z]*i[z]
    return sum

def feed(network,inp):
    input = inp
    for layer in network:
        i = []
        for neuron in layer:
            act = add_weights(neuron['weights'],input)
            neuron['output'] = sigmoid(act)
            i.append(neuron['output'])
        input = i
    return input

def sigmoid(x):
    return 1.0/(1.0+exp(-x))

def deri(x):
    return x*(1.0-x)

def back(network,e):
    for z in reversed(range(len(network))):
        layer = network[z]
        errors = []
        if z==len(network)-1:
            for y in range(len(layer)):
                neuron = layer[y]
                errors.append(e[y]-neuron['output'])
        else:
            for y in range(len(layer)):
                error = 0.0
                neuron = layer[y]
                for w in range(len(network[z+1])):
                    neuron = network[z+1][w]
                    error += neuron['weights'][y]*neuron['delta']
                errors.append(error)
        for y in range(len(layer)):
            neuron = layer[y]
            neuron['delta'] = errors[y]*deri(neuron['output'])

def update_weights(network,data,lr):
    input = data
    for z in range(len(network)):
        layer = network[z]
        if z !=0:
            input = [neuron['output'] for neuron in network[z-1]]
        for neuron in layer:
            for y in range(len(input)):
                neuron['weights'][y]+=neuron['delta']*lr*input[y]
            neuron['weights'][-1]+=lr*neuron['delta']


def train(network,data,expected,lr,epoch):
    yy = []
    xx = []
    for z in range(epoch):
        rs = []
        print 'epoch no:', z
        for y in range(len(data)):
            sm = feed(network,data[y])
            back(network,expected[y])
            update_weights(network,data[y],lr)
            rs.append(abs(expected[y][0]-sm[0]))
        aa =  sum(rs)/len(data)
        print aa
        yy.append(aa)
        xx.append(z+1)
    tt = 'learning rate: ',str(lr),' epoch: ',str(epoch),' hidden: ', str(len(network[1][0]['weights'])-1)
    # plt.plot(xx,yy)
    # plt.title(tt)
    # plt.xlabel('epoch')
    # plt.ylabel('error')
    # plt.axis([0,epoch,0,1])
    # plt.savefig('t1.png')
    # plt.show()

data = [ [3.0,1.5],
         [2.0,1.0],
         [4,1.5,1],
         [3.0, 1.0],
         [3.5, .5],
         [2.0 , .5 ],
         [5.5,1.0],
         [1.0,1.0] ]
ex = [[1],
      [0],
      [1],
      [0],
      [1],
      [0],
      [1],
      [0]]

exm = [[2.0,1.0]]

data2 = [[1,1],
         [1,0],
         [0,1],
         [0,0]]
ex2 = [[0],
        [1],
        [1],
        [0]]

# network = init_network(2,2,1)

# train(network,data2,ex2,.001,600000)

# for z in ex2:
#     print feed(network,z)
