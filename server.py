#!/usr/bin/python3.6
from my_rest.wsgi import application
import cherrypy

if __name__ == '__main__':
    cherrypy.tree.graft(application, '/my-rest')
    
    cherrypy.server.unsubscribe()
    
    server = cherrypy._cpserver.Server()
    
    server.socket_host = "0.0.0.0"
    server.socket_port = 8000
    server.thread_pool = 30
    
    server.subscribe()
    
    server2 = cherrypy._cpserver.Server()
   
    server2.socket_host = "0.0.0.0"
    server2.socket_port = 8001
    server2.thread_pool = 30
      
    server2.subscribe()
    
    cherrypy.engine.start()
    cherrypy.engine.block()
