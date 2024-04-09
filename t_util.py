t_util.py: Trigram Related Routines
#!/usr/bin/python
import sys
sys.path.insert (0, '/usr/local/lib/python-1.5/lib')
# remember to delete the above line when changing operating systems
#
#
# YiJing Construction Program
#
# Initialization routines for trigrams
#
# Licence Terms: GNU General Public Licence
#
# Module History
#
# 5 February 2002
#
# Segregated out of hexagram.py
#

import h_util, x_util, time

# trigram functions are below this line

def trigram_name_trigram_line(trigram_name):
trigram_name = x_util.bump_case(trigram_name)
trigram_name_table = {
 "qian" : ("qian", "|", "|", "|"),
 "dui" : ("dui","|", "|", "o"),
 "li": ("li", "|", "o", "|"),
 "zhen" : ("zhen", "|", "o", "o"),
 "sun" : ("sun","o", "|", "|"),
 "kan" : ("kan","o", "|", "o"),
 "gen" : ("gen","o", "o", "|"),
 "kun" : ("kun","o", "o", "o")
 }
try:
 trigram_lines = trigram_number_table[trigram_name]
except:
 trigram_lines = ("m33", "*", "*", "*")
return trigram_lines

return trigram_line

def trigram_number_to_name(trigram_number):
# this uses FuXi numbers
trigram_number = in_range(trigram_number, 1, 8)
trigram_number_table = {
 "1" : ("qian", "|", "|", "|"),
 "2" : ("dui","|", "|", "o"),
 "3" : ("li", "|", "o", "|"),
 "4" : ("zhen", "|", "o", "o"),
 "5" : ("sun","o", "|", "|"),
 "6" : ("kan","o", "|", "o"),
 "7" : ("gen","o", "o", "|"),
 "8" : ("kun","o", "o", "o")
 }
try:
 return_trigram_name = trigram_number_table[trigram_number]
except:
 return_trigram_name = ("altair", "*", "*", "*")
return return_trigram_name

def wen_trigram_number_to_name(trigram_number):
trigram_number = in_range(trigram_number, 1, 9)
trigram_number_table = {
 1 : ("kan","o", "|", "o"),
 2 : ("kun","o", "o", "o"),
 3 : ("zhen","|", "o", "o"),
 4 : ("sun","o", "|", "|"),
 5 : ("m36","*", "*", "*"),
 6 : ("qian", "|", "|", "|"),
 7 : ("dui","|", "|", "o"),
 8 : ("gen","o", "o", "|"),
 9 : ("li","|", "o", "|")
 }
try:
 return_trigram_name = trigram_number_table[trigram_number]
except:
 return_trigram_name = "m33"
return return_trigram_name

def trigram_name_to_number(trigram_name):
# FuXi, King Wen
trigram_name = x_util.bump_case(trigram_name)
trigram_name_table = {
 "qian" : (1, 6),
 "dui" : (2, 7),
 "li": (3, 9),
 "zhen" : (4, 3),
 "sun" : (5, 4),
 "kan" : (6, 1),
 "gen" : (7, 8),
 "kun" : (8, 2)
 }
try:
 return_trigram_number = trigram_name_table[trigram_name]
except:
 return_trigram_number = 0
return return_trigram_number

def decipher_trigram(line_one, line_two, line_three):
if line_one == "*":
 return_trigram = ("stardust", "*", "*", "*")
# print line_one, line_two, line_three
# print "stardust"
elif line_one == "o":
 if line_two == "o":
 if line_three == "o":
return_trigram = ("kun", "o", "o", "o")
 else:
return_trigram = ("gen", "o", "o", "|")
 else:
 if line_three == "o":
return_trigram = ("kan", "o", "|", "o")
 else:
return_trigram = ("sun", "o", "|", "|")
else:
 if line_two == "o":
 if line_three == "o":
return_trigram = ("zhen", "|", "o", "o")
 else:
return_trigram = ("li","|", "o", "|")
 else:
 if line_three == "o":
return_trigram = ("dui", "|", "|", "o")
 else:
return_trigram = ("qian", "|", "|", "|")
return return_trigram

