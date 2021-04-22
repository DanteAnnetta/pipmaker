#A simple tool to create modules and upload it in PyPi!


Before using this module, you must create an account on GitHub and an account on Pypi.

You can do this using this links:
http://github.com

https://pypi.org/account/register/

Doing this, you only need a python script which must have a principal class with the module methods.

For upload your module to pypi.org, you need to create a new python script in the directory of your class script and use the following code:

import pipmaker
import os

module = pipmaker.pipmaker()
description = the_description_of_the_module
module_name = "the_name_of_the_module"
author = "the_author_of_the_module"
author_email_adress = "the_email_adress"
module.compiler( description, module_name , author , author_email_adress ) # Between this step and the next step, you must create a proyect in GitHub with MIT license and copy the URL
module.update("the_github_url_of_the_proyect")#Now you must upload all the files into the GitHub proyect    
module.test(os.getcwd())
module.upload("your_pypi_username" , "the_password")