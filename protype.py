from time import sleep
import random
from subprocess import call
import os
from collections import Counter
import keyboard

#Tabs
Running=True
Home_Page = True
Menu_Page = False
Counter_Page = False
Reverse_Page = False
Skip_Page = False
Slicing_Page = False
Case_Page = False

#Controls
key_left='left'
key_right='right'
key_up='w'
key_down='s'

#Tab Control
Menu_Page_Number = 1
Counter_Page_Number = 1 

#setup
Text =  ' '
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def remove(string):
    return string.replace(" ", "")

isint=True

#Colors
class colors:
    Black= '\u001b[30m'
    Red= '\u001b[31m'
    Green= '\u001b[32m'
    Yellow= '\u001b[33m'
    Blue= '\u001b[34m'
    Magenta= '\u001b[35m'
    Cyan= '\u001b[36m'
    White= '\u001b[37m'
    Purple = "\033[95m"
    Reset= '\u001b[0m'
    Underline= '\u001b[4m'
    Bold = '\u001b[1m'


def Home():
    clear()
    global Home_Page,Menu_Page
    print(f'''┌───────────────────────────────────────────────────────┐
                      {colors.Bold}{colors.Underline}Information{colors.Reset}
    The objective of this is so you can see for your
    self all of the examples shown above press {colors.Bold}LEFT{colors.Reset}
    and {colors.Bold}RIGHT{colors.Reset} arrows{colors.Reset} to go to the next pages on the
    next page, and {colors.Bold}ENTER{colors.Reset} once ready to begin,
    also once this begins you can always press {colors.Bold}' ! '{colors.Reset} 
    to go to the Menu 
└───────────────────────────────────────────────────────┘
    ''')
    input('')
    clear()
    Home_Page = False
    Menu_Page = True

def Menu():
    global Menu_Page_Number,Page_Menu,Counter_Page,Menu_Page,Reverse_Page,Skip_Page,Slicing_Page ,Case_Page
    
    #Pages
    Page_Menu=[(f'''┌───────────────────────────────────────────────────────┐
                        {colors.Bold}{colors.Underline}Main Menu{colors.Reset}
    
        『{colors.Red}1.Slicing{colors.Reset}』 『{colors.Yellow}2.Reverse{colors.Reset}』  『{colors.Green}3.Skip{colors.Reset}』 
    
                        {colors.Bold}Page {Menu_Page_Number}/2{colors.Reset}
└───────────────────────────────────────────────────────┘'''),(f'''┌───────────────────────────────────────────────────────┐
                        {colors.Bold}{colors.Underline}Main Menu{colors.Reset}
    
    『{colors.Blue}4.Upper/Lower Case{colors.Reset}』 『{colors.Purple}5.Counter{colors.Reset}』
    
                        {colors.Bold}Page {Menu_Page_Number}/2{colors.Reset}
└───────────────────────────────────────────────────────┘''')]
    
    if Menu_Page_Number == 1:
        clear()
        print(Page_Menu[0])
    elif Menu_Page_Number == 2:
        clear()
        print(Page_Menu[1])
    else:
        Menu_Page_Number = 1
    
    while True:
        if keyboard.read_key()==key_right:
            Menu_Page_Number+=1
            break
        if keyboard.read_key()==key_left:
            Menu_Page_Number-=1
            break
        if keyboard.read_key()=='5':
            clear()
            Menu_Page= False
            Counter_Page = True
            break
        
        if keyboard.read_key()=='2':
            clear()
            Menu_Page= False
            Reverse_Page = True
            break
        if keyboard.read_key()=='3':
            clear()
            Menu_Page= False
            Skip_Page = True
            break
        if keyboard.read_key()=='1':
            clear()
            Menu_Page= False
            Slicing_Page = True
            break
        if keyboard.read_key()=='4':
            clear()
            Menu_Page= False
            Case_Page = True
            break
        


def Counters():
    global Text,Counter_Page,Menu_Page

    clear()
    Text=input(f'''┌───────────────────────────────────────────────────────┐
                        {colors.Bold}{colors.Underline}Counter{colors.Reset}

{colors.Bold}Text:{colors.Reset} ''')
    char=len(remove(Text))
    print(f'''
{colors.Bold}──────────────────────────────────────────────
{colors.Bold}Characters:{colors.Reset} {char}''')
    if Text == "":
        print("\nAdd at least one word")
    else:
        word=Text.split(" ")
        word=len(word)
        print(f'''
{colors.Bold}Words:{colors.Reset} {word}
                               Press {colors.Bold}' ➡  '{colors.Reset} to Restart
└───────────────────────────────────────────────────────┘''')
    while True:
        if keyboard.read_key()=='!':
            Counter_Page = False
            Menu_Page = True
            break
        elif keyboard.read_key()==key_right:
            break



