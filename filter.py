#!/usr/bin/env python

from optparse import OptionParser
import os.path
import re

class warna():  #definisi warna string
   cetak = '\033[0m'
   ijo ='\033[1;32m'
   putih = '\033[1;37m'
   biru = '\033[1;34m'
   kuning = '\033[1;33m'
   abang = '\033[1;31m'

def author(): #tanda %s (persen s) untuk definisikan string
   print('''%s
______  ___      ___________________________________
___   |/  /_____ ___(_)__  /___  ____/__(_)__  /_  /_____________
__  /|_/ /_  __ `/_  /__  / __  /_   __  /__  /_  __/  _ \_  ___/
_  /  / / / /_/ /_  / _  /___  __/   _  / _  / / /_ /  __/  /
/_/  /_/  \__,_/ /_/  /_____/_/      /_/  /_/  \__/ \___//_/
                                                      v.01
%s
[+] Recode
[+] Jangan Lupa Bismillah
[+] Author      : Rehan P
[+] Tool        : MailFilter v
[+] Description : Filter mailist Gmail, Yahoo, Hotmail
[+] Usage       : python filter.py nameMailist -o %s''' % (warna.ijo,warna.putih, warna.cetak))#memanggil warna string

# variabel regex untuk mencari,membaca, mensortir data gmail yahoo hotmail
regex = re.compile(r'''(
                  ([a-zA-Z0-9._%+-]+)
                   @
                   (gmail|yahoo|hotmail)
                   (\.com)
                   )''', re.VERBOSE)

def file_to_str(filename): #membuka file mailist
   with open(filename) as f:
       return f.read().lower()

def get_emails(s): #mensortir data email pada file mailist
   return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

def main(): #penggunaan argument dengan optparse
   parser = OptionParser()
   parser.add_option('-o','--output',dest='output',help='output file to saveFile.txt', action='store_true')
   (options, args) = parser.parse_args()
   try:
       if args and options.output: #jika args true dan options.output true maka melanjutkan program
           for arg in args: #melooping variabel arg dalam args (argument)
               if os.path.isfile(arg): #mengecek bila arg adalah file maka lanjutkan program
                   for email in get_emails(file_to_str(arg)): #mengulang variabel email dalam mailist
                       if 'gmail' in email: #jika ada gmail dalam email maka
                           f =open('gmailFile.txt', 'a') #variabel f membuat file gmailFile.txt
                           f.write(email+'\n') #f menambahkan data email lalu membuat garis baru
                           f.close() 
                       elif 'yahoo' in email: #jika ada yahoo dalam email maka
                           f = open('yahooFile.txt', 'a') #variabel f membuat file yahooFile.txt
                           f.write(email + '\n') #f menambahkan data email lalu membuat baris baru
                           f.close()
                       else: #selain gmail dan yahoo cetak hotmail
                           f = open('hotmailFile.txt', 'a')
                           f.write(email + '\n')
                           f.close()
                   author() #memanggil fungsi author
                   print(warna.cetak) #mencetak warna
                   print('%s[+] Succes filter to gmailFile.txt   [+]%s' % (warna.biru, warna.cetak)) #mencetak notif succes filter
                   print('%s[+] Succes filter to yahooFile.txt   [+]%s' % (warna.kuning, warna.cetak))
                   print('%s[+] Succes filter to hotmailFile.txt [+]%s' % (warna.abang, warna.cetak))
               else:
                   print('"{}" is not a file.').format(arg) #selain file di anggap dict

       else: #selain menjalakan python mailfilter.py maka panggil fungsi author
           author()
           print(warna.cetak)
   except Exception as e:
       print('Error Description', e) #mencetak error


if __name__=='__main__': #memanggil fungsi main()
   main()
