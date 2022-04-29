from string import ascii_letters, digits

import random, time, re

#Contamos la ocurrencia de los asteriscos
def asteriskDetector(target):

    c = target.count("*")
    return c


#Imprimir el baner de cabecera
GREEN, RESET = "\033[92m", "\033[0m"

char = lambda i: " ".join(random.sample(ascii_letters + digits, k=i)).upper()

def shuffle(line, name_length):

    for x in range(0, random.randint(1, 9)):
        print("\t{}".format(char(name_length)), end="\r")
        time.sleep(0.4)

    print("\t" + line)

def print_banner(name="Asterisk & Obelix", version="01.00.00", author="Jorge Coronado (aka @JorgeWebsec)"):

    print("""
    
               _            _     _                    ____  _          _ _      
     /\       | |          (_)   | |          ___     / __ \| |        | (_)     
    /  \   ___| |_ ___ _ __ _ ___| | _____   ( _ )   | |  | | |__   ___| |___  __
   / /\ \ / __| __/ _ \ '__| / __| |/ / __|  / _ \/\ | |  | | '_ \ / _ \ | \ \/ /
  / ____ \\__ \ ||  __/ |  | \__ \   <\__ \ | (_>  < | |__| | |_) |  __/ | |>  < 
 /_/    \_\___/\__\___|_|  |_|___/_|\_\___/  \___/\/  \____/|_.__/ \___|_|_/_/\_\
                                                                                 
                                                                                 
    """)

    name_length = len(name) + 4  
    name = " ".join(name.upper())  
    name = "{} \033[1m{} \033[0m{}".format(char(2), name, char(2))

    print("\n")
    lines = [char(name_length), name, char(name_length)]
    [shuffle(line, name_length) for line in lines]
    print("\n\t{}".format(author))
    print("\t{}\n".format(version))

    #Verificamos el email
def check_email(email):

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False