#!/usr/bin/python3
import logging
import json

from bottle import route, run, response, abort, post, request

api_version = "0.0.3" #API version, please iterate every time you push a version
hash_storage = {} #storage array for hashes

@route('/')
def root():
    return "Welcome to BT API " + api_version

@route('/url/<url>', method='GET')
def hash_get(url):
    """Returns all the hashes for a given url.

    Keyword arguments:
    url -- the url you want the hashes for.
    """
    try:
        output = []
        hash_list = hash_storage[url]
        for hashes in hash_list:
            output.append(hashes)
        response = {"url":url,"hashes":output}
        return json.dumps(response)
    except KeyError:
        errorOutput = "URL Not in Database"
        logging.warning(errorOutput)
        abort(400, errorOutput)
        

@route('/url', method='POST')
def hash_put():
    """Stores a given url and hash.

    Data must be posted in JSON format in the form:
    {url:theurltosubmit,hash:thehashtosubmit}
    """
    posted_data = json.loads(request.body.read().decode("utf-8"))
    posted_url = posted_data['url']
    posted_hash = posted_data['hash']
    if(is_sha_256_hash(posted_hash)):
        if(posted_url in hash_storage):
            hash_list = hash_storage[posted_url]
            hash_list.append(posted_hash)
        else:
            hash_storage[posted_url] = [posted_hash]
    else:
        abort(400, "SHA256 Hash not submitted!")
    
def is_sha_256_hash(name):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
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