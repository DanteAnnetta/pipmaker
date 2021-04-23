# A simple tool to create modules and upload it in PyPi


Before using this module, you must create an account on GitHub and an account on Pypi.

You can do this using this links:
http://github.com

https://pypi.org/account/register/

And create a proyect in GitHub with MIT license and copy the URL

Doing this, you only need a python script which must have a principal class with the module methods.

For upload your module to pypi.org, you need to create a new python script in the directory of your class script and use the following code:

import pipmaker
import os

module = pipmaker.pipmaker()# Create a pipmaker object

description = the_description_of_the_module
module_name = "the_name_of_the_module"
author = "the_author_of_the_module"
author_email_adress = "the_email_adress"
github_url = "the_github_proyect_url"
module.compiler( description, module_name , author , author_email_adress , github_url) 

# If you want to test your module before upload it in pypi, use this line
module.test(os.getcwd())


module.upload("your_pypi_username" , "the_password")
