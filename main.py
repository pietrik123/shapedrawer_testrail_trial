# version
version = "1.0.0"

# log levels definitions
ERROR = 1
WARNING = 2
INFO = 3
DEBUG = 4

loglevel_txt_map = {ERROR : "ERROR", WARNING : "WARNING", INFO : "INFO", DEBUG: "DEBUG"}

# setup logger, open main log file
import time
log_timestamp_str = str(time.strftime("%Y%m%d_%H%M%S"))
f = open("logfile_" + log_timestamp_str + ".log", "w")

# load default configuration
log_level = DEBUG
character = "*"
# load configuration from file
try:
    file_cfg = open("shapedrawer.config","r")
    lines = file_cfg.read().splitlines()
    for l in lines:
        tokens = l.split("=")
        if tokens[0] == "char":
            character = tokens[1]
        elif tokens[0] == "loglevel":
            try:
                log_level = int(tokens[1])
            except:
                log_level = DEBUG
        else:
            log(INFO, "unsupported configuration: {}".format(l))
    file_cfg.close()
except:
    print("could not find configuration file shapedrawer.config!")
    log(ERROR, "could not find configuration file shapedrawer.config")
    log(INFO, "will use default values")

# logging functions
def log(msg):
    f.write(msg)
    
def log(level, msg):
    if level <= log_level:
        f.write(str(loglevel_txt_map[level]) + ":" + msg + "\n")

# program functions
def display_menu():
    log(DEBUG, "displaying menu")
    print("\nMain menu")
    print("\n1. Draw triangle.")
    print("2. Draw rectangle.")
    print("3. Exit.\n")

def draw_triangle(a):
    log(INFO, "drawing triangle")
    log(DEBUG, "drawing triangle {}".format(a))
    max_len = 7
    a = int(a)
    if a > max_len:
        log(DEBUG, "value to big")
        print("Too big. Max len of a is" + str(max_len))
    else:
        shape = "\n"
        for i in range(1, a+1):
            for j in range(0, i):
                shape += character
            shape += "\n"
        print(shape + "\n")
            
def draw_rectangle(a,b):
    log(INFO, "drawing rectangle")
    log(DEBUG, "drawing rectangle {}, {}".format(a,b))
    max_len = 7
    a = int(a)
    b = int(b)
    if (a > max_len or b > max_len):
        log(DEBUG, "value to big")
        print("Too big. Max len of a and b is" + str(max_len))
    else:
        shape = "\n"
        for i in range(0, b):
            for j in range(0, a):
                shape += character
            shape += "\n"
        print(shape + "\n")

  
log(INFO,"ShapeDrawer {}".format(version))
print("ShapeDrawer v.", version)

exit = 0

# main loop
log(DEBUG, "entering main loop")
while exit == 0:
    display_menu()
    inp = input("Choice: ")
    log(DEBUG, "user input".format(input))
    if '3' in inp:
        log(INFO,"exiting application")
        exit = 1
    elif '1' in inp:
        a = input("Enter a: ")
        draw_triangle(a)
    elif '2' in inp:
        a = input("Enter a: ")
        b = input("Enter b: ")
        draw_rectangle(a,b)
    else:
        print("Incorrect input")

# close file logger        
f.close()
    
    
    
