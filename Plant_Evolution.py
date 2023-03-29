import random
import turtle
plant = turtle.Turtle()
sc = turtle.Screen()
sc.setup(600, 600) #seting up the screen size
sc.mode('world') 
 
# set world coordinates
turtle.setworldcoordinates(-300, -300, 300, 300) #assigning the coordinates to start from the drawing will start 

# plant.setworldcoordinates(-300, -100, 300, 100)
plant.goto(0, 0)
#plant.speed(0)


#creating the function to generate the variations 
def generate_var(dict_para, variation_dict): # to generate the variations taking arguments of the perivious parameters and the range of variations in which the change will take place
    #list_parameters= ['length_root','length_branch','len_leaf','length_stem']
    dict_new_para = {} #creating a new dictionary in which the generated values of variations will stored
    for para in dict_para.keys(): # for every parameter in the keys dictionary 


        var_range = variation_dict[para] # change the values in the range assigned to each parameter in the variation dictionary
        dict_new_para[para] = -1    # making the python to count from 1 and not from 0

        while dict_new_para[para] < 0:  # making a while loop till the time the value of parameter after making the varition is not above the 0
            dict_new_para[para] = dict_para[para] + random.uniform(-var_range, var_range)  #adding the change created according to the assigned range of the parameters 

    return dict_new_para # then returing the new set of valuse of the parameters in the dictinory


 
 #code for writing text in turtle for the figures numbering
turtle.penup()
turtle.left(90)
turtle.forward(140)
turtle.pendown()
turtle.write("OG          1               2              3             4              5", move=False, align='center', font=('Arial', 15, 'normal'))
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.write('Type one of the variation and remember the no assign to it',move=False, align='center', font=('Arial', 12, 'normal'))
 # the code above is written by Suraj and Irfan of the functions for generating the variations and writing the text in turtle.



#the code below of drawing the plant is written by Yash and Pratik
def draw_plant(dict_of_tree_para,plant):
    length_stem = dict_of_tree_para["stem_len"]
    len_leaf = dict_of_tree_para['leaf_len']
    length_branch = dict_of_tree_para['branch_len']
    length_root = dict_of_tree_para['root_len']
   

    plant.penup()
    plant.left(180)
    plant.forward(300)
    plant.right(180)
    plant.pendown()
    # plant.goto(-200, 0)
    plant.speed(0)#for increasing the speed at which turtle is drawing.
    

    #plant.color("#B8860B")
    
    base_value = [length_stem,len_leaf,length_branch,length_root]
    #for ground 

    plant.forward(40)#turtle moves forward
    #for stem

    plant.left(90) #angle changes according to the direction and the magnitude
    plant.forward(length_stem * 2)#stem length until 1 branch
    #for branch 1
    plant.left(45)
    plant.forward(length_branch) #branch length
    #for leaf triangle of branch 1

    plant.color('#458B74')#giving colour to leaves
    plant.left(90)
    plant.forward(len_leaf)
    plant.right(120)
    plant.forward(len_leaf * 2)
    plant.right(120)
    plant.forward(len_leaf * 2)
    plant.right(120)
    plant.forward(len_leaf)
    #tracing branch so it can come again to stem
    plant.color('#B8860B')#again giving back the brown colour
    plant.left(90)
    plant.forward(length_branch)
    #for stem length until branch 2
    plant.left(135)
    plant.forward(length_stem*2)
    #for branch 2
    plant.left(45)
    plant.forward(length_branch)
    #for leaf triangle of branch 2
    plant.color('#458B74')
    plant.left(90)
    plant.forward(len_leaf )
    plant.right(120)
    plant.forward(len_leaf * 2)
    plant.right(120)
    plant.forward(len_leaf * 2)
    plant.right(120)
    plant.forward(len_leaf )
    #tracing branch so it can come again to stem
    plant.color('#B8860B')
    plant.left(90)
    plant.forward(length_branch)
    #for stem length until top of the stem
    plant.left(135)
    plant.forward(length_stem)
    #for tracing back to branch 3 
    plant.right(180)
    plant.forward(length_stem*2)
    #for branch 3
    plant.left(135)
    plant.forward(length_branch)
    #for leaf triangle of branch 3
    plant.color('#458B74')
    plant.left(90)
    plant.forward(len_leaf )
    plant.right(120)
    plant.forward(len_leaf * 2)
    plant.right(120)
    plant.forward(len_leaf * 2)
    plant.right(120)
    plant.forward(len_leaf )
    #tracing branch so it can come again to stem
    plant.color('#B8860B')
    plant.left(90)
    plant.forward(length_branch)
    #for stem length until branch 4
    plant.left(45)
    plant.forward(length_stem*2)
    #for branch 4
    plant.left(135)
    plant.forward(length_branch)
    #for leaf triangle of branch 4
    plant.color('#458B74')
    plant.left(90)
    plant.forward(len_leaf )
    plant.right(120)
    plant.forward(len_leaf * 2)
    plant.right(120)
    plant.forward(len_leaf * 2)
    plant.right(120)
    plant.forward(len_leaf )
    #tracing branch so it can come again to stem
    plant.color('#B8860B')
    plant.left(90)
    plant.forward(length_branch)
    # for stem till the ground
    plant.left(45)
    plant.forward(length_stem)

    #for ground 
    plant.left(90)
    plant.forward(40)
    #for tracing back the ground to form root
    plant.right(180)
    plant.forward(50)
    #for root
    plant.left(110)
    plant.forward(length_root)
    plant.right(90) #for root fibres
    plant.forward(5) 
    plant.left(180)
    plant.forward(5)
    plant.right(90) #again for roots
    plant.forward(length_root)
    plant.right(90) #for root fibres
    plant.forward(5) 
    plant.left(180)
    plant.forward(5)
    plant.right(90)
    plant.forward(length_root)
    plant.right(180)
    plant.forward(length_root*3)
    plant.right(110)
    plant.forward(20)
    plant.right(110)
    plant.forward(length_root)
    plant.left(90)
    plant.forward(5)
    plant.right(180)
    plant.forward(5)
    plant.left(90)
    plant.forward(length_root)
    plant.left(90)
    plant.forward(5)
    plant.right(180)
    plant.forward(5)
    plant.left(90)
    plant.forward(length_root)
    plant.right(180)
    plant.forward(length_root *3)
    plant.left(110)
    plant.right(180)
    plant.forward(40)
    plant.penup()
    plant.forward(314)
    plant.pendown() 
   
    # plant.forward(length_root*3)
    # plant.right(110)
    # plant.forward(40)
    # plant.forward(length_root*3)
    # plant.right(110)
    # plant.forward(30)

