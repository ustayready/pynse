#!/usr/bin/python

# Required fields
NAME = "Test Plugin"

# Required Process method
def Process(host,port):
    global NAME

    response = '{} is processing on {} : {}'.format(NAME, host, port)
    return response
