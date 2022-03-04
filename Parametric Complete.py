from math import *
from turtle import *
from random import *
from os import *
from PIL import Image
from imageio import *
from time import *

#---------------------Questionaire
response_init = str.upper(input("Do you want to make multiple random graphs? (Y/N): "))
if response_init == "Y":
    makegif_reps = int(input("How many randomly generated .gifs do you want to make?: "))
elif response_init == "N":
    makegif_reps = 1
else:
    print("Invalid Response.")
    exit()
#---------------------Questionaire
    
#----------------------------------------------------Functions--------------------------------------------------------

def initialization(initial_response:str) -> list:
    if initial_response == "Y":
        response_g = "Y"
        gif_name = f"{usable_time}_Random_{gif_count}"
    if initial_response == "N":
        response_g = None
        gif_name = None
    return(response_g, gif_name)

def graph_points_list(t, x_t_equation:str, x_scaler:int, y_t_equation:str, y_scaler:int, movement_size:float) -> list:
    L=[]
    for i in range(3):
        x = x_scaler * eval(x_t_equation)
        y = y_scaler * eval(y_t_equation)
        temporary_L = [t,x,y]
        L.append(temporary_L)
        t+= movement_size
    point_previous, point_current, point_next = L
    #print(f"{point_current[0]/20*pi:.4%}")  #loading % every loop
    return(point_previous, point_current, point_next)

def slope(point_1:list, point_2:list) -> list:   #points in this program are defined by [t,x,y]
    rise = point_2[2] - point_1[2]
    run=point_2[1] - point_1[1]
    if run == 0:
        slope = 900000000000000.0
    else:
        slope = rise / run
    return(rise, run, slope)

def distance(rise:float, run:float) -> float:
    dist = sqrt(rise * rise + run * run)
    return(dist)

def heading_angle(run:float, slope:float) -> float:           
    if run>0:
        theta = atan(slope) * (180 / pi) + 180
    else:
        theta = atan(slope) * (180 / pi)
    return(theta)
        
def loading_bar_single_hundredth(loop_current:int, loops_total:int):
    if loop_current % (round(loops_total / 100)) == 0:
        print(f"{ceil(loop_current+1)/loops_total:.0%}")

def three_phase_color_shift(parameter:float):
    rgb_cycle_list = []
    rgb_cycle_list.clear()
    colormode(255)
    for i in range(3):
        cycle_color = int(255 * cos(parameter + i * pi / 3) ** 2)
        if cycle_color > 255:
            cycle_color = 255
        if cycle_color < 0:
            cycle_color = 0
        rgb_cycle_list.append(cycle_color)
    pencolor(rgb_cycle_list[0], rgb_cycle_list[1], rgb_cycle_list[2])
        
def screencap():   
    getcanvas().postscript(file = f"epic_{loop:010d}.eps") 
    
def delete_all_files_srt_with(startwith:str):
    del_list = []
    for file in listdir(mydir):
        if file.startswith(startwith):
            del_list.append(file)
            remove(file)
    print(f"{del_list} files deleted.")
#----------------------------------------------------Functions--------------------------------------------------------
       
#--------------------------------------------------Full Program-------------------------------------------------------
    
for gif_count in range(makegif_reps):       
    usable_time = strftime(f"%Y%j%H%M%S")    
    response_g, gif_name = initialization(response_init)
    
#---.eps doesn't capture bgcolor()
    pencolor("Black")
    pensize(10000)
    forward(1)
    left(180)
    forward(1)
    left(180)
#---.eps doesn't capture bgcolor()
    
#---Turtle Initialization
    bgcolor("black")
    penup()
    speed(0)
    colormode(255)
    setup(1700, 900, 2100, 85) #Turtle window size
    setposition(0, 0)
    pendown()
#---Turtle Initialization
    
#---Main Variables
    mydir = chdir(r"C:\Users\Brandon\Documents\Thonny doc\Gif compile folder (don't touch)")
    pensize(1)
    y_s = 160                 #Graph size y-scaler
    x_s = 250                 #Graph size x-scaler 
    step_size = .0001          #Stepsize scaler 
    gif_length = 7            #Length in sec
    v = 100                    #Graph density scaler
    number_of_frames = (150)  #Minimum frame count
    right(int(0))             #Graph angle
    t = float(0)              #Initial t
    save_rate = 100           #memory bank size (DNT)
#---Ajustable ^ static v
    dura = gif_length / number_of_frames
    loops = ceil((2 * pi / step_size))
    screencap_rate = floor(loops / number_of_frames)
    picture_set = []
    all_gifs = []
    number_of_gifs_created_counter = 0
    response = None
    response_special_case = None
#---Main Variables
    
#---RNG list + 2π
    R_2 = []
    for i in range(7):
        temprand = randint(1, 6)
        R_2.append(temprand)
    R_2.append(2 * pi)
    R_pi = sample(R_2, 8)
#---RNG list + 2π
    
#---Drawing Parameters
    if response_init != "Y":
        listen()
        response_rng = str.lower(textinput("Control Window","Random equation or Typed? (rand, type): "))
        if response_rng != "type" and response_rng != "rand":
            print("Invalid Response.")
            exit()
        if response_rng == "type":
            x_t = textinput("Input a function of t","x(t)= ")
            y_t = textinput("Input a function of t","y(t)= ")
    if response_init == "Y" or response_rng == "rand":
        x_t = str("sin(R_pi[0]*t*v)*cos(R_pi[1]*t*v)-cos(R_pi[2]*t*v)*sin(R_pi[3]*t*v)")        
        y_t = str("sin(R_pi[4]*t*v)*cos(R_pi[5]*t*v)-cos(R_pi[6]*t*v)*sin(R_pi[7]*t*v)")
    if response_init == "Y":
        gif_name = f"{usable_time}_Random_{gif_count}"
