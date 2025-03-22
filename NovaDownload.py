
import time
import os
import sys
import requests
import random

end = "\033[0m"
cyan= "\033[0;36m"
purple = "\033[0;35m"

logo2=f'''
                .                                            .
     {cyan}*{end}   .                  .              .   {cyan}     .   *          .
  .         .                    {cyan} .   {end}    .           .      .        .
        o                             .                   .
         .       {end} {purple}      .                  .           .
          0     .
                 .          .                 ,                ,    ,
 .          \          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .{cyan}   ##*#  #\##\##               .                     .
      .      ##*#  #o##\#         .                             ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __

'''
def print_progress_bar(iteration, total, length=50):
    progress = (iteration / total)
    arrow = '=' * int(round(length * progress) - 1) + '>'
    spaces = ' ' * (length - len(arrow))
    sys.stdout.write(f'\r[{arrow + spaces}] {int(progress * 100)}%')
    sys.stdout.flush()

def download_file(url, filename=None):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        if filename is None:
            filename = os.path.basename(url)
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        os.system('clear')
        print(f"{purple}Downloading missing moudles. (iiiapi)")
        print(logo2)
        for i in range(101):
            time.sleep(random.uniform(0.08, 0.01))
            print_progress_bar(i, 100)
        print("\nMoudles installed, rerun script.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file: {e}")
try:
    from iiiapi import fetch
except ImportError:
    url = 'https://github.com/9skifi/iiiapi/releases/download/api/iiiapi.py'
    download_file(url)
    exit()





logo=f'''
                                                                    ..;===+.
                                                                .:=iiiiii=+=
                                                             {purple}.=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                   =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                {cyan}  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;`
'''



current_directory = os.getcwd()


def write(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")
def inject():
    write("Opening directory")


while True:
    os.system('cls')
    print(f'{purple}{logo}')
    print('Nova V1.0.0')
    write(f'{purple}Enter{end}{cyan} youtube{end}{purple} link>')
    link=input(f'>')
    try:
       #public import
        fetch(link,'Nova V1.0.0')
        print(f'{purple}',end='')
        inject()
        os.system(f'explorer.exe {current_directory}')
    except Exception as e:
        with open('errorlog.txt','w') as file:
            file.write(str(e))
        try:
            os.system(f"explorer.exe '{current_directory}\errorlog.txt'")    
        except SyntaxWarning:
            pass




