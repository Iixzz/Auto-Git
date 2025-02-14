import os
import keyboard as kb
from time import sleep



class tag():
    def __init__(self, version, Ordner, repository):
        self.version = version
        self.script_dir = Ordner
        self.repository_URL = repository

        self.doTag()

    def doTag(self):
        os.system("start cmd")
        sleep(0.5)

        text("cd /d ", self.script_dir)

        text("git init", "")
        text("git remote add origin ", self.repository_URL)

        text("git tag ", self.version)
        text("git push origin ", self.version)
        text("git remote rm origin", "")
        sleep(5)

        os.system("taskkill /F /IM cmd.exe")

def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")


#Ausführung
if __name__ == "__main__":
    git_tag = tag()