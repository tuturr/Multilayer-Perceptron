import matplotlib.pyplot as plt
import csv
import pandas as pd
import sys
from copy import deepcopy
#from lib import utils, maths, neural_network as nn
#from lib import utils, maths, neural as nn
#from lib import utils, maths, n as nn
from lib import utils, test as nn

if __name__ == "__main__":
    args = utils.arg_parse()
    reader = utils.get_csv_infos()
    if args.graph:
        tmp_reader = deepcopy(reader)
        c = 'black'
        for k in reader:
            if "ID" in k:
                pass
            else:
                if args.color:
                    c = utils.parse_color_hist(args.color)
                tmp_reader[str(k)].hist(color=c, alpha=0.5)
                plt.title(str(k))
                plt.xlabel("Value")
                plt.ylabel("Number of elements")
                plt.show()
    del reader['ID'] ##
    values = list(range(len(reader['Diagnosis'])))
    desired_outputs = []
    for i in range(len(reader['Diagnosis'])):
        values[i] = 0 if reader['Diagnosis'][i] == 'B' else 1
        desired_outputs.append([values[i]])
    reader['Diagnosis'] = values
    #desired_outputs = reader['Diagnosis']
    if args.plot:
        nn.scatter(reader)
    del reader['Diagnosis']
    train, test = utils.separate_data(reader)
    t = nn.NeuralNetwork(train, desired_outputs, 2, 20)
    #t.__str__()
    #nn.plot_training_test_samples(train, test)
    #scale = utils.get_min_max_scale(train)
    #nn.main_network([30, 20, 20, 2], train, test, desired_outputs, scale)
    #del reader['Diagnosis']
