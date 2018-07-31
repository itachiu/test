import os

file_name = open('names.txt','r')


def readfile(file):
	application_names= []
	for i in file.readlines():
		application_names.append(i)
	return application_names
def installing(application_names):
	for i in application_names:
		i = i.replace("\n","")
		install_syntax = 'apt-get install '
		install_syntax +=str(i)
		install_syntax +=' -y'
		print("\n[+] Installing "+str(i)+" package........\n")
		os.system(install_syntax)
		print("\n[+] Package is installed..........\n")

        return 


installing(readfile(file_name))

