
h_util.py: Hexagram Utilities
#!/usr/bin/python
import sys
sys.path.insert (0, '/usr/local/lib/python-1.5/lib')
# remember to delete the above line when changing operating systems
#
# YiJing Hexagram Construction Program
#
# Initialization routines for hexagrams
#
# This module constructs and deconstructs hexagrams
# from lines, bigrams, trigrams, stems, branches
# dates and names.
#
# You need another module to actually display these routines.
#
# This is version 0.0.0.4
# Creation Date: 9 May 2001 @ 18:59 H GMT
# Last Update: 7 September 2002 @ 5:31 GMT
# Copyright: 2001 - 2002 Jonathon Blake
# Licence Terms: GNU General Public Licence

#
# Want / Need to add
#
#Hexagrams from Dates
#Nine Ki Star Astrology
#Plum Blossom Numerology
#
#
#
# YiJing Construction Program History
#
# 15 July 2001
#
# Added Stem and Branch functions
# Added Name functions
# Added Jin Fan 17 hexagram sequence
#
# 18 July 2001
#
# Deleted function lines_of_hexagram
#This function used to be used to load the hexagram lookup table into memory.
#When I eliminated that table, this function was no longer needed.
#
# 4 September 2001
#
# Corrected the evaluated hexagram function
# Added Crowley's Married Hexagram
# added the cxi6 & cxi5 series of hexagrams
# added the i6cx & i5cx series of hexagrams
#
# 4 February 2002
#
# Added the Feng Shui Sequence of hexagrams
#
# 5 February 2002
#
# Changed composition of trigram tupple
# [in specific, added name & lines)
#
# Segregated out trigram.py & stem.py
#
# 7 September 2002
#
# added Golden Trigram Sequences
#


import string, t_util, x_util

# utility.py contains the following

#
# other utilities
# file read / write functions
# Date Functions are below this line
#

def date_to_hexagram(day, month, year, era):
# source: http://homepage2.nifty.com/index_Z/meihua.html
# default is japanese era calendar
# add others as appropriate
era = x_util.bump_case(era)
if era == "japanese":
 starting_year = 660
elif era == "thelema":
 starting_year = - 1904
elif era in ["christian", "xian" ]:
 starting_year = 4
else:
starting_year = 660
month_number = month_to_number (month)
upper_trigram_number = year + month_number + starting_year
upper_trigram = trigram_number_to_name(upper_trigram_number)
lower_trigram = trigram_number_to_name(day)
moving_line = month_number + year + day
moving_line = moving_line % 6
hexagram_number = trigram_table(upper_trigram, lower_trigram)
return hexagram_number, upper_trigram, lower_trigram, moving_line

# Name Functions are below this line

def name_to_number(name_to_convert):
delta_name = x_util.bump_case(name_to_convert)
name_length = len(delta_name)
if name_length > 0:
 name_number = 0
 for counter in range(name_length):
 kounter = counter
 check_char = delta_name[kounter]
 gematria_table = {
 "a" : (1),
 "b" : (2),
 "c" : (3),
 "d" : (4),
 "e" : (5),
 "f" : (6),
 "g" : (7),
 "h" : (8),
 "i" : (9),
 "j" : (1),
 "k" : (2),
 "l" : (3),
 "m" : (4),
 "n" : (5),
 "o" : (6),
 "p" : (7),
 "q" : (8),
 "r" : (9),
 "s" : (1),
 "t" : (2),
 "u" : (3),
 "v" : (4),
 "w" : (5),
 "x" : (6),
 "y" : (7),
 "z" : (8),
 }
 try:
name_number = name_number + gematria_table[check_char]
 except:
name_number = name_number + 0
else:
 name_number = 0
return name_number

def name_to_trigram_number(name_to_convert):
trigram_data = name_to_number(name_to_convert)
trigram_number = trigram_data % 8
return trigram_number

def name_to_trigram_name(name_to_convert):
trigram_number = name_to_trigram_number (name_to_convert)
trigram_name = trigram_number_to_name (trigram_number)
return trigram_name

def names_to_line_number (forename, surname):
trigram_data_1 = name_to_number(forename)
trigram_data_2 = name_to_number(surname)
line_data = trigram_data_1 + trigram_data_2
line_number = line_data % 6
return line_number

def names_to_hex_number (forename, surname):
lower_trigram = name_to_trigram_number (forename)
upper_trigram = name_to_trigram_number (surname)
lower_trigram = trigram_number_to_name(lower_trigram)
upper_trigram = trigram_number_to_name(upper_trigram)
hex_number = trigram_table(upper_trigram, lower_trigram)
return hex_number

def obtain_names(checkpoint):
forename = read_input_data("Please type the first name", "The first name is ")
surname = read_input_data("Please type the last name", "The last name is ")
return forename, surname

def obtain_name_hexagram(checkpoint):
forename, surname = obtain_names (checkpoint)
hex_number = names_to_hex_number(forename, surname)
moving_line = names_to_line_number (forename, surname)
upper_trigram = name_to_trigram_name (surname)
lower_trigram = name_to_trigram_name (forename)
name_data = (hex_number, upper_trigram, lower_trigram, moving_line)
#print hex_number, upper_trigram, lower_trigram, moving_line
#print "H#, UT, LT, Moving Line"
return name_data

