 #!/usr/bin/python3

from  urllib.request import urlopen
import datetime 
from time import gmtime, strftime
from random import randrange as ran
import subprocess as sp
import os 

os.chdir("/home/jakesyl/Quotes/pyQOTD/src/")
class main:
    def main_func(self):
        os.chdir("/home/jakesyl/Quotes/pyQOTD/src/")
        response = urlopen('http://www.iheartquotes.com/api/v1/random')
        html = response.read()
        filename = str(strftime("%Y-%m-%d", gmtime()))
        filename += str(ran(90))
        filename += '.md'
        with open(filename, mode = 'a', encoding = 'utf-8') as a_file:
            a_file.write(str(html))
        gitpush = sp.check_output('git add -A && git pull && git commit -m "daily file" && git push -f', stderr=sp.STDOUT, shell=True)
        print(gitpush)
        commands = ["mv " + filename +  ' ~/Quotes/QOTD/_posts/', 'cd ~/Quotes/QOTD/ && git add -A',  'cd ~/Quotes/QOTD/ && git commit -m "added new posts"',  'cd ~/Quotes/QOTD/ && git pull', 'cd ~/Quotes/QOTD/ &&  git push', 'cd ~/Quotes/pyQOTD/ && rm -rf ' + filename +  ' && git add -A && git pull && git commit -m "added daily file" && echo hi && git push && echo done']
        for command in commands:
         gitpush = sp.check_output(command , stderr=sp.STDOUT, shell=True)
         print(gitpush)
mc = main() 
print(main.main_func(mc))
