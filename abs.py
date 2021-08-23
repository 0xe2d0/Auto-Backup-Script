try:
    from colorama import Fore,Back
except:
    print('Please download  requirements file , command : pip3 install -r requirements.txt')
    exit()
import time
import os
from distutils.dir_util import copy_tree
import shutil
import pathlib
import argparse

try:
    args = argparse.ArgumentParser(description="ABS Project minimal backup service")
    args.add_argument('-p','--path',required=False,default=".",help="Name of the folder to be backed up")
    args.add_argument('-o','--output',required=False,default=f'../backup',help="Path of output directory")
    args.add_argument('-l','--log-file',required=False,default="backup.log",help="Name of log files")
    args.add_argument('-t','--time',required=False,default=30,type=int,help="Backup time interval")
    arguments = args.parse_args()

    def folder_check(val):
        val = str(val)
        if not val.endswith('/'):
            return val+'/'

    def get_file_size(file_path):
        size = os.path.getsize(file_path)
        return str(round(size / 1024, 3)) +" kb"

    def file_or_folder(mainPath):
        files = []
        folders = []
        for path in pathlib.Path(mainPath).iterdir():
            if path.is_file():
                if str(path).startswith("."):continue
                files.append(path)
            else:
                if str(path).startswith("."):continue
                folders.append(path)

        return {"files":files,"folders":folders}

    def write_log(contents):
        context = "+"+"-"*50+"+"
        title1,title2 = "Files And Folders","Size"
        context += f"\n|{title1}"+" "*(35-len(title1))+"|"+title2+" "*(14-len(title2))+"|"
        context += "\n+"+"-"*50+"+"
        for text in contents:
            context += f"\n|{text[0]}"+" "*(35-len(text[0]))+"|"+text[1]+" "*(14-len(text[1]))+"|"

        context += "\n+"+"-"*50+"+"
        with open(arguments.log_file,'a') as f:
            f.write('All files copied !!!')
            f.write(context+"\n\n")
            f.close()

    def log(contents):
        context = "+"+"-"*50+"+"
        title1,title2 = "Files And Folders","Size"
        context += f"\n|{Fore.RED+title1+Fore.RESET}"+" "*(35-len(title1))+"|"+Fore.RED+title2+Fore.RESET+" "*(14-len(title2))+"|"
        context += "\n+"+"-"*50+"+"
        for text in contents:
            context += f"\n|{Fore.GREEN+text[0]+Fore.RESET}"+" "*(35-len(text[0]))+"|"+Fore.YELLOW+text[1]+Fore.RESET+" "*(14-len(text[1]))+"|"
    
        context += "\n+"+"-"*50+"+"
        return context


    def backup():
        files = file_or_folder(arguments.path)['files']
        logInfos = []
        folders = file_or_folder(arguments.path)['folders']
        for folder in folders:
            shutil.copytree(folder,folder_check(arguments.output)+str(folder),copy_function=shutil.copy2)
        for file in files:
            shutil.copy(file,folder_check(arguments.output))
        for i in files:
            kb = get_file_size(i)
            logInfos.append((str(i),kb))

        for i in folders:
            kb = get_file_size(i)
            folder = str(i)+" /"
            logInfos.append((folder,kb))
        
        print(Fore.BLUE+'\nAll files copied !!!'+Fore.RESET)
        print(log(logInfos))
        write_log(logInfos)

    while 1:
        try:shutil.rmtree(arguments.output)
        except:pass
        backup()
        time.sleep(arguments.time)
except KeyboardInterrupt :
    print("\nBackup Service Closing")
    exit()
