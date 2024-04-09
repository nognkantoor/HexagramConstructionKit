
dis_util.py :Utilities of various kinds

#!/usr/bin/python
import sys
sys.path.insert (0, '/usr/local/lib/python-1.5/lib')
# remember to delete the above line when changing operating systems
#
# YiJing Hexagram Construction Program

#
# This module contains the routines that call the routines
# that deconstruct and reconstruct the hexagrams.
#
# This is version 0.0.0.1
# Creation Date: 7 September 2002 @ 6:24 GMT
# Last Update:7 September 2002 @ 6:24
# Copyright: 2002 Jonathon Blake
# Licence Terms: GNU General Public Licence
#
# 7 September 2002
#
# Segregated this out of the main program
#

import x_util, h_util, t_util, s_util

def display_all_hexagram_data(hexagram_lines):
#print "displaying data at display_all_data "

prefix_data = '<td><img src = "h_'
middle_data = '.png" alt = " '
end_data = ' " width = 45 height = 90 align = "center" border = 0 "></td>'

this_hexagram = hexagram_lines
hex_number = this_hexagram[0]
inverse = h_util.inverse_hexagram(this_hexagram)
reverse = h_util.reverse_hexagram(this_hexagram)
nuclear = h_util.nuclear_hexagram(this_hexagram)
golden = h_util.golden_hexagram(this_hexagram)
axillary_one = h_util.axillary_hexagram(this_hexagram, 1)
axillary_two = h_util.axillary_hexagram(this_hexagram, 2)
axillary_three = h_util.axillary_hexagram(this_hexagram, 3)
axillary_four = h_util.axillary_hexagram(this_hexagram, 4)
axillary_five = h_util.axillary_hexagram(this_hexagram, 5)
axillary_six = h_util.axillary_hexagram(this_hexagram, 6)
interlaced = h_util.interlaced_hexagram(this_hexagram)
married = h_util.married_hexagram(this_hexagram)
evolved = h_util.evolved_hexagram(this_hexagram)
wen_prior = h_util.wen_prior_hexagram(hex_number)
wen_next = h_util.wen_next_hexagram(hex_number)
mawangdui_prior = h_util.mawangdui_prior_hexagram(hex_number)
mawangdui_next = h_util.mawangdui_next_hexagram(hex_number)
fu_prior = h_util.fuxi_prior_hexagram(hex_number)
fu_next = h_util.fuxi_next_hexagram(hex_number)
base_prior = h_util.base_prior_hexagram(hex_number)
base_next = h_util.base_next_hexagram(hex_number)

#print this_hexagram[0], inverse[0], reverse[0], nuclear[0], golden[0], evolved[0], interlaced[0], married[0], axillary_one[0], axillary_two[0], axillary_three[0], axillary_four[0], axillary_five[0], axillary_six[0], wen_prior[0], wen_next[0], fu_prior[0], fu_next[0], mawangdui_prior[0], mawangdui_next[0], base_prior[0], base_next[0]
#print "H# In Re Nu Go Ev It MA A1 A2 A3 A4 A5 A6 WP WN FP FN MP MN BP BN "

string_hex_1 = (this_hexagram[0], inverse[0], reverse[0], nuclear[0], golden[0], evolved[0], interlaced[0], married[0], axillary_one[0], axillary_two[0], axillary_three[0], axillary_four[0], axillary_five[0], axillary_six[0], wen_prior[0], wen_next[0], fu_prior[0], fu_next[0], mawangdui_prior[0], mawangdui_next[0], base_prior[0], base_next[0])

c6c6_hexagram = h_util.c6c6(hexagram_lines)
c6c5_hexagram = h_util.c6c5(hexagram_lines)
c6c4_hexagram = h_util.c6c4(hexagram_lines)
c6c3_hexagram = h_util.c6c3(hexagram_lines)
c5c6_hexagram = h_util.c5c6(hexagram_lines)
c5c5_hexagram = h_util.c5c5(hexagram_lines)
c5c4_hexagram = h_util.c5c4(hexagram_lines)
c5c3_hexagram = h_util.c5c3(hexagram_lines)
c4c6_hexagram = h_util.c4c6(hexagram_lines)
c4c5_hexagram = h_util.c4c5(hexagram_lines)
c4c4_hexagram = h_util.c4c4(hexagram_lines)
c4c3_hexagram = h_util.c4c3(hexagram_lines)
c3c6_hexagram = h_util.c3c6(hexagram_lines)
c3c5_hexagram = h_util.c3c5(hexagram_lines)
c3c4_hexagram = h_util.c3c4(hexagram_lines)
c3c3_hexagram = h_util.c3c3(hexagram_lines)

 # print c6c6_hexagram[0], c6c5_hexagram[0], c6c5_hexagram[0], c6c4_hexagram[0], c6c3_hexagram[0], c5c6_hexagram[0], c5c5_hexagram[0], c5c4_hexagram[0], c5c3_hexagram[0], c4c6_hexagram[0], c4c5_hexagram[0], c4c4_hexagram[0], c4c3_hexagram[0], c3c6_hexagram[0], c3c5_hexagram[0], c3c4_hexagram[0], c3c3_hexagram[0]
 # print "66 65 64 63 56 55 54 53 46 45 44 43 36 35 34 33 "
