import numpy as np
import os 
import pickle
import sys 

#-------------------------------------------------------------------    
# Define the path to the .odb:
#-------------------------------------------------------------------
filepath = r"C:\Users\Sondrbe\Documents\Article_2\NL_Mesh_Study\MyNew.odb"

#-------------------------------------------------------------------    
# Define the variables used in the simulation:
#-------------------------------------------------------------------            
Set_on_Part = False
Set_on_Assembly = True
instance = 'PART-1-1'   
step_name = 'STEP-1'               
geometrySet = 'RIGHT_BC'
output_int = False
output_nodes = ['U3', 'RF3']



#-------------------------------------------------------------------    
# Define the path to the read_odb scripts:
#-------------------------------------------------------------------
read_odb_scripts_path = r"C:\Users\Sondrbe\Documents\Read_ODB_scripts"

#------------------------------------------------------------------------------
# Define the main function repsonsible for calling the other python scripts:
#------------------------------------------------------------------------------
def ReadODB(work_directory, filename, instance, step_name, geometrySet, output_int, output_node, Set_on_Part, Set_on_Assembly):     
    if Set_on_Part:
        if output_node:		
            os.system('abaqus python {0}\\ReadODB_node_Part.py  "'.format(read_odb_scripts_path) + filepath + '"  "'+ instance +'"  "'+ geometrySet +'"  "' +   step_name + '"  "' + output_node +'"')
        elif output_int:		
            os.system('abaqus python {0}\\ReadODB_element_Part.py  "'.format(read_odb_scripts_path) + filepath + '"  "'+ instance +'"  "'+ geometrySet +'"  "' +   step_name + '"  "' + output_int +'"')
    if Set_on_Assembly:
        if output_node:
            os.system('abaqus python {0}\\ReadODB_node_Assembly.py  "'.format(read_odb_scripts_path) + filepath + '"  "'+ instance +'"  "'+ geometrySet +'"  "' +   step_name + '"  "' + output_node +'"')
        elif output_int:	
            os.system('abaqus python {0}\\ReadODB_element_Assembly.py  "'.format(read_odb_scripts_path) + filepath + '"  "'+ instance +'"  "'+ geometrySet +'"  "' +   step_name + '"  "' + output_int  +'"')
    # Write the results with JSON (?):
    file = open('data.pkl', 'rb')    #'ba' means append binary, may use this one instead!   'wb'
    data = pickle.load(file, encoding='latin1') #If Python 3!!
    file.close()
    os.remove('data.pkl')  
    return data

