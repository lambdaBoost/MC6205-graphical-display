from array import array
import json
import urequests

#order the anodes are illuminated in
"""
anode_order = [3,4,5,6,7,9,10,11,12,2,\
               15,16,17,18,19,21,22,23,24,14\
               ,27,28,29,30,31,33,34,35,36,26\
               ,39,40,41,42,43,45,46,47,48,38\
               ,51,52,53,54,55,57,58,59,60,50\
               ,63,64,65,66,67,69,70,71,72,62\
               ,75,76,77,78,79,81,82,83,84,74\
               ,87,88,89,90,91,93,94,95,96,86]
"""

anode_order = [2,3,4,5,6,7,9,10,11,12,\
               14, 15,16,17,18,19,21,22,23,24,\
               26,27,28,29,30,31,33,34,35,36,\
               38,39,40,41,42,43,45,46,47,48,\
               50,51,52,53,54,55,57,58,59,60,\
               62,63,64,65,66,67,69,70,71,72,\
               74,75,76,77,78,79,81,82,83,84,\
               86,87,88,89,90,91,93,94,95,96,\
               99,98,97,92,85,80,73,68,61,56,\
               49,44,37,32,25,20,13,8,1,0]


TEST_FILE = '../imgs/test_card_json.json'

def read_test_file():
    
    """
    reads the test card image and returns it as a nested list

    """
    with open(TEST_FILE) as f:
        dat = json.load(f)
        
    return dat

def get_row(array, row_num):
    
    np_row = array[row_num]
    
    #convert to int
    row_value = np_row.dot(2**np.arange(np_row.size)[::-1])
    
    #convert to 100 length binary string
    row_binary = row_value.format('#0100b')
    
def get_api_image(uri):
        
    w=urequests.get(uri)
    response = w.text
    
    return response
    