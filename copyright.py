Copy_gnu.py : Copyright Routines.
#!usr/bin/python
import sys
sys.path.insert (0, '/usr/local/lib/python-1.5/lib')

# Name: Copyright and Licence Terms
# Author: Jonathon Blake
# Version: 0.0.0.1
# Creation Date: 17 September 2001
# Creation Time: 15:57 GMT
# Last Modified: 8 September 2002
# Update Time:4:01 GMT
# Copyright: 2001 - 2002: Jonathon Blake

# Licensing Terms:
#
# By obtaining, using, and/or copying this software and/or its
# associated documentation, you agree that you have read, understood,
# and will comply with the following terms and conditions:
#
# Permission to use, copy, modify, and distribute this software and its
# associated documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appears in all
# copies, and that both that copyright notice and this permission notice
# appear in supporting documentation, and that the name of
# the author --- Jonathon Blake --- not be used in
# advertising or publicity pertaining to distribution of the software
# without specific, written prior permission.
#
# THE AUTHOR --- JONATHON BLAKE --- DISCLAIMS
# ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM 
# LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
# OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE
# OR PERFORMANCE OF THIS SOFTWARE.
#
# --------------------------------------------------------------------
#
# Furthermore, you also agree to the terms and conditions of the GNU
# General Public License, Version 2.0.

# *********************************************************************

# Module History

# 13 September 2001
#
# Wrote all modules not listed in the rest of this history section
#
# 21 September 2001
#
# renamed licence to python_license.
# Split lack_of_warrenty into python_lack_of_warranty and gnu_lack_of_warranty.
#
# Added show_pc


import sys, time

def python_license(check):
 print """
 By obtaining, using, and/or copying this software and/or its
 associated documentation, you agree that you have read,
 understood,and will comply with the following terms and
 conditions:

 Permission to use, copy, modify, and distribute this software and
 its associated documentation for any purpose and without fee is
 hereby granted, provided that the above copyright notice appears
 in all copies, and that both that copyright notice and this
 permission notice appear in supporting documentation, and that the
 name of the author --- Jonathon Blake --- not be used in
 advertising or publicity pertaining to distribution of the software
 without specific, written prior permission.
 """
return

def python_lack_of_warranty(check):
print """

 THE AUTHOR --- JONATHON BLAKE --- DISCLAIMS ALL WARRANTIES WITH
 REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF
 MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE
 LIABLE FOR ANY SPECIAL, INDIRECTOR CONSEQUENTIAL DAMAGES OR ANY
 DAMAGES WHATSOEVER RESULTING FROM LOSSOF USE, DATA OR PROFITS,
 WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCEOR OTHER TORTIOUS
 ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
 OF THIS SOFTWARE.
 """
def gnu_lack_of_warrenty(check):
python_lack_of_warranty(check)
print """

 Furthermore, you also agree to the terms and conditions of
 the GNU General Public License, Version 2.0.

"""
return

def gnu_public_licence(check):

print """

GNU GENERAL PUBLIC LICENSE
Version 2, June 1991
 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
675 Mass Ave, Cambridge, MA 02139, USA


 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 """