string_hex_2 = (c6c6_hexagram[0], c6c5_hexagram[0], c6c4_hexagram[0], c6c3_hexagram[0], c5c6_hexagram[0], c5c5_hexagram[0], c5c4_hexagram[0], c5c3_hexagram[0], c4c6_hexagram[0], c4c5_hexagram[0], c4c4_hexagram[0], c4c3_hexagram[0], c3c6_hexagram[0], c3c5_hexagram[0], c3c4_hexagram[0], c3c3_hexagram[0])

c6i6_hexagram = h_util.c6i6(hexagram_lines)
c5i6_hexagram = h_util.c5i6(hexagram_lines)
c4i6_hexagram = h_util.c4i6(hexagram_lines)
c3i6_hexagram = h_util.c3i6(hexagram_lines)
c6i5_hexagram = h_util.c6i5(hexagram_lines)
c5i5_hexagram = h_util.c5i5(hexagram_lines)
c4i5_hexagram = h_util.c4i5(hexagram_lines)
c3i5_hexagram = h_util.c3i5(hexagram_lines)

i6c6_hexagram = h_util.i6c6(hexagram_lines)
i6c5_hexagram = h_util.i6c5(hexagram_lines)
i6c4_hexagram = h_util.i6c4(hexagram_lines)
i6c3_hexagram = h_util.i6c3(hexagram_lines)
i5c6_hexagram = h_util.i5c6(hexagram_lines)
i5c5_hexagram = h_util.i5c5(hexagram_lines)
i5c4_hexagram = h_util.i5c4(hexagram_lines)
i5c3_hexagram = h_util.i5c3(hexagram_lines)

string_hex_3 = (c6i6_hexagram[0], c5i6_hexagram[0], c4i6_hexagram[0], c3i6_hexagram[0], c6i5_hexagram[0], c5i5_hexagram[0], c4i5_hexagram[0], c3i5_hexagram[0], i6c6_hexagram[0], i6c5_hexagram[0], i6c4_hexagram[0], i6c3_hexagram[0], i5c6_hexagram[0], i5c5_hexagram[0], i5c4_hexagram[0], i5c3_hexagram[0])

gc6_hexagram = h_util.gc6(hexagram_lines)
gc5_hexagram = h_util.gc5(hexagram_lines)
gc4_hexagram = h_util.gc4(hexagram_lines)
gc3_hexagram = h_util.gc3(hexagram_lines)
c6g_hexagram = h_util.c6g(hexagram_lines)
c5g_hexagram = h_util.c5g(hexagram_lines)
c4g_hexagram = h_util.c4g(hexagram_lines)
c3g_hexagram = h_util.c3g(hexagram_lines)
gi6_hexagram = h_util.gi6(hexagram_lines)
gi5_hexagram = h_util.gi5(hexagram_lines)
i6g_hexagram = h_util.i6g(hexagram_lines)
i5g_hexagram = h_util.i5g(hexagram_lines)

string_hex_4 = (gc6_hexagram[0], gc5_hexagram[0], gc4_hexagram[0], gc3_hexagram[0], c6g_hexagram[0], c5g_hexagram[0], c4g_hexagram[0], c3g_hexagram[0], gi6_hexagram[0], gi5_hexagram[0], i6g_hexagram[0], i5g_hexagram[0])