def golden_trigram(hexagram_lines):
check_line = h_util.reduce_bigram(hexagram_lines[1], hexagram_lines[2])
line_one = h_util.moving_line_to_symbol (check_line)
check_line = h_util.reduce_bigram(hexagram_lines[3], hexagram_lines[4])
line_two = h_util.moving_line_to_symbol (check_line)
check_line = h_util.reduce_bigram(hexagram_lines[5], hexagram_lines[6])
line_three = h_util.moving_line_to_symbol (check_line)
return_trigram = decipher_trigram(line_one, line_two, line_three)
print return_trigram, "at golden_trigram "
return return_trigram

def hexagram_family(hex_number):
if hex_number in (1, 44, 33, 12, 20, 23, 35, 14):
 return_trigram = "qian"
elif hex_number in (29, 60, 3, 63, 49, 55, 36, 7):
 return_trigram = "kan"
elif hex_number in (52, 22, 26, 41, 38, 10, 61, 53):
 return_trigram = "gen"
elif hex_number in (51, 16, 40, 32, 46, 48, 28, 17):
return_trigram = "zhen"
elif hex_number in (57, 9, 37, 42, 25, 21, 27, 18):
 return_trigram = "sun"
elif hex_number in (30, 56, 50, 64, 4, 59, 6, 13):
 return_trigram = "li"
elif hex_number in (2, 24, 19, 11, 34, 43, 5, 8):
 return_trigram = "kun"
elif hex_number in (58, 47, 45, 31, 39, 15, 62, 54):
 return_trigram = "dui"
else:
 return_trigram = "antares"
# print hex_number, " is where ANTARES was found"
# print "antares"
print return_trigram, " from hexagram_family"
return return_trigram

def trigrams_in_hexagram(hexagram_lines, trigram_type):
#print hexagram_lines
line_six =hexagram_lines[6]
line_five = hexagram_lines[5]
line_four = hexagram_lines[4]
line_three = hexagram_lines[3]
line_two =hexagram_lines[2]
line_one =hexagram_lines[1]
trigram_type_table = {
"c6" : (0, line_one, line_two, line_three),
"c5" : (0, line_two, line_three, line_four),
"c4" : (0, line_three, line_four, line_five),
"c3" : (0, line_four, line_five, line_six),
"i6" : (0, line_one, line_two, line_three),
"i5" : (0, line_two, line_three, line_four),
"upper" : (0, line_one, line_two, line_three),
"lower" : (0, line_four, line_five, line_six)
 }
try:
 return_trigram_lines = trigram_type_table[trigram_type]
except:
 return_trigram_lines = ("horsehead", "*","*","*")
line_one = return_trigram_lines[1]
line_two = return_trigram_lines[2]
line_three = return_trigram_lines[3]
new_trigram = decipher_trigram(line_one, line_two, line_three)
return new_trigram

 This is the Feng Shui Sequence ##

def feng_shui_sequence(trigram_lines, feng_shei_sequence_number):
line_one = trigram_lines[1]
line_two = trigram_lines[2]
line_three = trigram_lines[3]
if feng_shei_sequence_number == 1:
 line_one = h_util.reverse_line(line_one)
elif feng_shei_sequence_number == 2:
 line_one = h_util.reverse_line(line_one)
 line_two = h_util.reverse_line(line_two)
 line_three = h_util.reverse_line(line_three)
elif feng_shei_sequence_number == 3:
 line_two = h_util.reverse_line(line_two)
 line_three = h_util.reverse_line(line_three)
elif feng_shei_sequence_number == 4:
 time.sleep(4)
# print "Feng Shui Sequence : The Original Trigram"
elif feng_shei_sequence_number == 5:
 line_three = h_util.reverse_line(line_three)
elif feng_shei_sequence_number == 6:
 line_one = h_util.reverse_line(line_one)
 line_three = h_util.reverse_line(line_three)
elif feng_shei_sequence_number == 7:
 line_one = h_util.reverse_line(line_one)
 line_two = h_util.reverse_line(line_two)
elif feng_shei_sequence_number == 8:
 line_two = h_util.reverse_line(line_two)
else:
 print "invalid Feng Shui Sequence Number"
new_trigram = decipher_trigram(line_one, line_two, line_three)
return new_trigram

#
# 1:Sheng Qi:Prosperity
# 2:Yan Nian:Longevity
# 3:Tian Yi: Health
# 4:Fu Wei: Peace
# 5:Huo Hal: Accidents
# 6:Liu Sha: Malicious Encounters
# 7:Wu Gui: Litigation
# 8:Jus Ming:Disease
#

print " t_util module is loaded "