# Stem Functions are below this line
# Branch Functions are below this line

# bigram functions are below this line

def reduce_bigram(upper_line, lower_line):
if upper_line == "|":
 if lower_line == "o":
 return_bigram = "old yang"
 else:
 return_bigram = "young yang"
else:
 if lower_line == "o":
 return_bigram = "young yin"
 else:
 return_bigram = "old yin"
return return_bigram

def moving_line_to_symbol(moving_line):
#
# Not the operation overload.
#In most these I treat moving_line as a a string,
#but for some of them, moving_line is an integer.
#
# This operation overload is why I am not using
# if moving_line in ["old_yang", "young_yan" ]
#return_line = "|"
# etc
#
# I _think_ that any reasonable data thrown here, will result
# in the correct line being returned.
#
if moving_line == "old_yang":
 return_line = "|"
elif moving_line == "old_yin":
 return_line = "o"
elif moving_line == "young_yang":
 return_line = "|"
elif moving_line == "young_yin":
 return_line = "o"
elif moving_line == "old yang":
 return_line = "|"
elif moving_line == "old yin":
 return_line = "o"
elif moving_line == "young yang":
 return_line = "|"
elif moving_line == "young yin":
 return_line = "o"
elif moving_line == "yin":
 return_line = "o"
elif moving_line == "yang":
 return_line = "|"
elif moving_line == "|":
 return_line = "|"
elif moving_line == "o":
 return_line = "o"
elif moving_line == " | ":
 return_line = "|"
elif moving_line == " o ":
 return_line = "o"
elif moving_line == "| ":
 return_line = "|"
elif moving_line == "o ":
 return_line = "o"
elif moving_line == " |":
 return_line = "|"
elif moving_line == " o":
 return_line = "o"
elif moving_line == 9:
 return_line = "|"
elif moving_line == 8:
 return_line = "o"
elif moving_line == 7:
 return_line = "|"
elif moving_line == 6:
 return_line = "o"
elif moving_line == 3:
 return_line = "|"
elif moving_line == 2:
 return_line = "o"
else:
 return_line = "*"
 print moving_line, " was not listed in moving_line_to_symbol "
return return_line

 This is the Feng Shui Sequence ##

def feng_shei (hexagram_lines, feng_shui_this, put_on_this, feng_shui_sequence_number):
feng_shui_lines = t_util.trigrams_in_hexagram (hexagram_lines, feng_shui_this)
feng_shui_lines = t_util.feng_shui_sequence(feng_shui_lines, feng_shui_sequence_number)
base_trigram = t_util.trigrams_in_hexagram (hexagram_lines, put_on_this)
base_hexagram = trigram_lines_to_hexagram(feng_shui_lines, base_trigram)
top_hexagram = trigram_lines_to_hexagram(base_trigram, feng_shui_lines)
return base_hexagram, top_hexagram

# hexagram functions are below this line

def load_hexagram (hex_number):
print hex_number, " at load_hexagram "
if hex_number > 64:
 hex_number = hex_number - 64
 hex_number = load_hexagram (hex_number)
elif hex_number < 1:
 hex_number = hex_number + 64
 hex_number = load_hexagram (hex_number)
