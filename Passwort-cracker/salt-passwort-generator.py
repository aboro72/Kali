#!/usr/bin/python3
import hashlib

zz = 0
for entry in """pa$$word
iloveyou
princess
1234567
rockyou
12345678
abc123
nicole
daniel
babygirl
monkey
lovely
jessica
654321
michael
ashley
qwerty
111111
iloveu
000000
michelle
tigger
sunshine
chocolate
password1
soccer
anthony
friends
butterfly
purple
angel
jordan
liverpool
justin
loveme
fuckyou
123123
football
secret
andrea
carlos
jennifer
joshua
bubbles
1234567890
superman
hannah
amanda
loveyou
pretty
basketball
andrew
angels
tweety
flower
playboy
hello
elizabeth
hottie
tinkerbell
charlie
samantha
barbie
chelsea
lovers
teamo
jasmine
brandon
666666
shadow
melissa
eminem
matthew
robert
danielle
forever
family
jonathan
987654321
computer
whatever
dragon
vanessa
cookie
naruto
summer
sweety
spongebob
joseph
junior
softball
taylor
yellow
daniela
lauren
mickey
princesa
alexandra
alexis
jesus
estrella
miguel
william
thomas
beautiful
mylove
angela
poohbear
patrick
iloveme
sakura
adrian
alexander
destiny
christian
121212
sayang
america
dancer
monica
richard
112233
princess1
555555
diamond
carolina
steven
rangers
louise
orange
789456
999999
shorty
11111
nathan
snoopy
passw0rd
password1""".split("\n"):
    zz += 1
    s = "salt" + str(zz)
    print(s + "$" + hashlib.md5((s + entry).encode()).hexdigest())

