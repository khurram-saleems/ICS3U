#     Assignment | Assignment 1-3 
#  Program Title | The 411
#                |
#     Written by | Khurram Shaikh
#           Date | Friday, September 30, 2022
#                |
#    Description | This program asks user to answer 16 questions,
#                | and then displays their 411/information in a  
#                | paragraph. Program continues to run until user  
#                | exits. Includes personalized information such 
#                | as gender pronouns, IQ message, and sibling 
#                | plural/singular form.                  

# Start while loop allowing user to continue or exit the program
while True:
    print("{:-^80}".format("The 411"))
    
    # Ask user if they would like to exit or continue
    exitPrgrm=input("Would you like to exit? If so, enter 'Y'/'Yes', to continue enter 'N'/'No'. ")
    
    # If user enters 'Y' or 'Yes' exit program
    if (exitPrgrm == "Y" or exitPrgrm == "Yes"):
        break
    
    # Else if user enters 'N' or 'No' continue program
    elif (exitPrgrm == "N" or exitPrgrm == "No"):
        
        # Ask 16 questions
        name = input("\nWhat is your name? ")
        school = input("\nWhat is the name of your school? ")
        
        # Starts while loop to error trap for gender 
        while True:
            gender = input("\nAre you a male or a female? Enter 'M'/'Male' or 'F'/'Female': ")
            
            # If user does not enter M, Male, F, or Female display error
            if (gender == "M" or gender == "Male" or gender == "F" or gender == "Female"):
                break
            print("Error! Enter either 'M'/'Male' or 'F'/'Female'.")
        
        # If user enters male store he/his pronouns in variables
        # store gender as male
        if (gender == "M" or gender == "Male"):
            gender = "male"
            pronoun_1 = "he"
            pronoun_2 = "his"
        
        # Else if user enters female store she/her pronouns in variables
        # store gender as female
        elif (gender == "F" or gender == "Female"):
            gender = "female"
            pronoun_1 = "she"
            pronoun_2 = "her"
        intelligenceQ = int(input("\nWhat is/believed to be your Intelligence Quotient (IQ)? Enter whole numbers. "))
        
        # If user enter's IQ greater than 115 notify that it is above average 
        if (intelligenceQ>115):
            IQ_resp = "that is an above average score"
        # Any under condition mention it is a very nice score
        else:
            IQ_resp = "a very nice score"
        height = float(input("\nIn feet, how tall are you exactly? "))
        
        # Starts while loop in case user enters unrealistic value for age
        while True:
            age = int(input("\nIn whole numbers, how old are you? Must be older than 0 and less than or equal to 122. "))
            
            # If age is less than 0 and greater than 122 print error message
            if (age>0 and age<=122):
                break
            print("\nError! Please enter value greater than 0 and less than 122.")
        fav_sport = input("\nWhat is your favourite sport? ")
        first_lang = input("\nWhat is your first language? ")
        num_brother = int(input("\nHow many brothers do you have? Enter whole numbers only. "))
        
        # If user enters 1, store brother in variable
        if (num_brother == 1):
            male_sibling = "brother"
        
        # Under any other condition store brothers in variable
        else:
            male_sibling = "brothers"  
        num_sister = int(input("\nHow many sisters do you have? Enter whole numbers only. "))
        
        # If user enters 1 store sister in variable
        if (num_sister == 1):
            female_sibling = "sister"
        
        # Under any other condition store sisters in variable
        else:
            female_sibling = "sisters"
        volunteerHr = int(input("\nHow many volunteer hours do you have? "))
    
        # Start while loop in case user enters invalid value
        while True:
            mark1 = int(input("\n[ENTER] first mark from course #1: "))
            mark2 = int(input("\n[ENTER] second mark from course #2: "))
            mark3 = int(input("\n[ENTER] third mark from course #3: "))
            mark4 = int(input("\n[ENTER] fourth mark from course #4: "))

            # If marks are greater than 100 or less than 0 tell user to enter valid value
            if (mark1 <= 100 and mark2 <= 100 and mark3 <= 100 and mark4 <= 100 and mark1 >= 0 and mark2 >= 0 and mark3 >= 0 and mark4 >= 0):
                break
            print("\nError! Please enter a valid value no greater than 100 and no less than 0.") 
        
        # Calculate mark average
        mrkAvg=(mark1+mark2+mark3+mark4)/4
        fav_sub = input("\nWhat is your favourite subject? ")  
        
        # Display the 411 based on the information user gave
        print("\nThis is {}, currently {} is {} years old and identifies as".format(name,pronoun_1,age))
        print("a {}. {} is the school {} attends, and {} favourite".format(gender,school,pronoun_1,pronoun_2))
        print("subject is {}! Last semester {} average was {:.2f}%,".format(fav_sub,pronoun_2,mrkAvg))
        print("and IQ stands at {}, {}. So far, {} has completed".format(intelligenceQ,IQ_resp,pronoun_1))
        print("{} volunteer hours. At {} feet, {} very much enjoys {} as {}".format(volunteerHr,height,pronoun_1,fav_sport,pronoun_2))
        print("favourite sport. Also, {} is {} first language, and {} family".format(first_lang,pronoun_2,pronoun_2))
        print("contains {} {} and {} {}.\n".format(num_brother,male_sibling,num_sister,female_sibling))
        