jin_fan_1 = this_hexagram
jin_fan_2 = h_util.axillary_hexagram(jin_fan_1, 1)
jin_fan_3 = h_util.axillary_hexagram(jin_fan_2, 2)
jin_fan_4 = h_util.axillary_hexagram(jin_fan_3, 3)
jin_fan_5 = h_util.axillary_hexagram(jin_fan_4, 4)
jin_fan_6 = h_util.axillary_hexagram(jin_fan_5, 5)
jin_fan_7 = h_util.axillary_hexagram(jin_fan_6, 4)
jin_fan_8 = h_util.axillary_hexagram(jin_fan_7, 3)
jin_fan_9 = h_util.axillary_hexagram(jin_fan_8, 2)
jin_fan_10 = h_util.axillary_hexagram(jin_fan_9, 1)
jin_fan_11 = h_util.axillary_hexagram(jin_fan_10, 2)
jin_fan_12 = h_util.axillary_hexagram(jin_fan_11, 3)
jin_fan_13 = h_util.axillary_hexagram(jin_fan_12, 4)
jin_fan_14 = h_util.axillary_hexagram(jin_fan_13, 5)
jin_fan_15 = h_util.axillary_hexagram(jin_fan_14, 4)
jin_fan_16 = h_util.axillary_hexagram(jin_fan_15, 3)
jin_fan_17 = h_util.axillary_hexagram(jin_fan_16, 2)

string_hex_5 = (jin_fan_1[0], jin_fan_2[0], jin_fan_3[0], jin_fan_4[0], jin_fan_5[0], jin_fan_6[0], jin_fan_7[0], jin_fan_8[0], jin_fan_9[0], jin_fan_10[0], jin_fan_11[0], jin_fan_12[0], jin_fan_13[0], jin_fan_14[0], jin_fan_15[0], jin_fan_16[0], jin_fan_17[0])

f1_hex, f11_hex = h_util.feng_shei (hexagram_lines, "c6", "c3", 1)
f2_hex, f12_hex = h_util.feng_shei (hexagram_lines, "c6", "c3", 2)
f3_hex, f13_hex = h_util.feng_shei (hexagram_lines, "c6", "c3", 3)
f4_hex, f14_hex = h_util.feng_shei (hexagram_lines, "c6", "c3", 4)
f5_hex, f15_hex = h_util.feng_shei (hexagram_lines, "c6", "c3", 5)
f6_hex, f16_hex = h_util.feng_shei (hexagram_lines, "c6", "c3", 6)
f7_hex, f17_hex = h_util.feng_shei (hexagram_lines, "c6", "c3", 7)
f8_hex, f18_hex = h_util.feng_shei (hexagram_lines, "c6", "c3", 8)

f21_hex, f31_hex = h_util.feng_shei (hexagram_lines, "c5", "c3", 1)
f22_hex, f32_hex = h_util.feng_shei (hexagram_lines, "c5", "c3", 2)
f23_hex, f33_hex = h_util.feng_shei (hexagram_lines, "c5", "c3", 3)
f24_hex, f34_hex = h_util.feng_shei (hexagram_lines, "c5", "c3", 4)
f25_hex, f35_hex = h_util.feng_shei (hexagram_lines, "c5", "c3", 5)
f26_hex, f36_hex = h_util.feng_shei (hexagram_lines, "c5", "c3", 6)
f27_hex, f37_hex = h_util.feng_shei (hexagram_lines, "c5", "c3", 7)
f28_hex, f38_hex = h_util.feng_shei (hexagram_lines, "c5", "c3", 8)

f41_hex, f51_hex = h_util.feng_shei (hexagram_lines, "c5", "c4", 1)
f42_hex, f52_hex = h_util.feng_shei (hexagram_lines, "c5", "c4", 2)
f43_hex, f53_hex = h_util.feng_shei (hexagram_lines, "c5", "c4", 3)
f44_hex, f54_hex = h_util.feng_shei (hexagram_lines, "c5", "c4", 4)
f45_hex, f55_hex = h_util.feng_shei (hexagram_lines, "c5", "c4", 5)
f46_hex, f56_hex = h_util.feng_shei (hexagram_lines, "c5", "c4", 6)
f47_hex, f57_hex = h_util.feng_shei (hexagram_lines, "c5", "c4", 7)
f48_hex, f58_hex = h_util.feng_shei (hexagram_lines, "c5", "c4", 8)

f61_hex, f71_hex = h_util.feng_shei (hexagram_lines, "i6", "c3", 1)
f62_hex, f72_hex = h_util.feng_shei (hexagram_lines, "i6", "c3", 2)
f63_hex, f73_hex = h_util.feng_shei (hexagram_lines, "i6", "c3", 3)
f64_hex, f74_hex = h_util.feng_shei (hexagram_lines, "i6", "c3", 4)
f65_hex, f75_hex = h_util.feng_shei (hexagram_lines, "i6", "c3", 5)
f66_hex, f76_hex = h_util.feng_shei (hexagram_lines, "i6", "c3", 6)
f67_hex, f77_hex = h_util.feng_shei (hexagram_lines, "i6", "c3", 7)
f68_hex, f78_hex = h_util.feng_shei (hexagram_lines, "i6", "c3", 8)