# below code is written by Suraj/Irfan & Yash/pratik
#the dictonary of the parameters who's value we are changing always to draw the plant.
dict_of_trees = {"stem_len":14 , "leaf_len":12 , "branch_len":30 , "root_len":10}
#the dictonay of the parameters with value of range in which the change will take place. 
variation_dict = {"stem_len":4,"leaf_len":2, "branch_len":1 , "root_len":3}
    #length_root': 3,'length_branch':1,'len_leaf':2,'
#calling the function to draw the plant with assigned values of the parameters
draw_plant(dict_of_trees,plant)


# below code is written by Suraj and Irfan

#making a condition so that the program enters the while loop and only comes out when the condtion is not satisfied = False.
not_satisfied = True
dict_old_para = dict_of_trees #
while not_satisfied:
    num_input = 0 # setting the num_input=0 so that the program enters the second while loop and asks the user to 'enter the fig no'. 
    children =[] # creating a list where every time the new sets of values which are generated in the function as dictonary can stored and called when drawing them 
    for i in range(5): # runing the for loop for 5 times to generate 5 different values for the paratmeters 
        children.append(generate_var(dict_old_para,variation_dict)) # after generating the 5 values for the paratmeters then adding them to the main dictonary in the a list children

# print(children)
    
    for child in children: # taking the each item from the list as child 
    # draw_tree(child)
        draw_plant(child,plant) # calling the function to draw the plant with each child items new values of parameters.
        
    

# new_parent = children[usr_choice - 1]
    ### Plotting the first tree and five variations here
    ### 
    turtle.reset() #ending the starting text
    while num_input not in [1, 2, 3, 4, 5]:
        num_input = int(input("Enter the fig no.:   ")) # asking the user to enter the fig no with which he wants to go ahead.
        if num_input <= 5 and num_input > 0:# Condition for the input value to be from 1 to 5 
            dict_old_para=children[num_input-1] # as python counts from 0 so putting -1 so that if the user inputs fig no 2 then the pyton will take the value of fig no 2 only and not the 3rd one
            satisfy_input = input("Are you satisfied? (y/n)")  # after the user have inputed the fig no then asking him about that does he wnats to stop their or wants to go ahead by asking him the statement "are you staisfied"
            
            if satisfy_input == "y": # if the user answers Y then the condition is satisfied as false and the while loop ends.
                not_satisfied = False
            
            elif satisfy_input== 'n':  #if the user answers n then it will again repeat the while loop and generate the variations and again draw them. 
                plant.goto(50, 0) # clearing the earlier drawn images and showing just the new ones.
                plant.clear()# clear the priviously drawn images
        else:
            print("Enter a fig no between 1 to 5")# prints the input when the input value is not from 1 to 5
    
    
if not_satisfied == False: # if the not_satisfied == false 
    # Code for writing text for the end part 
    turtle.penup()
    turtle.right(90)
    turtle.forward(140)
    turtle.pendown()
    turtle.write("      Original plant      After evolution", move=False, align='center', font=('Arial', 15, 'normal'))
    
    plant.goto(225, 0)  # assigning the postion to start to draw the plants

    plant.clear() # clear the priviously drawn images
    draw_plant(dict_of_trees,plant)  # draw the plant with base values with which the program started
    draw_plant(dict_old_para,plant) # draw the plant which the user have selected with it values  
    



turtle.done() # close the turtle