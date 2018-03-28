#!/usr/bin/env python

import argparse
import sys,os
import ConfigParser

# Used to connect to the device
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

# Used to upload the cert & key
from nssrc.com.citrix.netscaler.nitro.resource.config.system.systemfile import systemfile

def checkfile(filename):
  if(not os.path.isfile(filename)):
    sys.exit("File %s does not exist" % filename)
  return filename

def uploadfile(filename):
  print("Uploading file: %s" %filename)

def logout():
  print("Logging out")
  session.logout()

def connect(ip,user,passwd):
  ns_session = nitro_service(ip,"HTTPS")
  ns_session.set_credential(user,passwd)

  ns_session.timeout=30

  try:
    ns_session.login()
  except nitro_exception as  e:
    print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)

  print("Connected to: %s as %s" %(ip,user))
  return ns_session

def main(arguments):
  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument("-u", "--url", help="URL of site being added ie. sig.o.e" , required=True)
  parser.add_argument("-k", "--keyfile", help="Full path to key file", required=True  )
  parser.add_argument("-c", "--certfile", help="Full Path to certificate file", required=True )
  parser.add_argument("--config", help="Config file",default="./config" )
  args = parser.parse_args(arguments)

  configfile= checkfile(args.config)
  keyfile = checkfile(args.keyfile)
  cert = checkfile(args.certfile)
  url = args.url

  config = ConfigParser.ConfigParser()
  config.read(configfile)

  nsip = config.get('default','ns_ip')
  username = config.get('default','ns_username')
  password = config.get('default','ns_password')
  global session
  session = connect(nsip,username,password)




  logout()



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
