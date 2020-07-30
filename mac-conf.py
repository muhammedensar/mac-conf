#! /usr/bin/python#!/usr/local/bin/python
# coding: utf-8

import optparse
import subprocess
import re


def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="Ağ Arayüzünü Seçin!")
    parse_object.add_option("-m","--mac",dest="mac",help="Atamak istediğiniz MAC adresini giriniz.")
    return parse_object.parse_args()

def mac_conf(interface,mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])


print("""
     _________________________________________________________E
    |        __  __    _    ____    ____             __       |
    |       |  \/  |  / \  / ___|  / ___|___  _ __  / _|      |
    |       | |\/| | / _ \| |     | |   / _ \| '_ \| |_       |
    |       | |  | |/ ___ \ |___  | |__| (_) | | | |  _|      |
    |       |_|  |_/_/   \_\____|  \____\___/|_| |_|_|        |
    |                       MAC-Conf v1.0                     |
    |                       Author : Ns4r                     |
    |         Contact: https://twitter.com/muhamm3ds          |
    |_________________________________________________________|
""")

(user_input,argument) = user_input()
mac_conf(user_input.interface,user_input.mac)
print("[+] Interface : " + user_input.interface)
print("[+] Atanan MAC Adresi : " + user_input.mac)
print("[+] İşlem Tamamlandı..")