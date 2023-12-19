#!/usr/bin/env python
# coding: utf-8

# ***
# <p style ="text-align: center"><font size="7"><span style="color:purple">Welcome To our Solar-System🌞</span></font></p>

# ![a54b26aaead6b77c811de8f9c8889f6d.jpg](attachment:a54b26aaead6b77c811de8f9c8889f6d.jpg)

# ***
# <font size="4"><span style ="color:red">**Solar System:**</span><span style ="color:green"> **assemblage consisting of the**</span>.<span style ="color:orange"> **Sun**</span><span style ="color:green"> **—an average star in the Milky Way Galaxy and those bodies orbiting around it:**</span>.<span style ="color:blue"> **8 (formerly 9) planets**</span>.<span style ="color:green">— with more than **210** known planetary **satellites (moons)**; many **asteroids**, some with their own **satellites**; **comets** and other **icy bodies**; and vast reaches of **highly tenuous gas** and dust known as the **interplanetary medium**.</span></font>.

# ***
# <p style="text-align: center;"><font size="6"><span style = "color:purple">Now Lets Start!!</span></font></p>
# 
#                                          🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
# 
# 
# <div class = "alert alert-info"><p style="text-align: center;"><font size="5"><span style = "color:BLUE">Lets!!Check your *BASIC* Knowledge regarding Solar-System💡</span></font></p>
# 
# 

# In[8]:


from colorama import Back,Fore,Style # using colorama to change the front , back color of the output text 
import winsound  # using winsound to play the background sound 
inputFile = open("solar mcq.txt","r") # open and reading a file containing all the data rlate dto MCQ'S 
file1 = open("userAnswer Record.txt", "w") # Writing the userInput into the file 
inputFile2 = open("Answer sheet.txt" , "r")# Chechking the answers from file by comparing the userInput 
words= inputFile.readlines() # store or read data in words
answers = inputFile2.readline() # store or read every answer in answers
count=0
grade=0
i = -1
space ="\t\t\t\t\t"
result = "Multiple Choice Questions (MCQ'S)"
def decore():
 print(Fore.RED+"--"+"-"*len(result)+"--"+"\n"+"- "+" "*len(result)+""+" -")
 print(Fore.RED+"- "+Style.RESET_ALL+result+Fore.YELLOW +""+" -"+"\n"+"- "+" "*len(result)+""+" -"+"\n"+"--"+"-"*len(result)+"--"+"\n")
decore()
print(Style.RESET_ALL)
print(space+Back.CYAN+"<<<<<<<<< Each carry 10 marks >>>>>>>>>")
#print("\N{smiling face with sunglasses}")
print(Style.RESET_ALL)
for s in range(0, 72): # for loop to loop over every line of the file 
 if(s%6!=0 or s==0): # just printing the 6 lines of the file containing the question and the options 
  print(words[s])
 else:              # else for prompting the user for answer the question  
  if(s<=60):
   count=count+1
   i = i+1
   print(Back.YELLOW+"Answer: " ,count)
   print(Style.RESET_ALL)
   userInput = input("Enter the Answer here:") 
   print(Back.RED+ "****Your Answer has been saved****") 
   # here , answer has been save dor written to the Useranswer record file to save as record
   print(Style.RESET_ALL)
   file1.writelines(userInput+" -----Your Answer\n")
   winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
   # Play system level sound after answer saved or before displaying the next Question
   print(words[s])
   if(userInput==answers[i]):# here checking the answer of the user enters if the answer is correct then the if statement will 
    #executed and grade will add by ten . 
     grade = grade+10
     if(i<9):
      # another if statement will be printing the current scores . Basically use to print the final gardes after the tenth question
      print(space,grade, Back.CYAN+"--------This is your current Grades--------")
      print(Style.RESET_ALL)
     else:
        print(space,grade, Back.GREEN+"******* This is your Final Grades ********")
        print(Style.RESET_ALL)
     
   else: # similar steps if the answer is wrong print the current score if the 10th question print the final grades 
     grade = grade+0
     if(i<9):
      print(space,grade, Back.CYAN+"--------- This is your current Grades---------")
      print(Style.RESET_ALL)
     else:
      print(space, grade, Back.GREEN+" ******* This is your Final Grades ********")
      print(Style.RESET_ALL)  
        
 #here , another if-else statement to give feedback what user earned . Special here is I use Emoji in the code to print out.
# I just use the simple format and the name of the emoji's in string to print out in output feedback . 
if(grade<=20):
    print(Back.BLACK+Fore.WHITE+"Sorry!!"+"\N{unamused face}"+" but Your knowledge regarding solar-system is so **weak**...")
