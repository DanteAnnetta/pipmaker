import pipmaker2
import os

module = pipmaker.pipmaker()# Create a pipmaker object

description = "the_description_of_the_module"
module_name = "the_name_of_the_module"
author = "the_author_of_the_module"
author_email_adress = "the_email_adress"
github_url = "the_github_proyect_url"
module.compiler( description, module_name , author , author_email_adress , github_url) 

#If you want to test your module before upload it in pypi, use this line
module.test(os.getcwd())


module.upload("your_pypi_username" , "the_password")


