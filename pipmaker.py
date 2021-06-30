# -*- coding: utf-8 -*-
#the class script name must be the same as the module name
import os

class pipmaker:
    def __init__(self):
        try:
            import setuptools
        except:
            try:
                os.system("pip3 install setuptools")
            except:
                os.system("pip install setuptools")
        
        try:
            import wheel
        except:
            try:
                os.system("pip3 install wheel")
            except:
                os.system("pip install wheel")    
        
        try:
            import twine
        except:
            try:
                os.system("pip3 install twine")
            except:
                os.system("pip install twine")
        
        try:
            import tqdm
        except:
            try:
                os.system("pip3 install tqdm")
            except:
                os.system("pip install tqdm")
        

    def compiler(self, description , module , author , email , github_url):
        self.module = module
        file = open("README.md" , "w")
        file.write("# " + description)
        file.close()
        
        file = open("setup.py" , "w")
        file.writelines('import setuptools'+ os.linesep)
        file.writelines('with open("README.md", "r") as fh:'+ os.linesep)
        file.writelines('    long_description = fh.read()'+ os.linesep)
        file.writelines('setuptools.setup('+ os.linesep)
        file.writelines('     name= "' + module + '",' + os.linesep)
        file.writelines('     version="0.1",'+ os.linesep)
        file.writelines('     scripts=["' + module + '.py"],'+ os.linesep)
        file.writelines('     author="' + author +'",'+ os.linesep)
        file.writelines('     author_email="' + email + '",'+ os.linesep)
        file.writelines('     description="' + description + '",'+ os.linesep)
        file.writelines('     long_description=long_description,'+ os.linesep)
        file.writelines('     long_description_content_type="text/markdown",'+ os.linesep)
        file.writelines('     url="' + github_url + '",'+ os.linesep) #the github repository url
        file.writelines('     packages=setuptools.find_packages(),'+ os.linesep)
        file.writelines('     classifiers=['+ os.linesep)
        file.writelines('         "Programming Language :: Python :: 3",'+ os.linesep)
        file.writelines('         "License :: OSI Approved :: MIT License",'+ os.linesep)
        file.writelines('         "Operating System :: OS Independent",'+ os.linesep)
        file.writelines('     ],'+ os.linesep)
        file.writelines(')')
        file.close()

        os.system("python setup.py bdist_wheel")

    def test(self, path):
        os.system("python setup.py install")


    #Before you run this function, you must create a repository in github and copy 
    #the link as the input of this function
    
    
        
    def upload(self , username , password):
        os.popen("python -m twine  upload dist/*  -u " + username + " -p" + password)
    
        



        
        