if(grade>20 and  grade<=50):
   print(Back.BLACK+Fore.WHITE+"Nice !! "+"\N{slightly smiling face}"+" Your knowledge regarding solar-system is **Good**...")
if(grade>50 and grade<100):
   print(Back.BLACK+Fore.WHITE+"Great!!!"+" \N{grinning face}"+" Your knowledge regarding solar-system is **Awesome**")
if(grade==100):
    print(Back.BLACK+Fore.WHITE+"Awesome!!!"+" \N{smiling face with sunglasses}"+" Your knowledge regarding solar-system is **Proficient**")


#  <p style ="text-align: center"><font size="5"><span style="color:purple">Lets Move Forward...</span></font></p>

# <p style ="text-align: center"><font size="5"><span style="color:purple">Hey! Do you wanna listen the sounds of Objects in our solar system.</span></font></p>

# In[4]:


from IPython.display import YouTubeVideo # using Ipython module and impotinh YouTubeVideo to display and play a Youtube Video 

youtube_video= YouTubeVideo('Y295gW-D3sc') # Decalring a variable and passing Video ID as an argument to the YouTubeVideo method

display(youtube_video) # giving command to display the video


# <div class = "alert alert-success"><p style ="text-align: center"><font size="5"><span style="color:GREEN">WOW!! Did you enjoy the video. That was AMAZING!! </span></font></p></div

# <div class = "alert alert-warning"><p style ="text-align: center"><font size="3"><span style="color:orange">Now, If you want to know more about the astronomical properties of your desired planet.Then, my next program will help you regarding this. </span></font></p></div

# In[4]:


import pandas as pd  # here I use pandas module to print the specific rows and column of the excel sheet 
from colorama import Back,Fore,Style
define= open("define planet.txt", "r") # here is a fle containing the data containing facts related to planets 
description = define.readlines()
print(Back.CYAN+"Please! write the name of the planet you want to study first")
print(Style.RESET_ALL)
userInput = input(Back.YELLOW+"Please enter here......") # prompting the user to enetr the name of the planets 
print()
space = "\t\t\t\t\t\t\t"
print(Back.RED+space+ userInput+space+"\t")
print(Style.RESET_ALL)
words = pd.read_excel('planet velocity.xlsx') # excel file containing the data related to the astronomical properties of  each planets 
print(Style.RESET_ALL)
userInput=userInput.lower()
if(userInput=="mercury"):
    print(words.loc[:,["Column1","Column2"]]) # syntax to print specific rows and columns using label indexing using the name of
    # columns to access them 
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!") # printing the facts related to the specific planets 
    print(Style.RESET_ALL)
    print("\n",description[0])
elif(userInput=="venus"):
    print(words.loc[:,["Column1","Column3"]])
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!")
    print(Style.RESET_ALL)
    print("\n",description[1])
elif(userInput=="earth"):
    print(words.loc[:,["Column1","Column4"]])
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!")
    print(Style.RESET_ALL)
    print("\n",description[2])
elif(userInput=="moon"):
    print(words.loc[:,["Column1","Column5"]])
elif(userInput=="mars"):
    print(words.loc[:,["Column1","Column6"]])
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!")
    print(Style.RESET_ALL)
    print("\n",description[3])
elif(userInput=="jupiter"):
    print(words.loc[:,["Column1","Column7"]])
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!")
    print(Style.RESET_ALL)
    print("\n",description[4])
elif(userInput=="saturn"):
    print(words.loc[:,["Column1","Column8"]])
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!")
    print("\n",Style.RESET_ALL)
    print(description[5])
elif(userInput=="uranus"):
    print(words.loc[:,["Column1","Column9"]])
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!")
    print(Style.RESET_ALL)
    print("\n",description[6])
elif(userInput=="neptune"):
    print(words.loc[:,["Column1","Column10"]])
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!")
    print(Style.RESET_ALL)
    print("\n",description[7])
elif(userInput=="pluto"):
    print(words.loc[:,["Column1","Column11"]])
    print("\t\t\t\t\t\t\t"+Back.GREEN+" FACTS!!!")
    print(Style.RESET_ALL)
    print("\n",description[8])
else:
    print(Back.YELLOW+"Please!! Enter the valid Planet names.")  # else statements if the enetred name is not valid 
    
    
print()




# <p style ="text-align: center"><font size="5"><span style="color:purple">I hope You like this class.</span><span style="color:magenta"></span></font></p>
# 
# ***
# 
# <p style ="text-align: center"><font size="7"><span style="color:purple">Thank You👍</span><span style="color:magenta"></span></font></p>
# 

# In[ ]:




