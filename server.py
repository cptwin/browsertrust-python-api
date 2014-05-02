#!/usr/bin/python3

from bottle import route, run, response, HTTPResponse

hash_storage = {} #storage array for hashes

@route('/')
def root():
    return "Welcome to BT API 0.0.1"

@route('/url/<url>', method='GET')
def hash_get(url):
    output = outputJSONHashesForURL(url)
    if(isSHA256Hash(url)):
        return { "success" : True, "HASHES" : output }
    else:
        return { "success" : False, "HASHES" : output }

def outputJSONHashesForURL(url):
    output = []
    for hash in a:
        if(hash[0] == url):
            output.append( { "success" : True, "URL" : hash[0],  "HASH" : hash[1] } )
    return output
    
@route('/url/<url>/hash/<myhash>', method='PUT')
def hashPut(myhash, url):
    if(is_SHA_256_hash(myhash) and is_SHA_256_hash(url)):
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
    
def is_SHA_256_hash(name):
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