#---Drawing Parameters
        
#-----------------------------------Drawing Loop
    for loop in range(loops):
        loading_bar_single_hundredth(loop, loops)
#-------Draw Parametric
        point_triple = graph_points_list(t, x_t, x_s, y_t, y_s, step_size)
        
        rr_slope1 = slope(point_triple[0], point_triple[1])
        theta1 = heading_angle(rr_slope1[1], rr_slope1[2])
        
        rr_slope2 = slope(point_triple[1], point_triple[2])
        theta2 = heading_angle(rr_slope2[1], rr_slope2[2])
        
        dist = distance(rr_slope2[0], rr_slope2[1])

        left(theta2 - theta1)
        forward(dist)
                        
        t+= step_size
        
        three_phase_color_shift(t)
#-------Draw Parametric
        
#-------Screencap                
        if (response_g != "N" and (loop + 1) % screencap_rate == 0):
            screencap()
            picture_set.append(imread(f"epic_{loop:010d}.eps"))
            remove(f"epic_{loop:010d}.eps")
                    
        if len(picture_set) == save_rate and response_g == None:
            listen()
            response_g = str.upper(textinput("Control Window", "Process a gif? (Y/N): "))
        
        if response_g == "N": 
            picture_set.clear()
            
        if response_g == "Y" and gif_name == None:
            gif_name = "temporary name"                
     
        if (response_g == "Y" and len(picture_set) % save_rate == 0 and picture_set != []):            
            number_of_gifs_created_counter += 1
            mimsave(f"temp_{gif_name}_{number_of_gifs_created_counter}.gif", picture_set, duration=dura)   #pictures -> gif
            picture_set.clear()            
#-------Screencap
#-----------------------------------Drawing Loop
            
#-----------------------------------Finishing Steps            
#---Create temp_gif from screenshots
    if response_g == "Y" and picture_set != []:
        number_of_gifs_created_counter += 1
        mimsave(f"temp_{gif_name}_{number_of_gifs_created_counter}.gif", picture_set, duration=dura)
    
    if response_g == None and gif_name == None:
        response_special_case = str.upper(textinput("Control Window", "Want to make a gif? (Y/N): "))        
        if response_special_case == "Y":
            number_of_gifs_created_counter += 1
            gif_name = textinput("Graph Naming Window", "Name Graph")
            mimsave(f"temp_{gif_name}_{number_of_gifs_created_counter}.gif", picture_set, duration=dura)
#---Create temp_gif from screenshots
#---list of all temp_gifs in order            
    for i in range(number_of_gifs_created_counter):
        all_gifs.append(f"temp_{gif_name}_{i+1}.gif")
#---list of all temp_gifs in order
        
#---Single Graph Options        
    if response_init != "Y":
        while response != ("save" or "end") and response_g == "Y":
            response = str.lower(textinput("Control Window", "Do you want to save your gif or end the program (save/end): "))
            if response == "end":
                delete_all_files_srt_with("temp_")
                exit()
            if response == "save":
                gif_name = textinput("Control Window","Name: ")
                print(f"{gif_name}")
                if response_rng == "rand":
                    print(f"x(t)= sin({R_pi[0]*v}*t)*cos({R_pi[1]*v}*t)-cos({R_pi[2]*v}*t)*sin({R_pi[3]*v}*t)))")
                    print(f"y(t)= sin({R_pi[4]*v}*t)*cos({R_pi[5]*v}*t)-cos({R_pi[6]*v}*t)*sin({R_pi[7]*v}*t)))")
                if response_rng == "type":
                    print(x_t)
                    print(y_t)
            if response != ("save" or "end"):
                print("Invalid Response")
#---Single Graph Options
                
#---Temporary gifs into single    
    gif_data = get_reader(all_gifs[0])                     #this is needed to get num_frames
    num_frames = gif_data.get_length()
    new_gif = get_writer(f"Complete_{gif_name} {loops}_loops {screencap_rate}_rate.gif", duration = dura)

    for i in range(len(all_gifs) - 1):                     #Ignores the last gif
        gif_data = get_reader(all_gifs[i])                 #Adds all the frames from each gif to a bigger new_gif
        for frames in range(num_frames):
            new_gif.append_data(gif_data.get_next_data())
        print(f"{i+1/(len(all_gifs)):.2%} Done with {gif_name}'s final build")

    gif_data = get_reader(all_gifs[-1])                    #Appends the last gif
    num_frames = gif_data.get_length()
    for frames in range(num_frames):
        new_gif.append_data(gif_data.get_next_data())
    print(f"100% finished - Complete_{gif_name} {loops}_loops {screencap_rate}_rate.gif")    
#---Temporary gifs into single
    
#---Cleans Up Temporary Files        
    gif_data.close()
    new_gif.close()
    picture_set.clear()
    all_gifs.clear()
    delete_all_files_srt_with("temp_")
#---Cleans Up Temporary Files
    
#---Resets for the next graph    
    print(f"Done with {(gif_count + 1)}/{makegif_reps} .gifs.")
    if response_init == "Y":
        reset()
#---Resets for the next graph
        
#---Closes When done         
    if gif_count+1 == makegif_reps:
        delete_all_files_srt_with("epic_")
        bye()
        print("Completely done")
        exit()
#---Closes When done         
#-----------------------------------Finishing Steps