#!/usr/bin/env python
# coding: utf-8

# In[10]:


#This program makes a diamond shape with a given width and string to use
def diamond(w,inString):
    #By a given width, we can find the height needed
    h = int((w+1)/2)
    output = ""
############################################## --- Making the string into a list
    inList = []
    for i in inString:
        inList.append(i)
################################################# --- Making the diamond top  
    x = 0
    counter = 0
    switch = True
    #The switch turns off the first while loop once it is done making
    #the top, which turns on the second while loop
    while switch:
        for x in range(h):
            track = h-x
            #Track is meant to be a tracking value for the values that I need of each progressing line
            output += (track-1)*" "    
            for i in range(w-2*(track-1)):
                output += inList[counter]
                counter += 1
                #The counter here is to dictate which index of the string to print
                if counter == len(inString):
                    counter = 0
            output += "\n"
        switch = False
############################################## --- Making the diamond bottom
    while not switch:
        for x in range(1,h):
            output += (x)*" "    
            for i in range(w-2*x):
                output += inList[counter]
                counter += 1 
                if counter == len(inString):
                    counter = 0
            output += "\n"
        break
    return output


# In[ ]:




