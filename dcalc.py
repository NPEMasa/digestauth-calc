#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import ConfigParser
import hashlib

param   = len(sys.argv) - 1
param_a = param % 2  #
param_b = param / 2
#URL = sys.argv[param]

class digestauth():
    def msg(self):
        help = """
+------------------------+
| Command Usage          |
+------------------------+
-v  : This Program Version
-h  : This help

+A1 Calc Mode+
-a1 : Calculate A1 of Digest Authentication.
      The needed parameter is <username>, <passwd>,
      <config-file-path>.

+A2 Calc Mode+
-a2 : Calculate A2 of Digest Authentication.
      The needed parameter is <URI>, <config-file-path>.

+Single Calc Mode+
-S  : Calculate response of Digest Authentication.
      The needed parameter is <username>, <passwd>,
      <URI>, <config-file-path>.

+Auto Calc Mode+
-A  : Calculate response of Digest Authentication
      with dictionary-file.
      The needed parameter is <dict-file-path>,
      <config-file-path>.

[A1 Calc Mode Usage]
$ python dcalc.py -a1 --user <username> --pass <passwd> -c <config-file-path>

[A2 Calc Mode Usage]
$ python dcalc.py -a2 --uri <URI> -c <config-file-path>

[Single Calc Mode Usage]
$ python dcalc.py -S --user <username> --pass <passwd> --uri <URI> -c <config-file-path>

[Auto Calc Mode Usage]
$ python dcalc.py -A -d <dict-file-path> -c <config-file-path>

"""
        print (help)

    def a1calc(self):
        print ("[*]Starting calc A1...")
        #input --user --pass
        user, passwd, realm, config = "", "", "", ""
        i = 2
        print(sys.argv)

        for j in range(len(sys.argv)):
            if sys.argv[i] == "--user":
                print(sys.argv[i])
                # username load
                user = sys.argv[i+1]
                i=i+2
                if i == len(sys.argv):
                    break
                else:
                    continue
            elif sys.argv[i] == "--pass":
                print(sys.argv[i])
                # password load
                passwd = sys.argv[i+1]
                i=i+2
                if i == len(sys.argv):
                    break
                else:
                    continue
            elif sys.argv[i] == "-c":
                config = ConfigParser.ConfigParser()
                config.read(sys.argv[i+1])

                section1 = 'A1'
                realm = config.get(section1, 'realm')
                i=i+2
                if i == len(sys.argv):
                    break
                else:
                    continue
            else:
                u_a1()

        a1 = user + ":" + realm + ":" + passwd
        a1 = hashlib.md5(a1).hexdigest()
        print("A1 : %s " % a1)

    def a2calc(self):
        print ("[*]Starting calc A2...")
        #input --uri -c
        uri, config, method = "", "", ""
        i = 2
        print(sys.argv)

        for j in  range(len(sys.argv)):
            if sys.argv[i] == "--uri":
                uri = sys.argv[i+1]
                i=i+2
                if i == len(sys.argv):
                    break
                else:
                    continue
            elif sys.argv[i] == "-c":
                config = sys.argv[i+1]
                config = ConfigParser.ConfigParser()
                config.read(sys.argv[i+1])

                section1 = 'A2'
                method = config.get(section1, 'method')
                i=i+2
                if i == len(sys.argv):
                    break
                else:
                    continue
            else:
                self.u_a2()

        a2 = method + ":" + uri
        a2 = hashlib.md5(a2).hexdigest()
        print("A2 : %s" % a2)

    def res(self):
        print ("[*]Starting calc Response...")
        #input --user --pass --uri -c
        user, passwd, uri, config, method, nonce, cnonce, qop, nc = "", "", "", "", "", "", "", "", ""
        res1, res2, realm = "", "", ""
        i = 2

        for j in range(len(sys.argv)):
            if sys.argv[j] == "--user":
                user = sys.argv[j+1]
                j=j+2
                if j == len(sys.argv):
                    break
                else:
                    continue
            elif sys.argv[j] == "--pass":
                passwd = sys.argv[j+1]
                j=j+2
                if j == len(sys.argv):
                    break
                else:
                    continue
            elif sys.argv[j] == "--uri":
                uri = sys.argv[j+1]
                j=j+2
                if j == len(sys.argv):
                    break
                else:
                    continue
            elif sys.argv[j] == "-c":
                config = sys.argv[j+1]
                print("[*] Loading Config File...")
                config = ConfigParser.ConfigParser()
                config.read(sys.argv[j+1])

                section1 = 'True-Response'
                res1 = config.get(section1, 'response')
                user = config.get(section1, 'user')
                realm = config.get(section1, 'realm')
                method = config.get(section1, 'method')
                nonce = config.get(section1, 'nonce')
                cnonce = config.get(section1, 'cnonce')
                uri = config.get(section1, 'uri')
                qop = config.get(section1, 'qop')
                nc = config.get(section1, 'nc')
                j=j+2
                if j == len(sys.argv):
                    break
                else:
                    continue
            else:
                j=j+2
                if j == len(sys.argv):
                    self.u_single()


        a1 = user + ":" + realm + ":" + passwd
        a2 = method + ":" + uri
        a1 = hashlib.md5(a1).hexdigest()
        a2 = hashlib.md5(a2).hexdigest()
        res2 = a1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + a2
        res2 = hashlib.md5(res2).hexdigest()

        print("[*]Calculat successful.")

        print("res1 : %s" % res1)
        print("res2 : %s" % res2)
        print("user : %s" % user)
        print("realm : %s" % realm)
        print("method : %s" % method)
        print("uri : %s" % uri)
        print("nonce : %s" % nonce)
        print("cnonce : %s" % cnonce)
        print("qop : %s" % qop)
        print("nc : %s" % nc)



    def AutoCalcMode(self):
        print ("[*]Starting Auto-Calc-Mode...")
        # usage :  python dcalc.py -A -d dict.txt -c config.txt
        i = 2
        user, passwd, uri, config, method, nonce, cnonce, qop, nc = "", "", "", "", "", "", "", "", ""
        res1, res2, realm = "", "", ""
        list = []

        for k in range(len(sys.argv)):
            if sys.argv[i] == "-d":
                print("[*] Reading Dictionary File...")
                f = open(sys.argv[i+1])
                list = f.read().splitlines()
                f.close()

                i = i + 2
                if i == len(sys.argv):
                    break
                else:
                    continue

            elif sys.argv[i] == "-c":
                print("[*] Loading Config File...")
                config = ConfigParser.ConfigParser()
                config.read(sys.argv[i+1])

                section1 = 'True-Response'
                res1 = config.get(section1, 'response')
                user = config.get(section1, 'user')
                realm = config.get(section1, 'realm')
                method = config.get(section1, 'method')
                nonce = config.get(section1, 'nonce')
                cnonce = config.get(section1, 'cnonce')
                uri = config.get(section1, 'uri')
                qop = config.get(section1, 'qop')
                nc = config.get(section1, 'nc')

                i = i + 2
                #print(i)
                if i == len(sys.argv):
                    break
                else:
                    continue

            else:
                i = i + 2
                if i == len(sys.argv):
                    self.u_auto()


        j = 0
        for j in range(len(list)):

            passwd = list[j]
            #print(passwd)
            a1 = user + ":" + realm + ":" + passwd
            a2 = method + ":" + uri
            a1 = hashlib.md5(a1).hexdigest()
            a2 = hashlib.md5(a2).hexdigest()
            res2 = a1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + a2
            res2 = hashlib.md5(res2).hexdigest()

            if res2 == res1:
                print("[*]Response matched. Answer is { %s }" % res2)
                print("res1 : %s" % res1)
                print("res2 : %s" % res2)
                print("passwd : %s" % passwd)

                break

            else:
                j = j + 1



    def SingleCalcMode(self):
        print ("[*]Starting Single-Calc-Mode...")
        self.res()


    def config(self):
        # config load data sample.

        config = ConfigParser.ConfigParser()
        config.read(sys.argv[2])

        section1 = 'A1'
        print config.get(section1, 'realm')

        section2 = 'A2'
        print config.get(section2, 'method')
        print config.get(section2, 'uri')

        section3 = 'Response'
        print config.get(section3, 'nonce')
        print config.get(section3, 'cnonce')
        print config.get(section3, 'qop')
        print config.get(section3, 'nc')

    def u_a1(self):
        usage = """
        [ERR] Command Validation Error.
              # python dcalc.py -a1 --user <username> --pass <passwd>-c <config-file-path>
        """
        print(usage)

    def u_a2(self):
        usage = """
        [ERR] Command Validation Error.
              # python dcalc.py -a2 --uri <URI> -c <config-file-path>
        """
        print(usage)

    def u_single(self):
        usage = """
        [ERR] Command Validation Error.
              # python dcalc.py -S --user <username> --pass <passwd> --uri <URI> -c <config-file-path>
        """
        print(usage)

    def u_auto(self):
        usage = """
        [ERR] Command Validation Error.
              # python dcalc.py -A -d <dict-file-path> -c <config-file-path>
        """
        print(usage)

def main():
    global d
    d = digestauth()
    if sys.argv[1] == "-a1":
        d.a1calc()

    elif sys.argv[1] == "-a2":
        d.a2calc()

    elif sys.argv[1] == "-res":
        d.res()

    elif sys.argv[1] == "-A":
        d.AutoCalcMode()

    elif sys.argv[1] == "-S":
        d.SingleCalcMode()

    elif sys.argv[1] == "-h":
        d.msg()

    elif sys.argv[1] == "-v":
        print ("Digest Auth Calculator ver: 1.0.0 ")

    elif sys.argv[1] == "-c":
        d.config()


if __name__ == '__main__':
    main()
