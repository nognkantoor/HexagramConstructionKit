s_util.py : Stem and Branch Routines

#!/usr/bin/python
import sys
sys.path.insert (0, '/usr/local/lib/python-1.5/lib')
# remember to delete the above line when changing operating systems
#
# YiJing Construction Program
#
# Initialization routines for stems and branches

# Licence Terms: GNU General Public Licence

# Module History
#
# 5 February 2002
#
# Segregated out of hexagram.py
#

import string, x_util, t_util, h_util

# Stem Functions are below this line

def hexagram_stems(hexagram_lines):
#print "At hexagram stems"
#print hexagram_lines
upper = t_util.trigrams_in_hexagram(hexagram_lines, "upper")
lower = t_util.trigrams_in_hexagram(hexagram_lines, "lower")
lower = lower[0]
upper = upper[0]
#print lower, upper, " is lower and upper stem "
lower_stem_table = {
"kun" : ("gui"),
"dui" : ("ding"),
"li": ("xin"),
"sun" : ("ji"),
"qian" : ("ren"),
"gen" : ("bing"),
"kan" : ("wu"),
"zhen" : ("geng")
 }
try:
 lower_stem = lower_stem_table[lower]
except:
 lower_stem = "andromeda"
upper_stem_table = {
"kun" : ("yi"),
"dui" : ("ding"),
"li": ("xin"),
"sun" : ("ji"),
"qian" : ("jia"),
"gen" : ("bing"),
"kan" : ("wu"),
"zhen" : ("geng")
 }
try:
 upper_stem = upper_stem_table[upper]
except:
 upper_stem = "magellen"
#print lower_stem, upper_stem
return lower_stem, upper_stem

def stem_name_to_stem_number (stem_name):
stem_name = x_util.bump_case(stem_name)
stem_table = {
 "wu": (1),
 "yi": (2),
 "ren" : (2),
 "geng" : (3),
 "xin" : (4),
 "quei" : (5),
 "jia" : (6),
 "ding" : (7),
 "bing" : (8),
 "ji": (9),
 }
try:
 stem_number = stem_table[stem_name]
except:
 stem_number = 0
return stem_number

def stem_number_to_stem_name (stem_number):
stem_table = {
 1 : ("wu"),
 2 : ("ren"),
 2 : ("yi"),
 3 : ("geng"),
 4 : ("xin"),
 6 : ("jia"),
 7 : ("ding"),
 8 : ("bing"),
 9 : ("ji"),
 }
try:
 stem_name = stem_table[stem_number]
except:
 stem_name = sagitarius
return stem_name

# Branch Functions are below this line

def hexagram_branches(hexagram_lines):
hexagram_number = h_util.get_hexagram_number(hexagram_lines)
family = t_util.hexagram_family(hexagram_number)
branch_table = {
"kun" : ("wei", "si","mao", "chou", "hai", "you"),
"dui" : ("si","mao", "chou", "hai", "you", "wei"),
"li": ("mao", "chou", "hai", "you", "wei", "si"),
"sun" : ("chou", "hai", "you", "wei", "si","mao"),
"qian" : ("zi","yin", "chen", "wu","shen", "xu"),
"gen" : ("chen", "wu","shen", "xu","zi","yin"),
"kan" : ("yin", "chen", "wu","shen", "xu","zi"),
"zhen" : ("zi","yin", "chen", "wu","shen", "xu"),
}
try:
 branch = branch_table[family]
except:
 branch = "aldeberan"
#print branch
return branch

def branch_name_to_branch_number (branch_name):
branch_name = x_util.bump_case(branch_name)
branch_table = {
 "zi": (1, 6),
 "chou" : (5, 10),
 "yin" : (3, 8),
 "mao" : (3, 8),
 "chen" : (5, 10),
 "si": (2, 7),
 "wu": (2, 7),
 "wei" : (5, 10),
 "shen" : (4, 9),
 "you" : (4, 9),
 "xu": (5, 10),
 "hai" : (1, 6),
 }
try:
 branch_number = branch_table[branch_name]
except:
 branch_number = 0
return branch_number
#
# yin, then yang number
#
def branch_number_to_branch_name(branch_number):
branch_table = {
 1 : ("hai","yin"),
 1 : ("zi","yang"),
 2 : ("si","yin"),
 2 : ("wu","yang"),
 3 : ("yin","yin"),
 3 : ("mao","yang"),
 4 : ("shen","yin"),
 4 : ("you","yang"),
 5 : ("chou","yin"),
 5 : ("chen","yang"),
 5 : ("wei","yin"),
 5 : ("xu","yang"),
 6 : ("hai","yin"),
 6 : ("zi","yang"),
 7 : ("si","yin"),
 7 : ("wu","yang"),
 8 : ("yin","yin"),
 8 : ("mao","yang"),
 9 : ("shen","yin"),
 9 : ("you","yang"),
 10 : ("chen","yin"),
 10 : ("wei","yang"),
 10 : ("xu","yin"),
 10 : ("chou","yang"),
 }
try:
 branch_name = branch_table[branch_number]
except:
 branch_name = ("polaris", "taiji")
return branch_name

print " s_util module loaded"