print hex_number, " at start of hexagram table "
hexagram_table = {
 0 : (0,"*", "*", "*", "*", "*", "*"),
 1 : (1,"|", "|", "|", "|", "|", "|"),
 2 : (2,"o", "o", "o", "o", "o", "o"),
 3 : (3,"|", "o", "o", "o", "|", "o"),
 4 : (4,"o", "|", "o", "o", "o", "|"),
 5 : (5,"|", "|", "|", "o", "|", "o"),
 6 : (6,"o", "|", "o", "|", "|", "|"),
 7 : (7,"o", "|", "o", "o", "o", "o"),
 8 : (8,"o", "o", "o", "o", "|", "o"),
 9 : (9,"|", "|", "|", "o", "|", "|"),
 10 : (10,"|", "|", "o", "|", "|", "|"),
 11 : (11,"|", "|", "|", "o", "o", "o"),
 12 : (12,"o", "o", "o", "|", "|", "|"),
 13 : (13,"|", "o", "|", "|", "|", "|"),
 14 : (14,"|", "|", "|", "|", "o", "|"),
 15 : (15,"o", "o", "|", "o", "o", "o"),
 16 : (16,"o", "o", "o", "|", "o", "o"),
 17 : (17,"|", "o", "o", "|", "|", "o"),
 18 : (18,"o", "|", "|", "o", "o", "|"),
 19 : (19,"|", "|", "o", "o", "o", "o"),
 20 : (20,"o", "o", "o", "o", "|", "|"),
 21 : (21,"|", "o", "o", "|", "o", "|"),
 22 : (22,"|", "o", "|", "o", "o", "|"),
 23 : (23,"o", "o", "o", "o", "o", "|"),
 24 : (24,"|", "o", "o", "o", "o", "o"),
 25 : (25,"|", "o", "o", "|", "|", "|"),
 26 : (26,"|", "|", "|", "o", "o", "|"),
 27 : (27,"|", "o", "o", "o", "o", "|"),
 28 : (28,"o", "|", "|", "|", "|", "o"),
 29 : (29,"o", "|", "o", "o", "|", "o"),
 30 : (30,"|", "o", "|", "|", "o", "|"),
 31 : (31,"o", "o", "|", "|", "|", "o"),
 32 : (32,"o", "|", "|", "|", "o", "o"),
 33 : (33,"o", "o", "|", "|", "|", "|"),
 34 : (34,"|", "|", "|", "|", "o", "o"),
 35 : (35,"o", "o", "o", "|", "o", "|"),
 36 : (36,"|", "o", "|", "o", "o", "o"),
 37 : (37,"|", "o", "|", "o", "|", "|"),
 38 : (38,"|", "|", "o", "|", "o", "|"),
 39 : (39,"o", "o", "|", "o", "|", "o"),
 40 : (40,"o", "|", "o", "|", "o", "o"),
 41 : (41,"|", "|", "o", "o", "o", "|"),
 42 : (42,"|", "o", "o", "o", "|", "|"),
 43 : (43,"|", "|", "|", "|", "|", "o"),
 44 : (44,"o", "|", "|", "|", "|", "|"),
 45 : (45,"o", "o", "o", "|", "|", "o"),
 46 : (46,"o", "|", "|", "o", "o", "o"),
 47 : (47,"o", "|", "o", "|", "|", "o"),
 48 : (48,"o", "|", "|", "o", "|", "o"),
 49 : (49,"|", "o", "|", "|", "|", "o"),
 50 : (50,"o", "|", "|", "|", "o", "|"),
 51 : (51,"|", "o", "o", "|", "o", "o"),
 52 : (52,"o", "o", "|", "o", "o", "|"),
 53 : (53,"o", "o", "|", "o", "|", "|"),
 54 : (54,"|", "|", "o", "|", "o", "o"),
 55 : (55,"|", "o", "|", "|", "o", "o"),
 56 : (56,"o", "o", "|", "|", "o", "|"),
 58 : (58,"|", "|", "o", "|", "|", "o"),
 57 : (57,"o", "|", "|", "o", "|", "|"),
 59 : (59,"o", "|", "o", "o", "|", "|"),
 60 : (60,"|", "|", "o", "o", "|", "o"),
 61 : (61,"|", "|", "o", "o", "|", "|"),
 62 : (62,"o", "o", "|", "|", "o", "o"),
 63 : (63,"|", "o", "|", "o", "|", "o"),
 64 : (64,"o", "|", "o", "|", "o", "|"),
 65 : (65, " line 1 ", " line 2 ", " line 3 ", " line 4 ", " line 5 ", " line 6 ")
 }
try:
 print "Hexagram # ", hex_number, " was located"
 return_hexagram_lines = hexagram_table[hex_number]
except:
 return_hexagram_lines = (66, "*","*","*","*","*","*")
 print hex_number, " was not found in hexagram_table / load_hexagram "
return return_hexagram_lines

def t_kun(lower_trigram):
if lower_trigram[0] == "kun":
 hexagram_number = 2
elif lower_trigram[0] == "gen":
 hexagram_number = 15
elif lower_trigram[0] == "kan":
 hexagram_number = 7
elif lower_trigram[0] == "sun":
 hexagram_number = 46
elif lower_trigram[0] == "zhen":
 hexagram_number = 24
elif lower_trigram[0] == "li":
 hexagram_number = 36
elif lower_trigram[0] == "dui":
 hexagram_number = 19
elif lower_trigram[0] == "qian":
 hexagram_number = 11
else:
 hexagram_number = 70
return hexagram_number

def t_qian(lower_trigram):
if lower_trigram[0] == "kun":
 hexagram_number = 12
elif lower_trigram[0] == "gen":
 hexagram_number = 33
elif lower_trigram[0] == "kan":
 hexagram_number = 6
elif lower_trigram[0] == "sun":
 hexagram_number = 44
elif lower_trigram[0] == "zhen":
 hexagram_number = 25
elif lower_trigram[0] == "li":
 hexagram_number = 13
elif lower_trigram[0] == "dui":
 hexagram_number = 10
elif lower_trigram[0] == "qian":
 hexagram_number = 1
else:
 hexagram_number = 71
return hexagram_number

def t_dui(lower_trigram):
if lower_trigram[0] == "kun":
 hexagram_number = 45
elif lower_trigram[0] == "gen":
 hexagram_number = 31
elif lower_trigram[0] == "kan":
 hexagram_number = 47
elif lower_trigram[0] == "sun":
 hexagram_number = 28
elif lower_trigram[0] == "zhen":
 hexagram_number = 17
elif lower_trigram[0] == "li":
 hexagram_number = 49
elif lower_trigram[0] == "dui":
 hexagram_number = 58
elif lower_trigram[0] == "qian":
 hexagram_number = 43
else:
 hexagram_number = 72
return hexagram_number

def t_li(lower_trigram):
if lower_trigram[0] == "kun":
 hexagram_number = 35
elif lower_trigram[0] == "gen":
 hexagram_number = 56
elif lower_trigram[0] == "kan":
 hexagram_number = 64
elif lower_trigram[0] == "sun":
 hexagram_number = 50
elif lower_trigram[0] == "zhen":
 hexagram_number = 21
elif lower_trigram[0] == "li":
 hexagram_number = 30
elif lower_trigram[0] == "dui":
 hexagram_number = 38
elif lower_trigram[0] == "qian":
 hexagram_number = 14