time.sleep (check)
print """

Preamble

 The licenses for most software are designed to take away your
 freedom to share and change it. By contrast, the GNU General
 Public License is intended to guarantee your freedom to share
 and change free software--to make sure the software is free
 for all its users. This General Public License applies to
 most of the Free Software Foundation's software and to any
 other program whose authors commit to using it. (Some other
 Free Software Foundation software is covered by the GNU
 Library General Public License instead.) You can apply it to
 your programs, too.

 When we speak of free software, we are referring to freedom,
 not price. Our General Public Licenses are designed to make
 sure that you have the freedom to distribute copies of free
 software (and charge for this service if you wish), that you
 receive source code or can get it if you want it, that you
 can change the software or use pieces of it in new free
 programs; and that you know you can do these things.

"""
time.sleep(check)
print """

 To protect your rights, we need to make restrictions that
 forbid anyone to deny you these rights or to ask you to
 surrender the rights. These restrictions translate to certain
 responsibilities for you if you distribute copies of the
 software, or if you modify it.

 For example, if you distribute copies of such a program,
 whether gratis or for a fee, you must give the recipients all
 the rights that you have. You must make sure that they, too,
 receive or can get the source code. And you must show them
 these terms so they know their rights.

 We protect your rights with two steps: (1) copyright the
 software, and (2) offer you this license which gives you
 legal permission to copy, distribute and/or modify the
 software.

"""
time.sleep(check)
print """

 Also, for each author's protection and ours, we want to make
 certain that everyone understands that there is no warranty
 for this free software. If the software is modified by
 someone else and passed on, we want its recipients to know
 that what they have is not the original, so that any problems
 introduced by others will not reflect on the original
 authors' reputations.

 Finally, any free program is threatened constantly by
 software patents. We wish to avoid the danger that
 redistributors of a free program will individually obtain
 patent licenses, in effect making the program proprietary.
 To prevent this, we have made it clear that any patent must
 be licensed for everyone's free use or not licensed at all.

 The precise terms and conditions for copying, distribution
 and modification follow.

"""
time.sleep(check)
print """

GNU GENERAL PUBLIC LICENSE
 TERMS AND CONDITIONS FOR
COPYING, DISTRIBUTION AND MODIFICATION

 0. This License applies to any program or other work which
 contains a notice placed by the copyright holder saying it
 may be distributed under the terms of this General Public
 License. The "Program", below, refers to any such program or
 work, and a "work based on the Program" means either the
 Program or any derivative work under copyright law: that is
 to say, a work containing the Program or a portion of it,
 either verbatim or with modifications and/or translated into
 another language. (Hereinafter, translation is included
 without limitation in the term "modification".) Each licensee
 is addressed as "you".

 Activities other than copying, distribution and modification
 are not covered by this License; they are outside its scope.
 The act of running the Program is not restricted, and the
 output from the Program is covered only if its contents
 constitute a work based on the Program (independent of having
 been made by running the Program). Whether that is true
 depends on what the Program does.

"""
time.sleep(check)
print """

 1. You may copy and distribute verbatim copies of the
 Program's source code as you receive it, in any medium,
 provided that you conspicuously and appropriately publish on
 each copy an appropriate copyright notice and disclaimer of
 warranty; keep intact all the notices that refer to this
 License and to the absence of any warranty; and give any
 other recipients of the Program a copy of this License along
 with the Program.

 You may charge a fee for the physical act of transferring a
 copy, and you may at your option offer warranty protection in
 exchange for a fee.

"""
time.sleep(check)
print """

 2. You may modify your copy or copies of the Program or any
 portion of it, thus forming a work based on the Program, and
 copy and distribute such modifications or work under the
 terms of Section 1 above, provided that you also meet all of
 these conditions:

 a) You must cause the modified files to carry prominent
 notices stating that you changed the files and the date of
 any change.

 b) You must cause any work that you distribute or publish,
 that in whole or in part contains or is derived from the
 Program or any part thereof, to be licensed as a whole at no
 charge to all third parties under the terms of this License.

 c) If the modified program normally reads commands
 interactively when run, you must cause it, when started
 running for such interactive use in the most ordinary way, to
 print or display an announcement including an appropriate
 copyright notice and a notice that there is no warranty (or
 else, saying that you provide a warranty) and that users may
 redistribute the program under these conditions, and telling
 the user how to view a copy of this License. (Exception: if
 the Program itself is interactive but does not normally print
 such an announcement, your work based on the Program is not
 required to print an announcement.)

"""
time.sleep(check)
print """

 These requirements apply to the modified work as a whole. If
 identifiable sections of that work are not derived from the
 Program, and can be reasonably considered independent and
 separate works in themselves, then this License, and its
 terms, do not apply to those sections when you distribute
 them as separate works. But when you distribute the same
 sections as part of a whole which is a work based on the
 Program, the distribution of the whole must be on the terms
 of this License, whose permissions for other licensees extend
 to the entire whole, and thus to each and every part
 regardless of who wrote it.

 Thus, it is not the intent of this section to claim rights or
 contest your rights to work written entirely by you; rather,
 the intent is to exercise the right to control the
 distribution of derivative or collective works based on the
 Program.

 In addition, mere aggregation of another work not based on
 the Program with the Program (or with a work based on the
 Program) on a volume of a storage or distribution medium does
 not bring the other work under the scope of this License.

"""
time.sleep(check)
print """

 3. You may copy and distribute the Program (or a work based
 on it, under Section 2) in object code or executable form
 under the terms of Sections 1 and 2 above provided that you
 also do one of the following:

 a) Accompany it with the complete corresponding machine-
 readable source code, which must be distributed under the
 terms of Sections 1 and 2 above on a medium customarily used
 for software interchange; or,

 b) Accompany it with a written offer, valid for at least
 three years, to give any third party, for a charge no more
 than your cost of physically performing source distribution,
 a complete machine-readable copy of the corresponding source
 code, to be distributed under the terms of Sections 1 and 2
 above on a medium customarily used for software interchange;
 or,

 c) Accompany it with the information you received as to the
 offer to distribute corresponding source code. (This
 alternative is allowed only for noncommercial distribution
 and only if you received the program in object code or
 executable form with such an offer, in accord with Subsection
 b above.)

"""
time.sleep(check)
print """

 The source code for a work means the preferred form of the
 work for making modifications to it. For an executable work,
 complete source code means all the source code for all
 modules it contains, plus any associated interface definition
 files, plus the scripts used to control compilation and
 installation of the executable. However, as a special
 exception, the source code distributed need not include
 anything that is normally distributed (in either source or
 binary form) with the major components (compiler, kernel, and
 so on) of the operating system on which the executable runs,
 unless that component itself accompanies the executable.

 If distribution of executable or object code is made by
 offering access to copy from a designated place, then
 offering equivalent access to copy the source code from the
 same place counts as distribution of the source code, even
 though third parties are not compelled to copy the source
 along with the object code.

"""
time.sleep(check)
print """

 4. You may not copy, modify, sublicense, or distribute the
 Program except as expressly provided under this License. Any
 attempt otherwise to copy, modify, sublicense or distribute
 the Program is void, and will automatically terminate your
 rights under this License. However, parties who have received
 copies, or rights, from you under this License will not have
 their licenses terminated so long as such parties remain in
 full compliance.

 5. You are not required to accept this License, since you
 have not signed it. However, nothing else grants you
 permission to modify or distribute the Program or its
 derivative works. These actions are prohibited by law if you
 do not accept this License. Therefore, by modifying or
 distributing the Program (or any work based on the Program),
 you indicate your acceptance of this License to do so, and
 all its terms and conditions for copying, distributing or
 modifying the Program or works based on it.

"""
time.sleep(check)
print """

 6. Each time you redistribute the Program (or any work based
 on the Program), the recipient automatically receives a
 license from the original licensor to copy, distribute or
 modify the Program subject to these terms and conditions. You
 may not impose any further restrictions on the recipients'
 exercise of the rights granted herein. You are not
 responsible for enforcing compliance by third parties to this
 License.

"""
time.sleep(check)
print """

 7. If, as a consequence of a court judgment or allegation of
 patent infringement or for any other reason (not limited to
 patent issues), conditions are imposed on you (whether by
 court order, agreement or otherwise) that contradict the
 conditions of this License, they do not excuse you from the
 conditions of this License. If you cannot distribute so as to
 satisfy simultaneously your obligations under this License
 and any other pertinent obligations, then as a consequence
 you may not distribute the Program at all. For example, if a
 patent license would not permit royalty-free redistribution
 of the Program by all those who receive copies directly or
 indirectly through you, then the only way you could satisfy
 both it and this License would be to refrain entirely from
 distribution of the Program.

 If any portion of this section is held invalid or
 unenforceable under any particular circumstance, the balance
 of the section is intended to apply and the section as a
 whole is intended to apply in other circumstances.

 It is not the purpose of this section to induce you to
 infringe any patents or other property right claims or to
 contest validity of any such claims; this section has the
 sole purpose of protecting the integrity of the free software
 distribution system, which is implemented by public license
 practices. Many people have made generous contributions to
 the wide range of software distributed through that system in
 reliance on consistent application of that system; it is up
 to the author/donor to decide if he or she is willing to
 distribute software through any other system and a licensee
 cannot impose that choice.

 This section is intended to make thoroughly clear what is
 believed to be a consequence of the rest of this License.

"""
time.sleep(check)
print """

 8. If the distribution and/or use of the Program is
 restricted in certain countries either by patents or by
 copyrighted interfaces, the original copyright holder who
 places the Program under this License may add an explicit
 geographical distribution limitation excluding those
 countries, so that distribution is permitted only in or among
 countries not thus excluded. In such case, this License
 incorporates the limitation as if written in the body of this
 License.

 9. The Free Software Foundation may publish revised and/or
 new versions of the General Public License from time to time.
 Such new versions will be similar in spirit to the present
 version, but may differ in detail to address new problems or
 concerns.

 Each version is given a distinguishing version number. If the
 Program specifies a version number of this License which
 applies to it and "any later version", you have the option of
 following the terms and conditions either of that version or
 of any later version published by the Free Software
 Foundation. If the Program does not specify a version number
 of this License, you may choose any version ever published by
 the Free Software Foundation.

"""
time.sleep(check)
print """

 10. If you wish to incorporate parts of the Program into
 other free programs whose distribution conditions are
 different, write to the author to ask for permission. For
 software which is copyrighted by the Free Software
 Foundation, write to the Free Software Foundation; we
 sometimes make exceptions for this. Our decision will be
 guided by the two goals of preserving the free status of all
 derivatives of our free software and of promoting the sharing
 and reuse of software generally.

"""
time.sleep(check)
print """

 NO WARRANTY

 11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS
 NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
 APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE
 COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM
 "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
 IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF
 THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE,
 YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
 CORRECTION.

"""
time.sleep(check)
print """

 12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED
 TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY
 WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM AS PERMITTED
 ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL,
 SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF
 THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT
 LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR
 LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE
 PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH
 HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
 SUCH DAMAGES.

END OF TERMS AND CONDITIONS
 """

