import os
from termcolor import *
import socket
from platform import *

design = '''
(
 )\ )          )     (      (         )     )
(()/(    )  ( /( (   )\     )\     ( /(  ( /(     )     (
 /(_))( /(  )\()))\ ((_) ((((_)(   )\()) )\()) ( /(  (  )\
(_))  )(_))((_)\((_) _    )\ _ )\ ((_)\ ((_)\  )(_)) )\((_)
/ __|((_)_ | |(_)(_)| |   (_)_\(_)| |(_)| |(_)((_)_ ((_)(_)
\__ \/ _` || ' \ | || |    / _ \  | '_ \| '_ \/ _` |(_-<| |
|___/\__,_||_||_||_||_|   /_/ \_\ |_.__/|_.__/\__,_|/__/|_|

\t \t TECHNCIAL SAHIL ABBASI/ HACKER AND PROGRAMMER
\t\t MY WEBSITE => WWW.BLOGGERBHAI.GQ
\t\t YOUTUBE CHANNEL => www.youtube.com/c/TechnicalSahilAbbasi

\t     ***************** HACKER ARE HERE *****************



'''


print(colored(design,"blue"))

note = ''' \t\t THIS TOOL IS ONLY FOR TERMUX USER \t \n'''


print(colored(note,"red"))


if system() == "Window":
                        sys.exit("We Are Also Working In Hacking Tool. We'll Soon Launch It For Window Also")



try:
    color = colored("Enter The Target Address: ","green")
    print(color)
    input = input()
    a = colored(input,"blue")




    if(a):
           os.system("pkg install nmap")
           subprocess.call(["nmap","-v",input])



except FileNotFoundError:
                         a = "Plese Make Sure You're Connected To The Internet :)"

                         print(colored(a,"red"))

except KeyboardInterrupt:
                         print()