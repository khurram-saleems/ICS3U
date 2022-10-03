# Assignment 1-1
# Khurram's School Information
# 
# Khurram Shaikh
# Tuesday, September 20, 2022
#
# This program displays an introductory paragraph, and my schedule 
# along with start dates for semester one and two formatted in a 
# columned table. Includes additional contact information and 
# locker location.

from datetime import datetime
print('{:*^80s}\n'.format("Khurram Shaikh (19532sha)"))

# Output introductory paragraph
print("Super excited for another year at St.Benedict! My name is Khurram, I am") 
print("currently in Grade 11 and unfortunately my first semester is looking pretty")
print("tough. Although, really enthusiastic for my CS class! During the school year I")
print("hope to increase my involvement in extracurriculars, leadership and broaden my") 
print("passion for STEM. Really looking forward to innovate and learn!\n")

# Output scheduling information for semester one and two, formatted to total character length
print('Semester 1 start date: {:%Y-%m-%d %H:%M} AM\n'.format(datetime(2022, 9, 6, 8, 0)))
print("Here is my schedule for Semester 1:\n")
print("{:-^80}".format(''))
print("Per {:<3d} {:9} {:26} Rm {:<4d} {:13} {:11} |".format(1,"ENG 3UP","AP English",304,"Ms.Tapper", "8:00-9:15"))
print("Per {:<3d} {:9} {:26} Rm {:<4d} {:13} {:11} |".format(2,"MCR 3UP","AP Functions",306,"Ms.Stockie", "9:20-10:35"))
print("Per {:<3d} {:9} {:26} Rm {:<4d} {:13} {:11} |".format(3,"CHW 3MI","World History",226,"Mr.Kukwa", "11:25-12:40"))
print("Per {:<3d} {:9} {:26} Rm {:<4d} {:13} {:11} |".format(4,"ICS 3U","Intro to Computer Science",216,"Mr.Milardovic", "12:45-2:00"))
print("{:-^80}\n".format(''))
print('Semester 2 start date: {:%Y-%m-%d %H:%M} AM\n'.format(datetime(2023, 2, 6, 8, 0)))
print("Here is my schedule for Semester 2:\n")
print("{:-^80}".format(('')))
print("Per {:<3d} {:9} {:26} Rm {:<4d} {:13} {:11} |".format(1,"SPH 3UI","Physics ",314,"Mr.Reitzel", "8:00-9:15"))
print("Per {:<3d} {:9} {:26} Rm {:<4d} {:13} {:11} |".format(2,"HRT 3MI","World Religion",306,"Mr.Greg", "9:20-10:35"))
print("Per {:<3d} {:9} {:26} Rm {:<4d} {:13} {:11} |".format(3,"SCH 3UI","Chemistry",226,"Mr.Kukwa", "11:25-12:40"))
print("Per {:<3d} {:9} {:26} Rm {:<4d} {:13} {:11} |".format(4,"MHF 4UP","AP Advanced Functions",216,"Mr.Frat", "12:45-2:00"))
print("{:-^80}\n".format(''))

# Additional contact information
print("Additional contact information:\n")
print("School Email: {:20} Locker: {:>4d}".format("19532sha@wcdsb.ca",3448))
print()
print("Have a great day and best of luck with school!")


