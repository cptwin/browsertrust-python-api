#!/usr/bin/python3
import logging

from bottle import route, run, response, abort

api_version = "0.0.2" #API version, please iterate every time you push a version
hash_storage = {} #storage array for hashes

@route('/')
def root():
    return "Welcome to BT API " + api_version

@route('/url/<url>', method='GET')
def hash_get(url):
    try:
        output = ""
        hash_list = hash_storage[url]
        for hash in hash_list:
            output.append({"hash":hash})
        response = {"url":url,"hashes":output}
        return json.dumps(response)
    except KeyError:
        errorOutput = "URL Not in Database"
        logging.warning(errorOutput)
        abort(400, errorOutput)

def outputJSONHashesForURL(url):
    output = []
    for hash in a:
        if(hash[0] == url):
            output.append( { "success" : True, "URL" : hash[0],  "HASH" : hash[1] } )
    return output
    
@route('/url/<url>/hash/<myhash>', method='PUT')
def hash_put(myhash, url):
    if(is_sha_256_hash(myhash) and is_sha_256_hash(url)):
        hash_storage[url] = (url, myhash)
        """Either:
        #response.status = 201
        #return json.dumps({url: myhash})
        or:
        #body_output = json.dumps({url: myhash})
        #return bottle.HTTPResponse(status=201, body=body_output)
        """
    else:
        return { "success" : False, "URL" : url,  "HASH" : myhash }
    
def is_sha_256_hash(name):
    if len(name) == 64:
        return True
    else:
        return False

def main():
    run(host='localhost', port=8765, debug=True)

if __name__ == '__main__':
    # Set up some stuff for logging to provide neat output.
    logging.basicConfig(level=logging.INFO, filename='api_server.log', format='%(levelname)s\t%(asctime)s %(message)s')
    main()