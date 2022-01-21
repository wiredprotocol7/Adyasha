# base_file_name = "testALL"


from typing import List

codetop = """         #common in every file # in the top of every file
import requests \n
import restapicalls\n 
def main( ):\n
"""

codebot = """                     #common in every file     #bottom of every file
if __name__ == "__main__":\n
           main() """

testcucumber = """
from requests.auth import HTTPDigestAuth 
from behave import *
import restapicalls
from requests.auth import HTTPBasicAuth
endpoint = None
request = None
headers=None
auth=None
response_code = None
name= None
#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
#baaseurl = 'https://petstore3.swagger.io/api/v3'
baseurl='{baseurl}'
@given( 'I set {method} {endpoint} API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = '{endpoint}'
@when('I send {method} HTTPS request {endpoint}')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= '{method}',url='{baseurl}'+'/{endpoint}',load={parameter},headers={headers},auth={auth})
@then('I receive a valid HTTPS response code 200 from {endpoint} using {method}')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200
"""

addtestcucumber = """
endpoint = None
request = None
headers=None
auth=None
response_code = None
#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
#baseurl = 'https://petstore3.swagger.io/api/v3'
baseurl='{baseurl}'
@given( 'I set {method} {endpoint} API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = '{endpoint}'
@when('I send {method} HTTPS request {endpoint}')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= '{method}',url='{baseurl}'+'/{endpoint}',load={parameter},headers={headers},auth={auth})
@then('I receive a valid HTTPS response code 200 from {endpoint} using {method}')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200
"""


def createfile(typefile, base_file_name):  # create a file

    if typefile == 'py':
        filename = base_file_name + 'auto' + ".py"  # sting to store the name of the file
    if typefile == 'feature':
        filename = base_file_name + 'auto' + ".feature"
    print(filename)  # printing file name
    try:

        file = open(filename, "w")  # if there is no file it will create a new file if file exists then clear it
    except:
        print("unable to create file")

    return file


def create_test_script(headers, auth, base_file_name, method, endpoint, parameter=None,
                       baseurl='https://petstore3.swagger.io/api/v3'):
    # calling the createfile func that returns a file
    method_check = {'get', 'post', 'put', 'delete'}  # validation of methods
    if method.lower() not in method_check:
        print('this is not a correct method')
        return
    print(type(parameter))  # validate dictationary

    try:  # exception handeling
        print("I need to workout and loose weight now!")
        file = createfile(typefile='py', base_file_name=base_file_name)
        print(file.name)
        with open(file.name, 'w') as f:  # open(file.name, w) is for writing things into the file
            f.write(codetop)  # it will append all these into the new file
            f.write("    method ='" + method + "'\n")
            f.write("    endpoint='" + baseurl + endpoint + "'\n")
            f.write("    parameter=" + str(parameter) + "\n")
            f.write("    headers=" + str(headers) + "\n")
            f.write("    auth=" + str(auth) + "\n")
            f.write("    resp=restapicalls.api_call(method,endpoint,parameter,headers=headers,auth=auth)\n")
            f.write("    print(resp)\n")
            f.write(codebot)
    except Exception as error:
        print(error)
        print("file modification error")
        return

    return file  # returning the newly created file


def create_cucumber_script(baseurl, base_file_name, endpoints, methods, parameter_values, parameters, headers, auth):
    try:  # exception handeling
        file = createfile(typefile='py', base_file_name=base_file_name)
        txt = testcucumber.format(baseurl=baseurl, method=methods, endpoint=endpoints, parameter_value=parameter_values,
                                  parameter=parameters, headers=headers, auth=auth)
        # print (testcucumber)
        with open(file.name, 'w') as f:  # open(file.name, w) is for writing things into the file
            f.write(txt)



    except Exception as error:
        print(error)
        print("file modification error")
        return

    return file


def add_cucumber_script(baseurl, base_file_name, endpoints, methods, parameter_values, parameters, headers, auth):
    try:  # exception handeling

        txt = addtestcucumber.format(baseurl=baseurl, method=methods, endpoint=endpoints,
                                     parameter_value=parameter_values, parameter=parameters, headers=headers, auth=auth)
        # print (testcucumber)                 #print
        with open(base_file_name, 'a') as f:  # a is for adding/appending new texts into the file
            f.write(txt)



    except Exception as error:
        print(error)
        print("file modification error")
        return

    return f


def add_feature_script(file, featurename, scenarioname, endpoint, pointingattribute, methods):
    try:  # exception handeling

        with open(file,
                  'a') as f:  # open(file.name, w) is for writing things into the file #it will append all these into the new file
            print(f.name)
            f.write(" " + "\n")  # appending strings into the file

            f.write("Scenario: " + scenarioname + "\n")

            f.write("\t" + "Given I set " + methods + ' ' + endpoint + " API endpoint" + "\n")

            #f.write("\t" + "And I have valid " + pointingattribute + "\n")

            f.write("\t" + "When I send " + methods + " HTTPS request " + endpoint + "\n")

            f.write(
                "\t" + "Then I receive a valid HTTPS response code 200 from " + endpoint + " using " + methods + "\n")

    except Exception as error:
        print(error)
        print("file modification error")
        return

    return file  # returning the newly created file


def create_feature_script(file, featurename, scenarioname, endpoint, pointingattribute, methods):
    try:  # exception handeling

        with open(file.name, 'a') as f:  # open(file.name, w) is for writing things into the file
            # it will append all these into the new file
            f.write("Feature: " + featurename + "\n")  # appending strings into the file

            f.write("Scenario: " + scenarioname + "\n")

            f.write("\t" + "Given I set " + methods + ' ' + endpoint + " API endpoint" + "\n")

            #f.write("\t" + "And I have valid " + pointingattribute + "\n")

            f.write("\t" + "When I send " + methods + " HTTPS request " + endpoint + "\n")

            f.write(
                "\t" + "Then I receive a valid HTTPS response code 200 from " + endpoint + " using " + methods + "\n")

            f.close()
    except Exception as error:
        print(error)
        print("file modification error")
        return

    return file  # returning the newly created file


def create_file(featuresdir='features/', baseurl=None, typescript=None, projectid=None, userstoryid=None, method=None,
                endpoint=None, parameter=None, parameter_values=None, featurename=None, scenarioname=None,
                pointingattribute=None, headers=None, auth=None):
    if typescript == 'testscript':
        base_file_name = "testAPI" + projectid + userstoryid
        create_test_script(headers=headers, auth=auth, baseurl=baseurl, base_file_name=base_file_name, method=method,
                           endpoint=endpoint, parameter=parameter)
    if typescript == 'stepsscript':
        base_file_name = featuresdir + "steps/" + "testcucumber" + projectid + userstoryid
        create_cucumber_script(baseurl=baseurl, base_file_name=base_file_name, endpoints=endpoint, methods=method,
                               parameter_values=parameter_values, parameters=parameter, headers=headers, auth=auth)

    if typescript == 'createfeature':  # conditionals
        base_file_name = featuresdir + "testfeature" + projectid + userstoryid  # base file name
        newfile = createfile(typefile='feature', base_file_name=base_file_name)
        create_feature_script(file=newfile, featurename=featurename, scenarioname=scenarioname, endpoint=endpoint,
                              pointingattribute=pointingattribute, methods=method)
    if typescript == 'addtofeature':  # conditionals
        base_file_name = featuresdir + "testfeature" + projectid + userstoryid + 'auto.feature'  # base file name
        # exsistingfile=open(base_file_name,'a')
        add_feature_script(file=base_file_name, featurename=featurename, scenarioname=scenarioname, endpoint=endpoint,
                           pointingattribute=pointingattribute, methods=method)
    if typescript == 'addtostepsscript':
        base_file_name = featuresdir + "steps/" + "testcucumber" + projectid + userstoryid + 'auto.py'
        add_cucumber_script(baseurl=baseurl, base_file_name=base_file_name, endpoints=endpoint, methods=method,
                            parameter_values=parameter_values, parameters=parameter, headers=headers, auth=auth)


def create_file_new(typescript='testscript', baseurl="", projectid="1111", userstoryid="2222", method=None,
                    endpoint=None, parameter=None, contenttype=None, auth_type=None, parameter_values=None,
                    featurename=None, scenarioname=None, pointingattribute=None, headers=None, auth=None,
                    featuresdir='features/'):
    # def create_file_new(featuresdir='features/',contenttype=None,baseurl=None,typescript=None,projectid= None,userstoryid=None,method=None,endpoint=None,parameter=None,parameter_values=None,featurename=None,scenarioname=None,pointingattribute=None,headers=None,auth=None,auth_type=None):
    consumes = ["json", "xml"]
    if contenttype and type(contenttype) == List:
        for c_type in contenttype:
            content_type = c_type.split("/")
            if content_type[-1] in consumes:
                if headers == None:
                    headers = {}
                    headers.update({'Content-Type': c_type})
    if auth_type == 'headers':
        if headers == None:
            headers = {}  # empty dictionary if no header passed
        headers.update(auth)  # merge auth dictionary to header dictionary
        auth = None  # since authorisation done by headers
    elif auth_type == "HTTPDigestAuth":  # type of authentication
        auth = "HTTPDigestAuth" + auth
    elif auth == "HTTPBasicAuth":
        auth = "HTTPBasicAuth" + auth
    create_file(featuresdir=featuresdir, baseurl=baseurl, typescript=typescript, projectid=projectid,
                userstoryid=userstoryid, method=method, endpoint=endpoint, parameter=parameter,
                parameter_values=parameter_values, featurename=featurename, scenarioname=scenarioname,
                pointingattribute=pointingattribute, headers=headers, auth=auth)


def create_file_final(typescript='testscript', baseurl="", projectid="1111", userstoryid="2222", method=None,
                      endpoint=None, parameter=None, contenttype=None, auth_type=None, parameter_values=None,
                      featurename=None, scenarioname=None, pointingattribute=None, headers=None, auth=None,
                      featuresdir='features/'):
    pointingattribute =  parameter_values
    if typescript == "cucumber":
        create_file_new(typescript='stepsscript', baseurl=baseurl, projectid=projectid, userstoryid=userstoryid,
                        method=method,
                        endpoint=endpoint, parameter=parameter, contenttype=contenttype, auth_type=auth_type,
                        parameter_values=parameter_values,
                        featurename=featurename, scenarioname=scenarioname, pointingattribute=pointingattribute,
                        headers=headers, auth=auth,
                        featuresdir=featuresdir)
        create_file_new(typescript='createfeature', baseurl=baseurl, projectid=projectid, userstoryid=userstoryid,
                        method=method,
                        endpoint=endpoint, parameter=parameter, contenttype=contenttype, auth_type=auth_type,
                        parameter_values=parameter_values,
                        featurename=featurename, scenarioname=scenarioname, pointingattribute=pointingattribute,
                        headers=headers, auth=auth,
                        featuresdir=featuresdir)
    else:
        create_file_new(typescript=typescript, baseurl=baseurl, projectid=projectid, userstoryid=userstoryid,
                        method=method,
                        endpoint=endpoint, parameter=parameter, contenttype=contenttype, auth_type=auth_type,
                        parameter_values=parameter_values,
                        featurename=featurename, scenarioname=scenarioname, pointingattribute=pointingattribute,
                        headers=headers, auth=auth,
                        featuresdir=featuresdir)

##########--------TESTING-------------------################
# parameter2 = {"id": "4214","additionalMetadata":"Date22/11/19","file" : "songfile.mp4"}
# baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
# baseurl= 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baseurl = 'https://petstore3.swagger.io/api/v3'
# baseurl='http://httpbin.org'                    #new base url cuz xml didn't worked on petstore

# baseurl = 'https://www.googleapis.com/youtube/v3'
baseurl2= 'https://httpbin.org'
baseurl3= 'https://api.github.com'
# githubheader={'Authorization': 'token ' + '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' }   #authentication usinf header

endpoint = 'pet/10'
# endpoint = "videos"
endpoint2= "digest-auth/auth/user/pass"
endpoint3 = "users/adya1904/repos"

# create_file(baseurl=baseurl,parameter_values='id',typescript = 'stepsscript',projectid='hello',userstoryid='world', method = 'GET',endpoint = endpoint,parameter = None)
# create_file(typescript='stepsscript',projectid='hii',userstoryid='folks',endpoint = 'findByName', method = 'get', parameter_values = 'adyasha', parameter = 'None')
# create_file(typescript='createfeature',projectid='hey',userstoryid='you',featurename = 'Finding the songs using singer name using GET API', scenarioname ='Get song by singer name' ,endpoint ='findByname' , pointingattribute = ' Singername', method='GET')
# create_file(baseurl=baseurl,typescript = 'testscript',method='get',endpoint=endpoint,projectid='hello',userstoryid='world')
#create_file_new(baseurl=baseurl, typescript='createfeature', projectid='peet', userstoryid='storee',featurename='Finding the pets using pet id using GET API', scenarioname='Get pet by pet id',endpoint=endpoint, pointingattribute='petid', method='GET', parameter_values='petid')
# create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'Finding the order using order id using GET API', scenarioname ='Get order by order id' ,endpoint ='store/order/2' , pointingattribute = 'orderid', method='GET',parameter_values='orderid')
# create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'log users using userid using GET API', scenarioname ='log user using user id' ,endpoint ='user/login' , pointingattribute = 'userid', method='GET',parameter_values='userid',parameter={'username':'addy','password':'paddy'})
# create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='get user by user name using GET API',scenarioname='get user by user name',endpoint = 'user/user1',pointingattribute='username', method = 'GET', parameter_values = 'username')
# create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='placing order for pet',scenarioname='place order',endpoint = 'store/order',pointingattribute='ordername', method = 'POST', parameter_values = 'ordername',parameter={"id": 2,  "petId": 4,"quantity": 2,"shipDate": "2021-12-22T04:03:05.280Z","status": "available","complete": 'false'},baseurl=baseurl)
# create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='add a new pet to the store',scenarioname='adding pet',endpoint='pet',pointingattribute='petnumber',method='POST',parameter_values='petnumber',parameter={"id": 0,"category": {"id": 0,"name": "string"},"name": "doggie","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"})
# create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='place an order of pet to the store',scenarioname='ordering pet',endpoint='store/order',pointingattribute='petorder',method='POST',parameter_values='petorder',parameter={"id": 10,"petId": 198772,"quantity": 7,"shipDate": "2021-12-24T03:36:33.067Z","status": "approved","complete": 'true'})
# create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='update an exsisting pet in the store',scenarioname='update pet',endpoint='pet',pointingattribute='existingpetid',method='PUT',parameter_values='existingpetid',parameter={"id": 10,"name": "doggie","category": {"id": 1,"name": "Dogs"  },"photoUrls": ["string"  ],"tags": [{"id": 0,"name": "string"    }],"status": "available"})
# create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'delete the order using order id using delete method', scenarioname ='delete order by order id' ,endpoint ='store/order/1' , pointingattribute = 'deleteorderid', method='DELETE',parameter_values='deleteorderid')
# create_file(baseurl=baseurl,typescript='createfeature',projectid='peet',userstoryid='storee',featurename = 'pssing xml as parameters', scenarioname ='xml parameters' ,endpoint ='post' , pointingattribute = 'postxml', method='POST',parameter="\"<?xml version='1.0' encoding='utf-8'?><a>adyasha</a>\"",parameter_values='postxml',headers={'Content-Type': 'application/xml'})
# create_file(baseurl=baseurl,typescript='createfeature',projectid='peet',userstoryid='storee',featurename = 'testing youtube API authentication', scenarioname ='API authentication' ,endpoint =endpoint , pointingattribute = 'videoid', method='GET',parameter={'id':'7lCDEYXw3mM',"part":"snippet,contentDetails,statistics,status"},parameter_values='videoid',auth={'key':'AIzaSyAEh6NVVpnQViuYl6qAqUNN8AhzdWnaRFQ'})
# create_file(baseurl=baseurl2,typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'testing httpbin API authentication', scenarioname ='API authentication for httpbin' ,endpoint =endpoint2 , pointingattribute = 'userid', method='GET',parameter=None,parameter_values='userid',auth="HTTPDigestAuth('user', 'pass')")
# create_file(baseurl=baseurl3,typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'testing github API authentication', scenarioname ='API authentication for github' ,endpoint =endpoint3 , pointingattribute = 'githubuserid', method='GET',parameter=None,parameter_values='githubuserid',auth="HTTPBasicAuth('adya1904' ,'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')")
# create_file(baseurl=baseurl3,typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'testing github API authentication', scenarioname ='API authentication for github' ,endpoint =endpoint3 , pointingattribute = 'githubuserid2', method='GET',parameter={'type':'all'},parameter_values='githubuserid2', headers=githubheader)
# create_file_new(baseurl=baseurl2,contenttype='xml',typescript='createfeature',projectid='peet',userstoryid='storee',featurename = 'testing httpbin API authentication', scenarioname ='API authentication for httpbin' ,endpoint =endpoint2 , pointingattribute = 'userid', method='GET',parameter=None,parameter_values='userid',auth="('user', 'pass')",auth_type='HTTPDigestAuth')
# create_file_new(baseurl=baseurl3,contenttype='json',typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'testing github API authentication', scenarioname ='API authentication for github' ,endpoint =endpoint3 , pointingattribute = 'githubuserid2', method='GET',parameter={'type':'all'},parameter_values='githubuserid2', auth=githubheader,auth_type='headers')
# create_file_new(baseurl=baseurl3,contenttype='json',typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'testing github API authentication', scenarioname ='API authentication for github' ,endpoint =endpoint3 , pointingattribute = 'githubuserid', method='GET',parameter=None,parameter_values='githubuserid',auth="HTTPBasicAuth('adya1904' ,'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')")