else:
 hexagram_number = 73
return hexagram_number

def t_zhen(lower_trigram):
if lower_trigram[0] == "kun":
 hexagram_number = 16
elif lower_trigram[0] == "gen":
 hexagram_number = 62
elif lower_trigram[0] == "kan":
 hexagram_number = 40
elif lower_trigram[0] == "sun":
 hexagram_number = 32
elif lower_trigram[0] == "zhen":
 hexagram_number = 51
elif lower_trigram[0] == "li":
 hexagram_number = 55
elif lower_trigram[0] == "dui":
 hexagram_number = 54
elif lower_trigram[0] == "qian":
 hexagram_number = 34
else:
 hexagram_number = 74
return hexagram_number

def t_sun(lower_trigram):
if lower_trigram[0] == "kun":
 hexagram_number = 20
elif lower_trigram[0] == "gen":
 hexagram_number = 53
elif lower_trigram[0] == "kan":
 hexagram_number = 59
elif lower_trigram[0] == "sun":
 hexagram_number = 57
elif lower_trigram[0] == "zhen":
 hexagram_number = 42
elif lower_trigram[0] == "li":
 hexagram_number = 37
elif lower_trigram[0] == "dui":
 hexagram_number = 61
elif lower_trigram[0] == "qian":
 hexagram_number = 9
else:
 hexagram_number = 75
return hexagram_number

def t_kan(lower_trigram):
if lower_trigram[0] == "kun":
 hexagram_number = 8
elif lower_trigram[0] == "gen":
 hexagram_number = 39
elif lower_trigram[0] == "kan":
 hexagram_number = 29
elif lower_trigram[0] == "sun":
 hexagram_number = 48
elif lower_trigram[0] == "zhen":
 hexagram_number = 3
elif lower_trigram[0] == "li":
 hexagram_number = 63
elif lower_trigram[0] == "dui":
 hexagram_number = 60
elif lower_trigram[0] == "qian":
 hexagram_number = 5
else:
 hexagram_number = 76
return hexagram_number

def t_gen(lower_trigram):
if lower_trigram[0] == "kun":
 hexagram_number = 23
elif lower_trigram[0] == "gen":
 hexagram_number = 52
elif lower_trigram[0] == "kan":
 hexagram_number = 4
elif lower_trigram[0] == "sun":
 hexagram_number = 18
elif lower_trigram[0] == "zhen":
 hexagram_number = 27
elif lower_trigram[0] == "li":
 hexagram_number = 22
elif lower_trigram[0] == "dui":
 hexagram_number = 41
elif lower_trigram[0] == "qian":
 hexagram_number = 26
else:
 hexagram_number = 77
return hexagram_number

def trigram_table(upper_trigram, lower_trigram):
if upper_trigram[0] == "kun":
 hexagram_number = t_kun(lower_trigram)
elif upper_trigram[0] == "gen":
 hexagram_number = t_gen(lower_trigram)
elif upper_trigram[0] == "kan":
 hexagram_number = t_kan(lower_trigram)
elif upper_trigram[0] == "sun":
 hexagram_number = t_sun(lower_trigram)
elif upper_trigram[0] == "zhen":
 hexagram_number = t_zhen(lower_trigram)
elif upper_trigram[0] == "li":
 hexagram_number = t_li(lower_trigram)
elif upper_trigram[0] == "dui":
 hexagram_number = t_dui(lower_trigram)
elif upper_trigram[0] == "qian":
 hexagram_number = t_qian(lower_trigram)
elif upper_trigram[0] == "stardust":
 hexagram_number = 79
elif upper_trigram[0] == "antares":
 hexagram_number = 77
else:
 hexagram_number = 78
return hexagram_number

def get_hexagram_number(hexagram_lines):
upper_trigram = t_util.trigrams_in_hexagram(hexagram_lines, "upper")
lower_trigram = t_util.trigrams_in_hexagram(hexagram_lines, "lower")
hexagram_number = trigram_table(upper_trigram, lower_trigram)
return hexagram_number

def decipher_hexagram(hexagram_lines):
line_1 = hexagram_lines[1]
line_2 = hexagram_lines[2]
line_3 = hexagram_lines[3]
line_4 = hexagram_lines[4]
line_5 = hexagram_lines[5]
line_6 = hexagram_lines[6]
hex_number = get_hexagram_number(hexagram_lines)
return_hexagram = (hex_number, line_1, line_2, line_3, line_4, line_5, line_6)
return return_hexagram

def trigram_lines_to_hexagram(upper_trigram_lines, lower_trigram_lines):
#print lower_trigram_lines
#print upper_trigram_lines
line_one = upper_trigram_lines[0]
line_two = upper_trigram_lines[1]
line_three = upper_trigram_lines[2]
line_four = lower_trigram_lines[0]
line_five = lower_trigram_lines[1]
line_six = lower_trigram_lines[2]
hexagram_lines = (0, line_one, line_two, line_three, line_four, line_five, line_six)
return_hexagram = decipher_hexagram(hexagram_lines)
return return_hexagram

def inverse_hexagram(hexagram_lines):
new_lines = (0, hexagram_lines[6], hexagram_lines[5], hexagram_lines[4], hexagram_lines[3], hexagram_lines[2], hexagram_lines[1])
new_hexagram = decipher_hexagram(new_lines)
return new_hexagram