print """
 Appendix: How to Apply These Terms to Your New Programs

 If you develop a new program, and you want it to be of the
 greatest possible use to the public, the best way to achieve
 this is to make it free software which everyone can
 redistribute and change under these terms.

 To do so, attach the following notices to the program. It is
 safest to attach them to the start of each source file to
 most effectively convey the exclusion of warranty; and each
 file should have at least the "copyright" line and a pointer
 to where the full notice is found.

 <one line to give the program's name and a brief idea of what
 it does.>
 Copyright (C) 19yy <name of author>

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 as published by the Free Software Foundation; either version
 2 of the License, or (at your option) any later version.

 This program is distributed in the hope that it will be
 useful, but WITHOUT ANY WARRANTY; without even the implied
 warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
 PURPOSE. See the GNU General Public License for more details.

 You should have received a copy of the GNU General Public
 License along with this program; if not, write to the Free
 Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139,
 USA.

 Also add information on how to contact you by electronic and
 paper mail.

 If the program is interactive, make it output a short notice
 like this when it starts in an interactive mode:

 Gnomovision version 69,
 Copyright (C) 19yy name of author

 Gnomovision comes with ABSOLUTELY NO WARRANTY; for details
 type `show w'. This is free software, and you are welcome to
 redistribute it under certain conditions; type `show c' for
 details.

 The hypothetical commands `show w' and `show c' should show
 the appropriate parts of the General Public License. Of
 course, the commands you use may be called something other
 than `show w' and `show c'; they could even be mouse-clicks
 or menu items--whatever suits your program.

 You should also get your employer (if you work as a
 programmer) or your school, if any, to sign a "copyright
 disclaimer" for the program, if necessary.

 Here is a sample; alter the names:

 Yoyodyne, Inc., hereby disclaims all copyright interest in
 the program `Gnomovision' (which makes passes at compilers)
 written by James Hacker.

 <signature of Ty Coon>, 1 April 1989
 Ty Coon, President of Vice

 This General Public License does not permit incorporating
 your program into proprietary programs. If your program is a
 subroutine library, you may consider it more useful to permit
 linking proprietary applications with the library. If this is
 what you want to do, use the GNU Library General Public
 License instead of this License.

"""
return

