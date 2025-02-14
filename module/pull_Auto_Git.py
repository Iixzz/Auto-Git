import os
import keyboard as kb
from time import sleep


class pull():
    def __init__(self, Ordner, repository):
        self.script_dir = Ordner
        self.repository_URL = repository

        self.do_pull()
    
    def do_pull(self):
        os.system("start cmd")
        sleep(1)
        
        text("cd /d ", self.script_dir)
        text("git init", "")
        text("git remote add origin ", self.repository_URL)
        text("git pull origin master", "")
        text("git remote rm origin", "")
        sleep(5)

        os.system("taskkill /F /IM cmd.exe")



def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")

def main():
    git_pull = pull()

#Ausführung
if __name__ == "__main__":
    main()
