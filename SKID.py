Skid = {'Xresolver':'Alright you skid https://xresolver.com/ ',
            'Wireshark':' Some skids trying ddos you go to https://www.wireshark.org/',
            'Kali Linux':'YESSS SIR GOTTA HAVE A KALI VM FOR DEM SKIDS https://www.kali.org/ ',
            'Virtual Box':' gotta have a vm for your kali linyx https://www.virtualbox.org/ ',
            'Discord':' Ig discord is for hacking tips https://discord.com/ ',
            'Tor':'Every skid goes on the darkweb https://www.torproject.org/',
            'Metasploit':' METASPLOIT BOYSSSSSS https://www.metasploit.com/ ',
            'ltt':'#LTT Store.com '
}


print ("Sup skid?")
for key in Skid:
        print (key) 

Question = input('SOOOO WHAT SKID TOOL DO YOU WANT ? \n')

thing = Skid.get(Question)
if thing == None: 
        print ('You SKID pick one of the 10 items ')
else:
        print(' you fucking skid :(  ...\n', Question,'...', thing )