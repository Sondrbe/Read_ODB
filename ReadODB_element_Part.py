import numpy as np
import os 
from odbAccess import *
import pickle
import sys 


#-------------------------------------------------------------------    
# Define a helper function to split directory and file:
#------------------------------------------------------------------- 
def input_filepath(filepath):
    filesplit = filepath.split("\\")
    x = filesplit[0]
    for y in filesplit[1:-1]:
        x += '\\' + y
    file_directory, filename = x, filesplit[-1]
    return file_directory, filename


#-------------------------------------------------------------------    
# Read the input variables to the script:
#-------------------------------------------------------------------     
filepath = sys.argv[1]
instance = sys.argv[2]
geometrySet = sys.argv[3]
step_name = sys.argv[4]
output_node = sys.argv[5]


#-------------------------------------------------------------------    
# Change to working directory:
#------------------------------------------------------------------- 
directory, filename = input_filepath(filepath)
os.chdir(directory)


#-------------------------------------------------------------------    
# Define some helper functions to read the .odb file:
#-------------------------------------------------------------------  
def nodal_data(loadstep, nodeSet, output):
    data = []
    for label in nodeSet:
        string = 'Node ' + instance + '.' + str(label)
        a = [x for _,x in loadstep.historyRegions[string].historyOutputs[output].data]
        data.append(a) 
    return data
    
def node_labels(nodeSet):
    node_set = []
    for node in nodeSet:
        node_set.append(node.label)
    return node_set
	
def int_point_data(loadstep, elementSet, output):
    data = []
    for label in elementSet:
        string = 'Element ' + instance + '.' + str(label) + ' Int Point 1'
        a = [x for _,x in loadstep.historyRegions[string].historyOutputs[output].data]
        data.append(a)
    return np.array(data)

def element_labels(elementSet):
    elem_set = []
    for element in elementSet:
        elem_set.append(element.label)
    return elem_set
    
    
#-------------------------------------------------------------------    
# Read the .odb file:
#-------------------------------------------------------------------
odb = openOdb(filename)
assembly = odb.rootAssembly
step = odb.steps[step_name]

elementSet = assembly.instances[instance].elementSets[geometrySet]   # This line is unique!
elementSet = element_labels(elementSet)
result = int_point_data(step, elementSet, output_int)

#-------------------------------------------------------------------    
# Export the obtained results into Python:
#------------------------------------------------------------------- 
file = open('data.pkl', 'wb')    #'ba' means append binary, may use this one instead!   'wb'
pickle.dump(result, file)
file.close()