f81_hex, f91_hex = h_util.feng_shei (hexagram_lines, "i5", "c3", 1)
f82_hex, f92_hex = h_util.feng_shei (hexagram_lines, "i5", "c3", 2)
f83_hex, f93_hex = h_util.feng_shei (hexagram_lines, "i5", "c3", 3)
f84_hex, f94_hex = h_util.feng_shei (hexagram_lines, "i5", "c3", 4)
f85_hex, f95_hex = h_util.feng_shei (hexagram_lines, "i5", "c3", 5)
f86_hex, f96_hex = h_util.feng_shei (hexagram_lines, "i5", "c3", 6)
f87_hex, f97_hex = h_util.feng_shei (hexagram_lines, "i5", "c3", 7)
f88_hex, f98_hex = h_util.feng_shei (hexagram_lines, "i5", "c3", 8)

string_hex_6 = (f1_hex[0], f2_hex[0], f3_hex[0], f4_hex[0], f5_hex[0], f6_hex[0], f7_hex[0], f8_hex[0])
string_hex_7 = (f11_hex[0], f12_hex[0], f13_hex[0], f14_hex[0], f15_hex[0], f16_hex[0], f17_hex[0], f18_hex[0])
string_hex_8 = (f21_hex[0], f22_hex[0], f23_hex[0], f24_hex[0], f25_hex[0], f26_hex[0], f27_hex[0], f28_hex[0])
string_hex_9 = (f31_hex[0], f32_hex[0], f33_hex[0], f34_hex[0], f35_hex[0], f36_hex[0], f37_hex[0], f38_hex[0])
string_hex_10 = (f41_hex[0], f42_hex[0], f43_hex[0], f44_hex[0], f45_hex[0], f46_hex[0], f47_hex[0], f48_hex[0])
string_hex_11 = (f51_hex[0], f52_hex[0], f53_hex[0], f54_hex[0], f55_hex[0], f56_hex[0], f57_hex[0], f58_hex[0])
string_hex_12 = (f61_hex[0], f62_hex[0], f63_hex[0], f64_hex[0], f65_hex[0], f66_hex[0], f67_hex[0], f68_hex[0])
string_hex_13 = (f71_hex[0], f72_hex[0], f73_hex[0], f74_hex[0], f75_hex[0], f76_hex[0], f77_hex[0], f78_hex[0])
string_hex_14 = (f81_hex[0], f82_hex[0], f83_hex[0], f84_hex[0], f85_hex[0], f86_hex[0], f87_hex[0], f88_hex[0])
string_hex_15 = (f91_hex[0], f92_hex[0], f93_hex[0], f94_hex[0], f95_hex[0], f96_hex[0], f97_hex[0], f98_hex[0])

str_hex_1 = (string_hex_5 + string_hex_6 + string_hex_7 + string_hex_8 + string_hex_9 + string_hex_10 + string_hex_11 + string_hex_12 + string_hex_13 + string_hex_14 + string_hex_15)

string_hexagram = (string_hex_1 + string_hex_2 + string_hex_3 + string_hex_4 + str_hex_1)
checkpoint = x_util.print_a_file(hex_number, string_hexagram)
#print string_hexagram

# print this_hexagram[0], inverse[0], reverse[0], nuclear[0], golden[0], evolved[0], interlaced[0], married[0], axillary_one[0], axillary_two[0], axillary_three[0], axillary_four[0], axillary_five[0], axillary_six[0], wen_prior[0], wen_next[0], fu_prior[0], fu_next[0], mawangdui_prior[0], mawangdui_next[0], base_prior[0], base_next[0],c6c6_hexagram[0], c6c5_hexagram[0], c6c4_hexagram[0], c6c3_hexagram[0], c5c6_hexagram[0], c5c5_hexagram[0], c5c4_hexagram[0], c5c3_hexagram[0], c4c6_hexagram[0], c4c5_hexagram[0], c4c4_hexagram[0], c4c3_hexagram[0], c3c6_hexagram[0], c3c5_hexagram[0], c3c4_hexagram[0], c3c3_hexagram[0]
#print "H# In Re Nu Go Ev It MA A1 A2 A3 A4 A5 A6 WP WN FP FN MP MN BP BN c66 c65 c64 c63 c56 c55 c54 c53 c46 c45 c44 c43 c36 c35 c34 c33 J1 J2 J3 J4 J5 J6 J7 J8 J9 J10 J11 J12 J13 J14 J15 J16 J17 F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 F20 F21 F22 F23 F24 F25 F26 F27 F28 F29 F30 F31 F32 F33 F34 F35 F36 F37 F38 F39 F40 F41 F42 F43 F44 F45 F46 F47 F48 F49 F50 F51 F52 F53 F54 F55 F56 F57 F58 F59 F60 F61 F62 F63 F64 F65 F66 F67 F68 F69 F70 F71 F72 F73 F74 F75 F76 F77 F78 F79 "
return string_hexagram

