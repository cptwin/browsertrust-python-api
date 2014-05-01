#!/usr/bin/env python

from bottle import route, run

a = []

@route('/')
def root():
    return "Welcome to BT API 0.0.1"

@route('/hash', method='GET')
def hashGet():
    output = outputJSONHashes()
    return { "success" : True, "HASHES" : output }

@route('/url/<url>', method='GET')
def hashGet( url="URL" ):
    output = outputJSONHashesForURL(url)
    if(isSHA256Hash(url)):
        return { "success" : True, "HASHES" : output }
    else:
        return { "success" : False, "HASHES" : output }
    
def outputJSONHashes():
    output = []
    for hash in a:
        output.append( { "success" : True, "URL" : hash[0],  "HASH" : hash[1] } )
    return output

def outputJSONHashesForURL(url):
    output = []
    for hash in a:
        if(hash[0] == url):
            output.append( { "success" : True, "URL" : hash[0],  "HASH" : hash[1] } )
    return output
    
@route('/url/<url>/hash/<myhash>', method='PUT')
def hashPut(myhash="HASH", url="URL"):
    try:
        if(isSHA256Hash(myhash) and isSHA256Hash(url)):
            temp = [url, myhash]
            a.append(temp)
            return { "success" : True, "URL" : url,  "HASH" : myhash }
        else:
            return { "success" : False, "URL" : url,  "HASH" : myhash }
    except e:
        return { "success" : False, "URL" : url,  "HASH" : myhash }
        print(e)
    
def isSHA256Hash(name):
    if(len(name) == 64):
        return True
    else:
        return False

def main():
    run(host='localhost', port=8765, debug=True)

if __name__ == '__main__':main()