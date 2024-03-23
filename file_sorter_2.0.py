# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:23:01 2024

@author: Mahlogonolo Mathekga
shutil - (Shell Utilities)
shutil - provides a comprehensive set of functions for file and directory operations.

"""



import os, shutil
import schedule, time


def file_sorter():
        path = r"C:\Users\Mahlogonolo Mathekga\Downloads/"
        
        file_names = os.listdir(path)
        print(file_names)           #Printing out all the files in the directory
        
        folders = ["PDF Files", "Excel Files", "Word Files", "Python Notebooks", "CSV Files", "Music and Video Files", "Windows Installer Packages",
                   "MetaQuotes Files", "Images", "HTML Files","Python Files", "PowerPoint Files", "Zip Files", "Executable Files"]
        
        for folder in range(len(folders)):
            if not os.path.exists(path + folders[folder]):
                os.makedirs(path + folders[folder])
            
          
        for file in file_names:
            if ".pdf" in file:
                shutil.move(path + file, path + "PDF Files/" + file)
                
            elif ".xls" in file:
                shutil.move(path + file, path + "Excel Files/" + file)
                
            elif ".doc" in file:
                shutil.move(path + file, path + "Word Files/" + file)
                    
            elif ".pptx" in file:
                shutil.move(path + file, path + "PowerPoint Files/" + file)
            
            elif ".py" in file:
                shutil.move(path + file, path + "Python Files/" + file)
                
            elif ".ipynb" in file:
                shutil.move(path + file, path + "Python Notebooks/" + file)
            
            elif ".csv" in file:
                shutil.move(path + file, path + "CSV Files/" + file)
                
            elif ".html" in file:
                shutil.move(path + file, path + "HTML Files/" + file)
                
            elif ".mq5" in file:
                shutil.move(path + file, path + "MetaQuotes Files/" + file)
                
            elif ".png" in file:
                shutil.move(path + file, path + "Images/" + file)
            
            elif ".zip" in file:
                shutil.move(path + file, path + "Zip Files/" + file)
            
            elif ".exe" in file:
                shutil.move(path + file, path + "Executable Files/" + file)
            
            elif ".mp4" in file:
                shutil.move(path + file, path + "Music and Video Files/" + file)
                
            elif ".msi" in file:
                shutil.move(path + file, path + "Windows Installer Packages/" + file)
            
            else:
                break


schedule.every(15).days.do(file_sorter)

while True:
    schedule.run_pending()
    time.sleep(1)
    