def display_all_trigram_data(hexagram_lines):

hex_number = hexagram_lines[0]
upper_trigram = t_util.trigrams_in_hexagram(hexagram_lines, "upper")
lower_trigram = t_util.trigrams_in_hexagram(hexagram_lines, "lower")
nuclear = h_util.nuclear_hexagram(hexagram_lines)
nuclear_lower_trigram = t_util.trigrams_in_hexagram(nuclear, "lower")
nuclear_upper_trigram = t_util.trigrams_in_hexagram(nuclear, "upper")
interlaced = h_util.interlaced_hexagram(hexagram_lines)
interlaced_lower_trigram = t_util.trigrams_in_hexagram(interlaced, "upper")
interlaced_upper_trigram = t_util.trigrams_in_hexagram(interlaced, "upper")
married = h_util.married_hexagram(hexagram_lines)
married_lower_trigram = t_util.trigrams_in_hexagram(married, "lower")
married_upper_trigram = t_util.trigrams_in_hexagram(married, "upper")
golden = t_util.golden_trigram(hexagram_lines)
hex_family = t_util.hexagram_family(hexagram_lines[0])
nuclear_hex_family = t_util.hexagram_family(nuclear[0])
interlaced_hex_family = t_util.hexagram_family(interlaced[0])
married_hex_family = t_util.hexagram_family(married[0])
print married, " is married hexagram "
print married_hex_family, " is married_hex_family "
ft_01 = t_util.feng_shui_sequence(upper_trigram, 1)
ft_02 = t_util.feng_shui_sequence(upper_trigram, 2)
ft_03 = t_util.feng_shui_sequence(upper_trigram, 3)
ft_04 = t_util.feng_shui_sequence(upper_trigram, 4)
ft_05 = t_util.feng_shui_sequence(upper_trigram, 5)
ft_06 = t_util.feng_shui_sequence(upper_trigram, 6)
ft_07 = t_util.feng_shui_sequence(upper_trigram, 7)
ft_08 = t_util.feng_shui_sequence(upper_trigram, 8)
ft_11 = t_util.feng_shui_sequence(lower_trigram, 1)
ft_12 = t_util.feng_shui_sequence(lower_trigram, 2)
ft_13 = t_util.feng_shui_sequence(lower_trigram, 3)
ft_14 = t_util.feng_shui_sequence(lower_trigram, 4)
ft_15 = t_util.feng_shui_sequence(lower_trigram, 5)
ft_16 = t_util.feng_shui_sequence(lower_trigram, 6)
ft_17 = t_util.feng_shui_sequence(lower_trigram, 7)
ft_18 = t_util.feng_shui_sequence(lower_trigram, 8)

#space = " "
#print hexagram_lines[0], space, upper_trigram, space,lower_trigram, space, nuclear_upper_trigram, space, nuclear_lower_trigram, space, interlaced_upper_trigram, space, interlaced_lower_trigram,space, married_upper_trigram, space, married_lower_trigram, space, golden, space, hex_family, space, nuclear_hex_family, space, interlaced_hex_family, space, married_hex_family
#print "UT, LT, NUT, NLT, IUT, ILT, MUT, MLT, GT,HF,NF,IF, NF"
trigram_string = (hexagram_lines[0], upper_trigram[0], lower_trigram[0], nuclear_upper_trigram[0], nuclear_lower_trigram[0], interlaced_upper_trigram[0], interlaced_lower_trigram[0], married_upper_trigram[0], married_lower_trigram[0], golden[0], hex_family, nuclear_hex_family, interlaced_hex_family, married_hex_family, ft_01[0], ft_02[0], ft_03[0], ft_04[0], ft_05[0], ft_06[0], ft_07[0], ft_08[0], ft_11[0], ft_12[0], ft_13[0], ft_14[0], ft_15[0], ft_16[0], ft_17[0], ft_18[0])
print "Printing trigrams of ", hex_number, " now"
checkpoint = x_util.print_a_file(hex_number, trigram_string)
#print trigram_string
#print hexagram_lines
return trigram_string