def reverse_line(hexagram_line):
if hexagram_line == "|":
 new_line = "o"
elif hexagram_line == "o":
 new_line = "|"
else:
 new_line = "x"
return new_line

def reverse_hexagram(hexagram_lines):
new_line_1 = reverse_line(hexagram_lines[1])
new_line_2 = reverse_line(hexagram_lines[2])
new_line_3 = reverse_line(hexagram_lines[3])
new_line_4 = reverse_line(hexagram_lines[4])
new_line_5 = reverse_line(hexagram_lines[5])
new_line_6 = reverse_line(hexagram_lines[6])
new_lines = (0, new_line_1,new_line_2,new_line_3,new_line_4,new_line_5,new_line_6)
new_hexagram = decipher_hexagram(new_lines)
return new_hexagram

def nuclear_hexagram(hexagram_lines):
new_lines = (0, hexagram_lines[2], hexagram_lines[3],hexagram_lines[4], hexagram_lines[3],hexagram_lines[4],hexagram_lines[5])
new_hexagram = decipher_hexagram(new_lines)
return new_hexagram

def golden_hexagram(hexagram_lines):
new_lines = (0, hexagram_lines[3], hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram(new_lines)
return new_hexagram

def interlaced_hexagram(hexagram_lines):
new_lines = (0, hexagram_lines[1], hexagram_lines[3], hexagram_lines[5], hexagram_lines[2], hexagram_lines[4], hexagram_lines[6])
new_hexagram = decipher_hexagram(new_lines)
return new_hexagram

def married_hexagram(hexagram_lines):
new_lines = (0, hexagram_lines[2], hexagram_lines[4], hexagram_lines[6], hexagram_lines[1], hexagram_lines[3], hexagram_lines[5])
new_hexagram = decipher_hexagram(new_lines)
return new_hexagram

def evolved_hexagram(hexagram_lines):
line_one = hexagram_lines[1]
line_two = hexagram_lines[2]
line_three = hexagram_lines[3]
line_four = hexagram_lines[4]
line_five = hexagram_lines[5]
line_six = reverse_line(hexagram_lines[6])
new_lines = (0, line_six, line_one, line_two, line_three, line_four, line_five)
new_hexagram = decipher_hexagram (new_lines)
return new_hexagram

def axillary_hexagram (hexagram_lines, line_number):
line_one = hexagram_lines[1]
line_two = hexagram_lines[2]
line_three = hexagram_lines[3]
line_four = hexagram_lines[4]
line_five = hexagram_lines[5]
line_six = hexagram_lines[6]
if line_number == 1:
 line_one = reverse_line(line_one)
elif line_number == 2:
 line_two = reverse_line(line_two)
elif line_number == 3:
 line_three = reverse_line(line_three)
elif line_number == 4:
 line_four = reverse_line(line_four)
elif line_number == 5:
 line_five = reverse_line(line_five)
elif line_number == 6:
 line_six = reverse_line(line_six)
new_lines = (0, line_one, line_two, line_three, line_four, line_five, line_six)
new_hexagram = decipher_hexagram (new_lines)
return new_hexagram

def wen_next_hexagram(hex_number):
hex_number = hex_number + 1
if hex_number == "65":
 hex_number = "1"
new_hexagram = load_hexagram(hex_number)
return new_hexagram

def wen_prior_hexagram(hex_number):
hex_number = hex_number - 1
if hex_number == "0":
 hex_number = "64"
new_hexagram = load_hexagram(hex_number)
return new_hexagram

def fuxi_prior_hexagram(hex_number):
#print hex_number, " is fuxi_prior_hexagram at the begining "
check_hexagram = convert_to_fuxi_sequence(hex_number)
fuxi_number = check_hexagram[0]
fuxi_number = fuxi_number - 1
#print fuxi_number, " is the coverted fuxi hexagram number "
check_hexagram = convert_from_fuxi_sequence(fuxi_number)
#print check_hexagram, " is fuxi_prior_hexagram "
return check_hexagram

def fuxi_next_hexagram(hex_number):
check_hexagram = convert_to_fuxi_sequence(hex_number)
fuxi_number = check_hexagram[0]
fuxi_number = fuxi_number + 1
check_hexagram = convert_from_fuxi_sequence(fuxi_number)
return check_hexagram

def convert_from_fuxi_sequence(hex_number):
#fuxi sequence : king wen arrangement
#print hex_number, " is the fuxi sequence number "
if hex_number > 64:
 hex_number = hex_number - 64
 hex_number = convert_from_fuxi_sequence(hex_number)
elif hex_number < 1:
 hex_number = hex_number + 64
 hex_number = convert_from_fuxi_sequence(hex_number)
hexagram_table = {
 1 : 2,
 2 : 23,
 3 : 8,
 4 : 20,
 5 : 16,
 6 : 35,
 7 : 45,
 8 : 12,
 9 : 15,
 10 : 52,
 11 : 39,
 12 : 53,
 13 : 62,
 14 : 56,
 15 : 31,
 16 : 33,
 17 : 7,
 18 : 4,
 19 : 29,
 20 : 59,
 21 : 40,
 22 : 64,
 23 : 47,
 24 : 6,
 25 : 46,
 26 : 18,
 27 : 48,
 28 : 57,
 29 : 32,
 30 : 50,
 31 : 28,
 32 : 44,
 33 : 24,
 34 : 27,
 35 : 3,
 36 : 42,
 37 : 51,
 38 : 21,
 39 : 17,
 40 : 25,
 41 : 36,
 42 : 22,
 43 : 63,
 44 : 37,
 45 : 55,
 46 : 30,
 47 : 49,
 48 : 13,
 49 : 19,
 50 : 41,
 51 : 60,
 52 : 61,
 53 : 54,
 54 : 38,
 55 : 58,
 56 : 10,
 57 : 11,
 58 : 26,
 59 : 5,
 60 : 9,
 61 : 34,
 62 : 14,
 63 : 43,
 64 : 1
}
try:
 new_hexagram = hexagram_table[hex_number]
except:
 new_hexagram = 70
#print new_hexagram, " is the new_hexagram number "
return_hexagram = load_hexagram(new_hexagram)
#print return_hexagram
return return_hexagram

def convert_to_fuxi_sequence(hex_number):
# king wen arrangement : fuxi arrangement
if hex_number > 64:
 hex_number = hex_number - 64
 hex_number = convert_to_fuxi_sequence(hex_number)
elif hex_number < 1:
 hex_number = hex_number + 64
 hex_number = convert_to_fuxi_sequence(hex_number)
hexagram_table = {
 2 : 1,
23 : 2,
 8 : 3,
20 : 4,
16 : 5,
35 : 6,
45 : 7,
12 : 8,
15 : 9,
52 : 10,
39 : 11,
53 : 12,
62 : 13,
56 : 14,
31 : 15,
33 : 16,
 7 : 17,
 4 : 18,
29 : 19,
59 : 20,
40 : 21,
64 : 22,
47 : 23,
 6 : 24,
46 : 25,
18 : 26,
48 : 27,
57 : 28,
32 : 29,
50 : 30,
28 : 31,
44 : 32,
24 : 33,
27 : 34,
 3 : 35,
42 : 36,
51 : 37,
21 : 38,
17 : 39,
25 : 40,
36 : 41,
22 : 42,
63 : 43,
37 : 44,
55 : 45,
30 : 46,
49 : 47,
13 : 48,
19 : 49,
41 : 50,
60 : 51,
61 : 52,
54 : 53,
38 : 54,
58 : 55,
10 : 56,
11 : 57,
26 : 58,
 5 : 59,
 9 : 60,
34 : 61,
14 : 62,
43 : 63,
 1 : 64
 }
try:
 new_hexagram = hexagram_table[hex_number]
except:
 new_hexagram = 70
return_hexagram = load_hexagram(new_hexagram)
return return_hexagram

def mawangdui_prior_hexagram(hex_number):
check_hexagram = convert_to_mawangdui_sequence(hex_number)
mawangdui_number = check_hexagram[0]
mawangdui_number = mawangdui_number - 1
check_hexagram = convert_from_mawangdui_sequence(mawangdui_number)
return check_hexagram

def mawangdui_next_hexagram(hex_number):
check_hexagram = convert_to_mawangdui_sequence(hex_number)
mawangdui_number = check_hexagram[0]
mawangdui_number = mawangdui_number + 1
check_hexagram = convert_from_mawangdui_sequence(mawangdui_number)
return check_hexagram

def convert_to_mawangdui_sequence(hex_number):
# king wen sequence : mawangdui sequence
if hex_number > 64:
 hex_number = hex_number - 64
 hex_number = convert_to_mawangdui_sequence(hex_number)
elif hex_number < 1:
 hex_number = hex_number + 64
 hex_number = convert_to_mawangdui_sequence(hex_number)
hexagram_table = {
 1 : 1,
 12 : 2,
 33 : 3,
 10 : 4,
 6 : 5,
 13 : 6,
 25 : 7,
 44 : 8,
 52 : 9,
 26 : 10,
 23 : 11,
 41 : 12,
 4 : 13,
 22 : 14,
 27 : 15,
 18 : 16,
 29 : 17,
 5 : 18,
 8 : 19,
 39 : 20,
 60 : 21,
 63 : 22,
 3 : 23,
 48 : 24,
 51 : 25,
 34 : 26,
 16 : 27,
 62 : 28,
 54 : 29,
 40 : 30,
 55 : 31,
 32 : 32,
 2 : 33,
 11 : 34,
 15 : 35,
 19 : 36,
 7 : 37,
 36 : 38,
 24 : 39,
 46 : 40,
 58 : 41,
 43 : 42,
 45 : 43,
 31 : 44,
 47 : 45,
 49 : 46,
 17 : 47,
 28 : 48,
 30 : 49,
 14 : 50,
 35 : 51,
 56 : 52,
 38 : 53,
 64 : 54,
 21 : 55,
 50 : 56,
 57 : 57,
 9 : 58,
 20 : 59,
 53 : 60,
 61 : 61,
 59 : 62,
 37 : 63,
 42 : 64,
 1 : 1
 }
try:
 new_hexagram = hexagram_table[hex_number]
except:
 new_hexagram = 70
return_hexagram = load_hexagram(new_hexagram)
return return_hexagram

def convert_from_mawangdui_sequence(hex_number):
# mawangui_sequence : king wen sequence
if hex_number > 64:
 hex_number = hex_number - 64
 hex_number = convert_from_mawangdui_sequence(hex_number)
elif hex_number < 1:
 hex_number = hex_number + 64
 hex_number = convert_from_mawangdui_sequence(hex_number)
hexagram_table = {
 1 : 1,
 2 : 12,
 3 : 33,
 4 : 10,
 5 : 6,
 6 : 13,
 7 : 25,
 8 : 44,
 9 : 52,
10 : 26,
11 : 23,
12 : 41,
13 : 4,
14 : 22,
15 : 27,
16 : 18,
17 : 29,
18 : 5,
19 : 8,
20 : 39,
21 : 60,
22 : 63,
23 : 3,
24 : 48,
25 : 51,
26 : 34,
27 : 16,
28 : 62,
29 : 54,
30 : 40,
31 : 55,
32 : 32,
33 : 2,
34 : 11,
35 : 15,
36 : 19,
37 : 7,
38 : 36,
39 : 24,
40 : 46,
41 : 58,
42 : 43,
43 : 45,
44 : 31,
45 : 47,
46 : 49,
47 : 17,
48 : 28,
49 : 30,
50 : 14,
51 : 35,
52 : 56,
53 : 38,
54 : 64,
55 : 21,
56 : 50,
57 : 57,
58 : 9,
59 : 20,
60 : 53,
61 : 61,
62 : 59,
63 : 37,
64 : 42,
 1 : 1
 }
try:
 new_hexagram = hexagram_table[hex_number]
except:
 new_hexagram = 70
return_hexagram = load_hexagram(new_hexagram)
return return_hexagram

def convert_from_base_trigram_sequence(hex_number):
# base_trigram_sequence : king wen sequence
if hex_number > 64:
 hex_number = hex_number - 64
elif hex_number < 1:
 hex_number = hex_number + 64
hexagram_table = {
 1 : 1,
 2 : 44,
 3 : 13,
 4 : 33,
 5 : 10,
 6 : 6,
 7 : 25,
 8 : 12,
 9 : 9,
10 : 57,
11 : 37,
12 : 53,
13 : 61,
14 : 59,
15 : 42,
16 : 20,
17 : 14,
18 : 50,
19 : 30,
20 : 56,
21 : 38,
22 : 64,
23 : 21,
24 : 35,
25 : 26,
26 : 18,
27 : 22,
28 : 52,
29 : 41,
30 : 4,
31 : 27,
32 : 23,
33 : 43,
34 : 28,
35 : 49,
36 : 31,
37 : 58,
38 : 47,
39 : 17,
40 : 45,
41 : 5,
42 : 48,
43 : 63,
44 : 39,
45 : 60,
46 : 29,
47 : 3,
48 : 8,
49 : 34,
50 : 32,
51 : 55,
52 : 6,
53 : 54,
54 : 40,
55 : 51,
56 : 16,
57 : 11,
58 : 46,
59 : 36,
60 : 15,
61 : 19,
62 : 7,
63 : 24,
64 : 12
}
try:
 new_hexagram = hexagram_table[hex_number]
except:
 new_hexagram = 70
return_hexagram = load_hexagram(new_hexagram)
return return_hexagram

def convert_to_base_trigram_sequence(hex_number):
# king wen sequence : base_trigram_sequence
if hex_number > 64:
 hex_number = hex_number - 64
elif hex_number < 1:
 hex_number = hex_number + 64
hexagram_table = {
1 : 1,
 44 : 2,
 13 : 3,
 33 : 4,
 10 : 5,
6 : 6,
 25 : 7,
 12 : 8,
9 : 9,
 57 : 10,
 37 : 11,
 53 : 12,
 61 : 13,
 59 : 14,
 42 : 15,
 20 : 16,
 14 : 17,
 50 : 18,
 30 : 19,
 56 : 20,
 38 : 21,
 64 : 22,
 21 : 23,
 35 : 24,
 26 : 25,
 18 : 26,
 22 : 27,
 52 : 28,
 41 : 29,
4 : 30,
 27 : 31,
 23 : 32,
 43 : 33,
 28 : 34,
 49 : 35,
 31 : 36,
 58 : 37,
 47 : 38,
 17 : 39,
 45 : 40,
5 : 41,
 48 : 42,
 63 : 43,
 39 : 44,
 60 : 45,
 29 : 46,
3 : 47,
8 : 48,
 34 : 49,
 32 : 50,
 55 : 51,
6 : 52,
 54 : 53,
 40 : 54,
 51 : 55,
 16 : 56,
 11 : 57,
 46 : 58,
 36 : 59,
 15 : 60,
 19 : 61,
7 : 62,
 24 : 63,
 12 : 64
 }
try:
 new_hexagram = hexagram_table[hex_number]
except:
 new_hexagram = 70
return_hexagram = load_hexagram(new_hexagram)
return return_hexagram

def base_prior_hexagram(hex_number):
check_hexagram = convert_to_base_trigram_sequence(hex_number)
base_number = check_hexagram[0]
base_number = base_number - 1
check_hexagram = convert_from_base_trigram_sequence(base_number)
return check_hexagram

def base_next_hexagram(hex_number):
check_hexagram = convert_to_base_trigram_sequence(hex_number)
base_number = check_hexagram[0]
base_number = base_number + 1
check_hexagram = convert_from_base_trigram_sequence(base_number)
return check_hexagram

 The following hexagrams are derivatives that _might_ be useful 
#
# C : cast hexagram
# The number refers to the top line number of the trigram
# The first number refers to the upper trigram
# The second number refers to the lower trigram
#

def c6c3(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[2], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[6])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c6c4(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[3], hexagram_lines[4], hexagram_lines[4], hexagram_lines[5], hexagram_lines[6])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c6c5(hexagram_lines):
new_hexagram = (0, hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[4], hexagram_lines[5], hexagram_lines[6])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c6c6(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[5], hexagram_lines[6], hexagram_lines[4], hexagram_lines[5], hexagram_lines[6])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c5c6(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[5], hexagram_lines[6], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c5c5(hexagram_lines):
new_hexagram = (0, hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c5c4(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[3], hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c5c3(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[2], hexagram_lines[3], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c4c6(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[5], hexagram_lines[6], hexagram_lines[2], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c4c5(hexagram_lines):
new_hexagram = (0, hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[2], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c4c4(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[3], hexagram_lines[4], hexagram_lines[2], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c4c3(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[2], hexagram_lines[3], hexagram_lines[2], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c3c6(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[5], hexagram_lines[6], hexagram_lines[1], hexagram_lines[2], hexagram_lines[3])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c3c5(hexagram_lines):
new_hexagram = (0, hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[1], hexagram_lines[2], hexagram_lines[3])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c3c4(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[3], hexagram_lines[4], hexagram_lines[1], hexagram_lines[2], hexagram_lines[3])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c3c3(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[2], hexagram_lines[3], hexagram_lines[1], hexagram_lines[2], hexagram_lines[3])
new_hexagram = decipher_hexagram(new_hexagram)
return new_hexagram

def c6i6(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[5], hexagram_lines[6], hexagram_lines[2], hexagram_lines[4], hexagram_lines[6])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c5i6(hexagram_lines):
new_hexagram = (0, hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[2], hexagram_lines[4], hexagram_lines[6])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c4i6(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[3], hexagram_lines[4], hexagram_lines[2], hexagram_lines[4], hexagram_lines[6])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c3i6(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[2], hexagram_lines[3], hexagram_lines[2], hexagram_lines[4], hexagram_lines[6])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c6i5(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[5], hexagram_lines[6], hexagram_lines[1], hexagram_lines[3], hexagram_lines[5])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c5i5(hexagram_lines):
new_hexagram = (0, hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[1], hexagram_lines[3], hexagram_lines[5])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c4i5(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[3], hexagram_lines[4], hexagram_lines[1], hexagram_lines[3], hexagram_lines[5])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c3i5(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[2], hexagram_lines[3], hexagram_lines[1], hexagram_lines[3], hexagram_lines[5])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i6c6(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[4], hexagram_lines[6], hexagram_lines[4], hexagram_lines[5], hexagram_lines[6])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i6c5(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[4], hexagram_lines[6], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i6c4(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[4], hexagram_lines[6], hexagram_lines[2], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i6c3(hexagram_lines):
new_hexagram = (0, hexagram_lines[2], hexagram_lines[4], hexagram_lines[6], hexagram_lines[1], hexagram_lines[2], hexagram_lines[3])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i5c6(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[3], hexagram_lines[5], hexagram_lines[4], hexagram_lines[5], hexagram_lines[6])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i5c5(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[3], hexagram_lines[5], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i5c4(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[3], hexagram_lines[5], hexagram_lines[2], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i5c3(hexagram_lines):
new_hexagram = (0, hexagram_lines[1], hexagram_lines[3], hexagram_lines[5], hexagram_lines[1], hexagram_lines[2], hexagram_lines[3])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def gc6(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[6], hexagram_lines[5], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def gc5(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[4], hexagram_lines[3])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def gc4(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[4], hexagram_lines[3], hexagram_lines[2])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def gc3(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[3], hexagram_lines[2], hexagram_lines[1])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c6g(hexagram_lines):
new_hexagram = (0, hexagram_lines[6], hexagram_lines[5], hexagram_lines[4],hexagram_lines[4], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c5g(hexagram_lines):
new_hexagram = (0, hexagram_lines[5], hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c4g(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[3], hexagram_lines[2], hexagram_lines[4], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def c3g(hexagram_lines):
new_hexagram = (0, hexagram_lines[3], hexagram_lines[2], hexagram_lines[1], hexagram_lines[4], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def gi6(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[6], hexagram_lines[4], hexagram_lines[2])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def gi5(hexagram_lines):
new_hexagram = (0, hexagram_lines[4], hexagram_lines[3], hexagram_lines[4], hexagram_lines[5], hexagram_lines[3], hexagram_lines[1])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i6g(hexagram_lines):
new_hexagram = (0, hexagram_lines[6], hexagram_lines[4], hexagram_lines[2],hexagram_lines[4], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

def i5g(hexagram_lines):
new_hexagram = (0, hexagram_lines[5], hexagram_lines[3], hexagram_lines[1],hexagram_lines[4], hexagram_lines[3], hexagram_lines[4])
new_hexagram = decipher_hexagram (new_hexagram)
return new_hexagram

print " h_util.py module is loaded"