def show_python(check):
 python_license(check)
 time.sleep(check)
 python_lack_of_warranty(check)
 return

def show_gnu(check):
gnu_public_licence(check)
return

def show_w(check):
print """
 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 Version 2 as published by the Free Software Foundation.

 This program is distributed in the hope that it will be
 useful, but WITHOUT ANY WARRANTY; without even the implied
 warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
 PURPOSE. See the GNU General Public License for more details.

 You should have received a copy of the GNU General Public
 License along with this program; if not, write to the Free
 Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139,
 USA.
"""
time.sleep(check)
gnu_lack_of_warrenty(check)
return

def show_c(check, program_name, version_number, program_description, years):
print
print program_name, " Version ", version_number
print program_description
print "Copyright (c) ", years, " Jonathon Blake"
print "Distributed under the terms of the GNU Public Licence Version 2"
print
time.sleep(check)
return

def show_pc(check, program_name, version_number, program_description, years, brief_licence_description):
print
print program_name, " Version ", version_number
print program_description
print "Copyright (c) ", years, " Jonathon Blake"
print brief_licence_description
print
time.sleep(check)
return

def show_which(do_display, check):
if do_display == "true":
 show_python(check)
 show_gnu(check)
else:
 show_w(check)
return

check = 5
show_c(check, "Copyright Module", " 0.0.0.1", "General Purpose Copyright / Licence Terms", "2001 - 2002")

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
h.py: Main program
#!/usr/bin/python
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


p_util.py: Phase Utilities and Routines
#!/usr/bin/python
import sys
sys.path.insert (0, '/usr/local/lib/python-1.5/lib')
# remember to delete the above line when changing operating systems
#
# YiJing Hexagram Construction Program
#
# Initialization routines for the phases
#
# This is version 0.0.0.1
# Creation Date: 7 September 2002 @ 6:04 GMT
# Last Update: 7 September 2002 @ 6:04 GMT
# Copyright: 2002 Jonathon Blake
# Licence Terms: GNU General Public Licence

# Phases module History
#
# 7 September 2002
#
# First created
#
#This entire module is a stub. 
#

print " p_util.py module is loaded"


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