def display_all_branch_data(hexagram_lines):
branch_data = s_util.hexagram_branches(hexagram_lines)
branch_string = (hexagram_lines[0], branch_data)
return branch_string

def display_all_stem_data(hexagram_lines):
lower_stem, upper_stem = s_util.hexagram_stems(hexagram_lines)
stem_string = (hexagram_lines[0], upper_stem, lower_stem)
#print stem_string
#print "H#, US, LS"
return stem_string

def run_a_hexagram(hex_number):
this_hexagram = h_util.load_hexagram(hex_number)
hexagram_string = display_all_hexagram_data(this_hexagram)
trigram_string = display_all_trigram_data(this_hexagram)
stem_string = display_all_stem_data(this_hexagram)
branch_string = display_all_branch_data(this_hexagram)
return hexagram_string, trigram_string, stem_string, branch_string

def run_through_the_hexagrams(hex_number):
kounter = 0
for kounter in range(65):
 hex_number = kounter
 this_hexagram = h_util.load_hexagram(hex_number)
 check = display_all_hexagram_data(this_hexagram)
 print check
print "H# In Re Nu Go Ev It MA A1 A2 A3 A4 A5 A6 WP WN FP FN MP MN BP BN c66 c65 c64 c63 c56 c55 c54 c53 c46 c45 c44 c43 c36 c35 c34 c33 J1 J2 J3 J4 J5 J6 J7 J8 J9 J10 J11 J12 J13 J14 J15 J16 J17 F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 F20 F21 F22 F23 F24 F25 F26 F27 F28 F29 F30 F31 F32 F33 F34 F35 F36 F37 F38 F39 F40 F41 F42 F43 F44 F45 F46 F47 F48 F49 F50 F51 F52 F53 F54 F55 F56 F57 F58 F59 F60 F61 F62 F63 F64 F65 F66 F67 F68 F69 F70 F71 F72 F73 F74 F75 F76 F77 F78 F79 "
kounter = 0
for kounter in range(65):
 hex_number = kounter
 this_hexagram = h_util.load_hexagram(hex_number)
 check = display_all_trigram_data(this_hexagram)
 print check
print "Hexagram #, UT, LT, NUT, NLT, IUT, ILT, MUT, MLT, GT,HF,NF,IF, MF"
kounter = 0
hex_number = 0
for kounter in range(65):
 hex_number = kounter
 this_hexagram = load_hexagram(hex_number)
 check = display_all_stem_data(this_hexagram)
 print check
print "H#, US, LS"
kounter = 0
hex_number = 0
for kounter in range(65):
 hex_number = kounter
 this_hexagram = load_hexagram(hex_number)
 check = display_all_branch_data(this_hexagram)
 print check
print "H#, L#1, L#2, L#3, L#4, L#5, L#6"
return

def create_h_web_page(hex_number):
start_h_string = '<td><img src = "..\common\h_'
inter_h_string = '.png" alt = " '
end_h_string= ' " height = "90" width = "45" border = " 0 " align = "center" ></td> '
hex_string = str(hex_number)
return_hex_string = (start_h_string + hex_string + inter_h_string + hex_string + end_h_string)
return return_hex_string

def create_t_web_page(hex_number):
start_t_string = '<td><img src = "..\common\t_'
inter_t_string = '.png" alt = " '
end_t_string= ' " height = "90" width = "45" border = " 0 " align = "center" ></td> '
tri_string = str(hex_number)
return_tri_string = (start_t_string + hex_string + inter_t_string + hex_string + end_t_string)
return return_tri_string

def create_web_page(hex_number):
hexagram_string, trigram_string, stem_string, branch_string = run_a_hexagram(hex_number)
hex_count = len(hexagram_string)
hex_count = hex_count + 1
hex_array = [" " ] * hex_count
hex_count = hex_count - 1
for hex_kount in range(hex_count):
 check_hex_kount = hex_kount
 print check_hex_kount, " is check_hex_kount ", hex_count, " is the range we go to "
 create_this_hexagram = hexagram_string[check_hex_kount]
 hex_array[check_hex_kount] = create_h_web_page(create_this_hexagram)
checkpoint = x_util.print_a_file(hex_number, hex_array)
return

print " dis_util module is loaded "
