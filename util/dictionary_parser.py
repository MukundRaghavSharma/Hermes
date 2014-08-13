import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from yahoo_finance_attributes import attributes

def parse_dictionary(input_dictionary):
    return_attributes = []
    for input in input_dictionary:
        try:
            attr = attributes[input]
            return_attributes.append(attr)
        except:
            print "input error on: ", input
    return return_attributes
