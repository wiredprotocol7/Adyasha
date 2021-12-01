import random

base_file_name = "testAPI"

codetop = """
import requests \n
import restapicalls\n 
def main( ):\n
"""

codebot = """
if __name__ == "__main__":\n
           main() """


def createfile():
    filename = base_file_name + str(random.randint(0,100)) + ".py"
    print(filename)
    filename = open(filename, "a")
    return filename


def create_test_script(method, endpoint, parameter):
    file = createfile()
    with open(file.name, 'w') as f:
        f.write(codetop)
        f.write("    method ='" + method + "'\n")
        f.write("    endpoint=" + endpoint + "\n")
        f.write("    parameter=" + parameter + "\n")
        f.write("    resp=restapicalls.api_call(method,endpoint,parameter)\n")
        f.write("    print(resp)\n")
        f.write(codebot)
    return file


create_test_script("get", "www.google.com", "None")
