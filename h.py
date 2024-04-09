#!/usr/bin/python
# h.py: Main program
import sys
sys.path.insert (0, '/usr/local/lib/python-1.5/lib')
# remember to delete the above line when changing operating systems
#
# YiJing Hexagram Construction Program
#
# This program deconstructs and reconstructs hexagrams
# based upon an initial hexagram.
#
# The hexagram can be either configured manually, or calculated
# according one of several different methods.	
#
# This is version 0.0.0.5
# Creation Date: 9 May 2001 @ 18:59 H GMT
# Last Update:8 February 2003 @ 1:34 GMT
# Copyright: 2001 - 2002 Jonathon Blake
# Licence Terms: GNU General Public Licence
#
#
# 8 February 2003
#
# Fixed various bugs I found.
#
# 7 September 2002
#
# Essentially rewrote the program, putting things into modules.
#
# Copyright Module was completed.
#
# Modules it uses are:
#
# x_util:general purpose utilities/routines
# h_util:hexagram routines
# t_util:trigram routines
# s_util:stem and branch routines
# p_util:phase routines
#
import string, copy_gnu, x_util, h_util, t_util, s_util, p_util, dis_util
check = 5
copy_gnu.show_pc(check, "YiJing Hexagram Construction Program", "0.0.0.5", "A program to deconstruct and reconstruct the hexagrams of the YiJing.", "2001 - 2002", "Licence: GNU GPL")
do_display = x_util.true_false("Display the GNU GPL and Python Licence? y/n")
copy_gnu.show_which(do_display, check)
# hexagram_string, trigram_string, stem_string, branch_string = dis_util.run_a_hexagram(check)
# print hexagram_string
for counter in range (65):
 check = counter
 hexagram_string, trigram_string, stem_string, branch_string = dis_util.run_a_hexagram(check)
