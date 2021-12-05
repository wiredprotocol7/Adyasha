from behave import *

import restapicalls
baseurl=None
method=None
parameter=None
endpoint=None

@given('base_url is set')
def set_base_url(context):
    global baseurl
    baseurl='https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
@given('Method type is set')
def set_method(context):
    global method
    method = "get"
@when('API call parameter and endpoint is set')
def set_parameter_endpoint(context):
    global parameter
    parameter=None
    load = {'id': '4231'}
    global endpoint
    endpoint = baseurl + '/song' + "/" + load["id"]

@then('make API call')
def make_api_call(context):
    resp = restapicalls.api_call(method, endpoint, parameter)
    print(resp)




