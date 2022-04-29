from ctypes import util
from tabnanny import check
#import m.intelx as ix
import m.utils as utils

import time
from validate_email import validate_email

def main():

    #Imprimimos el banner
    utils.print_banner()

    #Obtenemos el target
    target = input("Insert email with asterisk: ")

    check_target = utils.asteriskDetector(target)
    if check_target:
        pass
    else:
        print("Plis insert a correct email.")

    #Contamos los asteriscos y lo imprimimos en pantalla
    asterisk_count = utils.asteriskDetector(target)
    print(f"{asterisk_count} asterisks have been detected.")

    #Recogemos los datos del objetivo
    name = input("Insert target name: ")
    last_name = input("Insert last name: ")
    birt = input("Insert year of birth: ")

    #Recogemos nexos para relacionar datos con intelx
    #phone = input("Insert phone number: ")
    #city = input("Insert city: ")
    #country = input("Insert country: ")
    username = input("Insert username: ")

    #Contamos la longitud de cada datos
    c_name = len(name)
    c_last_name = len(last_name)
    c_birt = len(birt)
    c_username = len(username)

    #Esperamos 2 segundos
    #time.sleep(2)

    #Detectamos el total del username
    target_split = target.split("@")
    c_email_username = target_split[0]
    c_email_username = len(str(c_email_username).replace("'",""))

    #Obtenemos el dominio
    domain = target_split[1]
    print(f"The domain used in the email is {domain}")

    #Detectamos las letras expuestas en el username
    target_asterisk_split = target.split("*")
    exposed = str(target_asterisk_split[0]).replace("'","")
    print(f"The exposed letters are: {exposed}")

    #Creamos una lista de emails que verificaremos posteriormente
    emails = []

    #Si lo expuesto aparece en el nombre
    if exposed in name:
        print("The exposed letters match the name...")
        #Si lo expuesto es igual al nombre
        if exposed == name:
            print("The exposed letters are the same as the name...")
            if c_name + c_last_name == c_email_username:
                em = f"{name}{last_name}@{domain}"
                emails.append(em)
            if c_name + c_last_name + 1 == c_email_username:
                em = f"{name}.{last_name}@{domain}"
                emails.append(em)
                em = f"{name}_{last_name}@{domain}"
                emails.append(em)
            if c_name + c_last_name + c_birt == c_email_username:
                em = f"{name}{last_name}{birt}@{domain}"
                emails.append(em)
            if c_name + c_last_name + c_birt - 2 == c_email_username:
                em = f"{name}{last_name}{birt[2:4]}@{domain}"
                emails.append(em)
            #Si el nombre aparece en el username
            if name in username:
                #si el username tiene el mismo tamaño que el email
                if c_username == c_email_username:
                    em = f"{username}@{domain}"
                    emails.append(em)
            if 1 + c_last_name == c_email_username:
                letter = name[0]
                em = f"{letter}{last_name}@{domain}"
                emails.append(em)
        else:
            d1 = input("Are the exposed letters part of the name? Y/n: ")
            if d1 == "y" or d1 == "Y" or d1 == "yes" or d1 == "Yes":
                if c_name + c_last_name == c_email_username:
                    em = f"{name}{last_name}@{domain}"
                    emails.append(em)
                if c_name + c_last_name + 1 == c_email_username:
                    em = f"{name}.{last_name}@{domain}"
                    emails.append(em)
                    em = f"{name}_{last_name}@{domain}"
                    emails.append(em)
                if c_name + c_last_name + c_birt == c_email_username:
                    em = f"{name}{last_name}{birt}@{domain}"
                    emails.append(em)
                if c_name + c_last_name + c_birt - 2 == c_email_username:
                    em = f"{name}{last_name}{birt[2:4]}@{domain}"
                    emails.append(em)
                if name in username:
                    if c_username == c_email_username:
                        em = f"{username}@{domain}"
                        emails.append(em)
                if len(name[0]) + last_name == c_email_username:
                    letter = name[0]
                    em = f"{letter}{last_name}@{domain}"
                    emails.append(em)
            else:
                pass
    #Si lo expuesto aparece en el apellido    
    elif exposed in last_name:
        #Si lo expuesto es igual al apellido
        if exposed == last_name:
            if c_last_name + c_name == c_email_username:
                em = f"{last_name}{name}@{domain}"
                emails.append(em)
            if c_last_name + c_name + 1 == c_email_username:
                em = f"{last_name}.{name}@{domain}"
                emails.append(em)
                em = f"{last_name}_{name}@{domain}"
            if c_last_name + c_name + birt == c_email_username:
                em = f"{last_name}{name}{birt}@{domain}"
                emails.append(em)
            if c_last_name + c_name + birt -2 == c_email_username:
                em = f"{last_name}{name}{birt[2:4]}@{domain}"
                emails.append(em)
            if last_name in username:
                if c_username == c_email_username:
                    em = f"{username}@{domain}"
                    emails.append(em)
        else:
            d2 = input("Are the exposed letters part of the last name? Y/n: ")
            if d2 == "y" or d2 == "Y" or d2 == "yes" or d2 == "Yes":
                if c_last_name + c_name == c_email_username:
                    em = f"{last_name}{name}@{domain}"
                    emails.append(em)
                if c_last_name + c_name + 1 == c_email_username:
                    em = f"{last_name}.{name}@{domain}"
                    emails.append(em)
                    em = f"{last_name}_{name}@{domain}"
                if c_last_name + c_name + birt == c_email_username:
                    em = f"{last_name}{name}{birt}@{domain}"
                    emails.append(em)
                if c_last_name + c_name + birt -2 == c_email_username:
                    em = f"{last_name}{name}{birt[2:4]}@{domain}"
                    emails.append(em)
                if last_name in username:
                    if c_username == c_email_username:
                        em = f"{username}@{domain}"
                        emails.append(em)

    print (emails)

    #Verificamos si los emails existen
    emails_ver = []
    for email in emails:
        is_valid = validate_email(
            email_address=email,
            check_format=True,
            check_blacklist=True,
            check_dns=True,
            dns_timeout=10,
            check_smtp=True,
            smtp_timeout=10,
            smtp_helo_host=None,
            smtp_from_address=None,
            smtp_skip_tls=False,
            smtp_tls_context=None,
            smtp_debug=False)

        file_result = input("Insert file result name (result.txt): ")
        if is_valid:
            print (f"{email} exist.")
            f = open(file_result, "a")
            data = f"{email},True\n"
            f.write(data)
        else:
            print (f"{email} no exist.")
            f = open(file_result, "a")
            data = f"{email},False\n"
            f.write(data)
        
main()