def Reverse():
    global Reverse_Page,Menu_Page
    clear()
    Text=input(f'''┌───────────────────────────────────────────────────────┐
                        {colors.Bold}{colors.Underline}Reverse{colors.Reset}
                        
    {colors.Bold}Text:{colors.Reset} ''')
    
    print(f'''
    {colors.Bold}Reversed:{colors.Reset} {Text[::-1]}
                               Press {colors.Bold}' ➡  '{colors.Reset} to Restart
└───────────────────────────────────────────────────────┘''')
    while True:
        if keyboard.read_key()=='!':
            Reverse_Page = False
            Menu_Page = True
            break
        elif keyboard.read_key()==key_right:
            break


def Skip():
    global Menu_Page,Skip_Page,isint
    clear()
    Text=input(f'''┌───────────────────────────────────────────────────────┐
                        {colors.Bold}{colors.Underline}Skip{colors.Reset}
    
    {colors.Bold}Text:{colors.Reset} ''')
    
    while (isint):
        Skip_OP=input(f'''
    {colors.Bold}Skip (Letters Skipping):{colors.Reset} ''')
        try:
            Skip_OP = int(Skip_OP)
            isint=False
        except ValueError:
            print("Type in a number.")
    
    
    
    print(f'''
    {colors.Bold}──────────────────────────────────────────────
    [{Skip_OP}] Letter Skipping:{colors.Reset} {Text[::Skip_OP]}''')
    
    print(f'''                               Press {colors.Bold}' ➡  '{colors.Reset} to Restart
└───────────────────────────────────────────────────────┘''')
    while True:
        if keyboard.read_key()=='!':
            Skip_Page = False
            Menu_Page = True
            break
        elif keyboard.read_key()==key_right:
            break


def Slice():
    global Menu_Page,Slicing_Page,isint
    clear()
    Text=input(f'''┌───────────────────────────────────────────────────────┐
                    {colors.Bold}{colors.Underline}Slicing{colors.Reset}
    
    {colors.Bold}Text:{colors.Reset} ''')
    
    while (isint):
        Slice_First=input(f'''
    {colors.Bold}Letters Sliced (Beginning):{colors.Reset} ''')
        try:
            Slice_First = int(Slice_First)
            isint=False
        except ValueError:
            print("Type in a number.")
    
    isint=True
    
    while (isint):
        Slice_Last=input(f'''
    {colors.Bold}Letters Sliced (End):{colors.Reset} ''')
        try:
            Slice_Last = int(Slice_Last)
            isint=False
        except ValueError:
            print("Type in a number.")
    isint=True
    
    
    #Agjusting First
    if Slice_First > len(Text) - 1:
        Slice_First = len(Text) - 1

    if Slice_First < 0:
        Slice_First = 0
    

    #Ajusting Last
    Slice_Last=  len(Text) - Slice_Last
    if Slice_Last > len(Text):
        Slice_Last=  len(Text) - Slice_Last
    Next=f'\n{colors.Bold}{colors.Red}Umm, I don\'t think you did something right.....{colors.Reset}'
    
    if Text[Slice_First:Slice_Last] == '':
        print(Next)
    else:
        print(f'''
    {colors.Bold}──────────────────────────────────────────────
    Sliced:{colors.Reset} {Text[Slice_First:Slice_Last]}''')
    
    print(f'''                               Press {colors.Bold}' ➡  '{colors.Reset} to Restart
└───────────────────────────────────────────────────────┘''')
    while True:
        if keyboard.read_key()=='!':
            Slicing_Page = False
            Menu_Page = True
            break
        elif keyboard.read_key()==key_right:
            break
    
    

def Case():
    global Menu_Page, Case_Page
    clear()
    Text=input(f'''┌───────────────────────────────────────────────────────┐
                    {colors.Bold}{colors.Underline}Upper/Lower case{colors.Reset}
    
    {colors.Bold}Text:{colors.Reset} ''')
    
    print(f'\n{colors.Bold}    ──────────────────────────────────────────────\n    Upper case:{colors.Reset} {Text.upper()}\n{colors.Bold}    Lower case:{colors.Reset} {Text.lower()}')
    print(f'''                               
                              Press {colors.Bold}' ➡  '{colors.Reset} to Restart
└───────────────────────────────────────────────────────┘''')
    while True:
        if keyboard.read_key()=='!':
            Case_Page = False
            Menu_Page = True
            break
        elif keyboard.read_key()==key_right:
            break
while(Running):
    if Home_Page == True:
        Home()
    if  Menu_Page == True:
        print(' ')
        Menu()
    if Counter_Page == True:
        Counters()
    if Reverse_Page == True:
        Reverse()
    if Skip_Page == True:
        Skip()
    if Slicing_Page == True:
        Slice()
    if Case_Page == True:
        Case()