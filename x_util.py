x_util.py: Various Routines and Utilities for Nefarious Purposes
#!/usr/bin/python
import sys
sys.path.insert (0, '/usr/local/lib/python-1.5/lib')

# remember to delete the above line when changing operating systems
#
# This module consists of general purpose utilities
# Things that i tend to use in every program I write
#
# This is version 0.0.0.6
# Creation Date: 9 May 2001 @ 18:59 H GMT
# Last Update:7 September 2002 @ 23:51 GMT
# Copyright: 2001 - 2002 Jonathon Blake
# Licence Terms: GNU General Public Licence

#
# 7 September 2002
#
# Added bump_case
#
# 8 September 2002
#
# added convert_unknown_to_string
# convert_integer_to_string
# clean_string
#
#

import string

#
# Now the utilities start
#

def bump_case(bump_string):
bump_string, atribute_data = clean_string(bump_string)
if atribute_data == "string":
 return_string = bump_string
elif atribute_data == "unknown":
 bump_string = bump_string[0]
 bump_string = convert_unknown_to_string(bump_string)
elif atribute_data == "integer":
 return_string = convert_integer_to_string(bump_string)
else:
 print " bump_case(bump_string) can not process the following "
 print bump_string
 print " as it is not a string "
 print " It appears to be the following: ", atribute_data
return return_string


def convert_integer_to_string(integer_string):
print " converting the following to a string "
print " : ", integer_string, " : "
integer_string = str(integer_string)
checkpoint = len(integer_string)
return_string, attribute_type = clean_string(integer_string)
return return_string

def convert_unknown_to_string(unknown_string):
some_string = unknown_string[0]
return_string, attribute_type = clean_string(some_string)
return return_string

def clean_string(some_string):
try:
 check = len(some_string)
# print check
 new_string = string.strip (some_string)
 check_string = string.lower (new_string)
 attribute_type = "string"
except TypeError:
 try:
 check_string = int(some_string)
 attribute_type = "integer"
 except:
 print "Unknown Error at clean string"
 print some_string
 print "This is neither a string, nor an integer"
 attribute_type = "unknown"
 check_string = some_string
#if attribute_type == "integer":
# check_string = convert_integer_to_string(check_string)
#elif attribute_type == "unknown":
# check_string = convert_unkown_to_string (check_string)
return check_string, attribute_type


def clear_screen(choice):
# Python seems to require that every function accept a paramater.
# In this instance choice is simply a space filler.
page_length = 25
# That is the number of lines most monitors have
# Change it to an appropriate figure, if necessary
for kount in range(page_length):
 print
print
return

def print_headline(header_line):
clear_screen
print
print header_line
print
return

def true_false(message_string):
is_valid = "false"
while is_valid == "false":
 print_headline(message_string)
 print ('If this is correct, type "yes". ')
 #, otherwise type "no". ')
 temp_string = raw_input()
 temp_string = string.strip(temp_string)
 temp_string = string.lower(temp_string)
 if temp_string in ["yes", "true","0", "+", "ja", "y", "good", "g" ]:
 check_point = "true"
 is_valid = "true"
 elif temp_string in ["no", "false", "1", "-", "nie", "n", "bad", "b" ]:
 check_point = "false"
 is_valid = "true"
 else:
 is_valid = "false"
return check_point

def read_input_data(message_string, validation_string):
check_point = "false"
while check_point == "false":
 clear_screen (5)
 print message_string
 input_string = raw_input()
 input_string = string.strip(input_string)
 temp_string = (validation_string + " " + input_string)
 check_point = true_false(temp_string)
return input_string

def in_range(check_this_number, low_number, high_number):
check_this_number = abs(check_this_number)
if check_this_number > high_number:
 check_this_number = check_this_number / high_number
if check_this_number < low_number:
 check_this_number = check_this_number + high_number
return check_this_number

# file read / write functions

def get_lines_of_file(var_which_file):
# This function counts the number of lines in a file
# and returns that number
file_suffix = string.lower(var_which_file)
check_the_file = string.strip(file_suffix)
try:
 input_file_handle = open(check_this_file, "r")
 data = input_file_handle.readlines()
 break_line_count = len(data)
except:
 break_line_count = 0
return break_line_count

def print_a_file(var_which_file, temp_line):
file_name = validate_file_name (var_which_file, "data")
print_to_this_file = file_name
print "About to write to file: ", print_to_this_file, " [Function: print_a_file ] "
write_line = string.strip(str(temp_line))
check_point = len(write_line)
if check_point > 1:
 line_count = get_lines_of_file(print_to_this_file)
 if line_count > 0 :
 kountry_datafile = open(print_to_this_file, "w")
 kountry_datafile.write(write_line + "\n")
 kountry_datafile.close()
 kounter = 1
 else:
 kountry_datafile = open(print_to_this_file, "a")
 kountry_datafile.write(write_line + "\n")
 kountry_datafile.close()
 kounter = 0
else:
 kounter = 0
return kounter

def validate_file_name(file_prefix, file_suffix):
file_prefix = bump_case(file_prefix)
file_suffix = bump_case(file_suffix)
if len(file_prefix) > 8:
 file_prefix - file_prefix[0:7]
#print file_prefix, " is the file prefix after surgery "
if len(file_suffix) > 3:
 file_suffix = file_suffix[0:3]
file_suffix = ("." + file_suffix)
#print file_suffix, " is the file suffix after surgery "
return_name = (file_prefix + file_suffix)
print return_name, " is the file name that was created/verified "
return return_name


print " x_util module is loaded"