create_file_final(baseurl=baseurl, typescript='cucumber', projectid='pet', userstoryid='store',
                featurename='Finding the pets using pet id using GET API', scenarioname='Get pet by pet id',
                endpoint=endpoint, method='GET',
                headers={'Content-type': 'application/json'})
create_file_final(baseurl=baseurl,typescript='cucumber',projectid='pet',userstoryid='storeorder',featurename = 'Finding the order using order id using GET API', scenarioname ='Get order by order id' ,endpoint ='store/order/2' , method='GET',headers = {'Content-type': 'application/json'})
# create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'log users using userid using GET API', scenarioname ='log user using user id' ,endpoint ='user/login' , pointingattribute = 'userid', method='GET',parameter_values='userid',parameter={'username':'addy','password':'paddy'},headers = {'Content-type': 'application/json'})
# create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='get user by user name using GET API',scenarioname='get user by user name',endpoint = 'user/user1',pointingattribute='username', method = 'GET', parameter_values = 'username',headers = {'Content-type': 'application/json'})
# create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='placing order for pet',scenarioname='place order',endpoint = 'store/order',pointingattribute='ordername', method = 'POST', parameter_values = 'ordername',parameter={"id": 2,  "petId": 4,"quantity": 2,"shipDate": "2021-12-22T04:03:05.280Z","status": "available","complete": 'false'},baseurl=baseurl)
# create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='add a new pet to the store',scenarioname='adding pet',endpoint='pet',pointingattribute='petnumber',method='POST',parameter_values='petnumber',parameter={"id": 0,"category": {"id": 0,"name": "string"},"name": "doggie","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"})#,headers = {'Content-type': 'application/text'})
# create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='place an order of pet to the store',scenarioname='ordering pet',endpoint='store/order',pointingattribute='petorder',method='POST',parameter_values='petorder',parameter={"id": 10,"petId": 198772,"quantity": 7,"shipDate": "2021-12-24T03:36:33.067Z","status": "approved","complete": 'true'})#,headers = {'Content-type': 'application/json'})
# create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='update an exsisting pet in the store',scenarioname='update pet',endpoint='pet',pointingattribute='existingpetid',method='PUT',parameter_values='existingpetid',parameter={"id": 10,"name": "doggie","category": {"id": 1,"name": "Dogs"  },"photoUrls": ["string"  ],"tags": [{"id": 0,"name": "string"    }],"status": "available"})#,headers = {'Content-type': 'application/json'})
# create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'create a list of users with given input array', scenarioname ='create user order' ,endpoint ='createWithList' , pointingattribute = 'orderlist', method='POST',parameter=[{"id": 10,"username": "theUser","firstName": "John","lastName": "James","email": "john@email.com","password": "12345","phone": "12345","userStatus": 1  }],parameter_values='orderlist')
# create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'delete the order using order id using delete method', scenarioname ='delete order by order id' ,endpoint ='store/order/1' , pointingattribute = 'deleteorderid', method='DELETE',parameter_values='deleteorderid',headers = {'Content-type': 'application/json'})
# create_file(baseurl=baseurl,typescript='stepsscript',projectid='peet',userstoryid='storee',featurename = 'pssing xml as parameters', scenarioname ='xml parameters' ,endpoint ='post' , pointingattribute = 'postxml', method='POST',parameter="\"<?xml version='1.0' encoding='utf-8'?><a>adyasha</a>\"",parameter_values='postxml',headers={'Content-Type': 'application/xml'})
# create_file(baseurl=baseurl,typescript='testscript',projectid='peet',userstoryid='storee',featurename = 'pssing xml as parameters', scenarioname ='xml parameters' ,endpoint ='post' , pointingattribute = 'postxml', method='POST',parameter="\"<?xml version='1.0' encoding='utf-8'?><a>adyasha</a>\"",parameter_values='postxml',headers={'Content-Type': 'application/xml'})
# create_file(baseurl=baseurl,typescript='stepsscript',projectid='peet',userstoryid='storee',featurename = 'testing youtube API authentication', scenarioname ='API authentication' ,endpoint =endpoint , pointingattribute = 'videoid', method='GET',parameter={'id':'7lCDEYXw3mM',"part":"snippet,contentDetails,statistics,status",'key':'AIzaSyAEh6NVVpnQViuYl6qAqUNN8AhzdWnaRFQ'},parameter_values='videoid')
# create_file(baseurl=baseurl2,typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'testing httpbin API authentication', scenarioname ='API authentication for httpbin' ,endpoint =endpoint2 , pointingattribute = 'userid', method='GET',parameter=None,parameter_values='userid',auth="HTTPDigestAuth('user', 'pass')")
# create_file(baseurl=baseurl3,typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'testing github API authentication', scenarioname ='API authentication for github' ,endpoint =endpoint3 , pointingattribute = 'githubuserid', method='GET',parameter={'type':'all'},parameter_values='githubuserid',auth="HTTPBasicAuth('adya1904' ,'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')")
# create_file(baseurl=baseurl3,typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'testing github API authentication', scenarioname ='API authentication for github' ,endpoint =endpoint3 , pointingattribute = 'githubuserid2', method='GET',parameter={'type':'all'},parameter_values='githubuserid2', headers=githubheader)
create_file_final(baseurl=baseurl2,contenttype='xml',typescript='cucumber',projectid='http',userstoryid='authcheck',featurename = 'testing httpbin API authentication', scenarioname ='API authentication for httpbin' ,endpoint =endpoint2 , method='GET',parameter=None,auth="('user', 'pass')",auth_type='HTTPDigestAuth')
# create_file_new(baseurl=baseurl3,contenttype='json',typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'testing github API authentication', scenarioname ='API authentication for github' ,endpoint =endpoint3 , pointingattribute = 'githubuserid2', method='GET',parameter={'type':'all'},parameter_values='githubuserid2',auth_type='headers')
create_file_final(baseurl=baseurl3,contenttype='json',typescript='cucumber',projectid='peet',userstoryid='storee',featurename = 'testing github API authentication', scenarioname ='API authentication for github' ,endpoint =endpoint3 , pointingattribute = 'githubuserid', method='GET',parameter=None,auth="HTTPBasicAuth('adya1904' ,'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')")
