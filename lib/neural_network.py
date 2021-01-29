import pandas as pd
import numpy as np
from copy import deepcopy ##

class Multilayer_Perceptron():
    #TODO
    def __init__(self, nb_inputs, nb_hidden_layers, nb_hidden_elems, nb_outputs, inputs):
        self.input_layer = np.zeros((1, nb_inputs), dtype=np.float64) #creation input layer
        self.input_layer = self.fill_input_layer(inputs, self.input_layer) #remplissage input layer
        self.bias_input = 1
        self.hidden_layers = np.zeros((nb_hidden_layers, nb_hidden_elems)) #creation matrice de hidder layers

    #TODO
    def fill_input_layer(self, inputs, input_layer):
        for i in range(len(input_layer)):
            neuron = Perceptron(inputs[i])
            neuron.init_neuron(inputs[i], self.bias_input) #init chaque neuronne de la input layer with same bias and weight correspondant a chaque input
            input_layer[i] = neuron
        return input_layer


class Perceptron():
    #TODO
    def __init__(self):
        self.z = 0
        self.bias = 0
        self.weight = 0

    #TODO
    def init_neuron(self, weights, bias, input_layer=False):
        self.set_bias(bias)
        #Input Layer is a bool that indicates if we are undergoing init of input layer or not
        if input_layer:
            self.weight = weights
        elif not input_layer:
            self.weight = weighted_sum(weights, bias)


    def set_bias(self, bias):
        self.bias = bias

    def __str__(self):
        print("\033[1mWeight\033[0m : {}\033[1m\nBias\033[0m : {}\n\033[1mZ\033[0m : {}".format(self.weight, self.bias, self.z))

#----------------------------------------------------------------#
#                   Activation Functions                         #

def sigmoid(index_e, w_sum, bias):
    e = 2.71828
    z = (b + w_sum) * -1
    sig = (1 / (1 + e**z))
    return sig

def ReLU(z):
    #return 0 if z < 0 else return 1
    return 0 if z < 0 else return z

#                                                                #
#----------------------------------------------------------------#

def create_multilayer_perceptron(nb_hidden_layers, inputs, size_output_layer):
    pass

def create_perceptron(inputs, weights, activation_func, bias):
    bias = 1    

def xavier_init(layer, previous_layer):
    W = np.random.randn((np.size(layer), np.size(previous_layer)) * (np.sqrt(2 / (np.size(previous_layer) + np.size(layer)))))
    return W

def weighted_sum(weights, bias):
    weighted_sum = 0
    for i in range(len(weights)):
        weighted_sum += weights[i] * i
    weighted_sum += 1 * bias
    return weighted_sum