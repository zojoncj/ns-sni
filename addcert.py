#!/usr/bin/env python

import argparse
import sys,os
import ConfigParser

from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

global config

def main(arguments):



  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument("-u", "--url", help="URL of site being added ie. sig.o.e" , required=True)
  parser.add_argument("-k", "--keyfile", help="Full path to key file", required=True  )
  parser.add_argument("-c", "--certfile", help="Full Path to certificate file", required=True )
  parser.add_argument("--config", help="Config file",default="./config" )

  args = parser.parse_args(arguments)
  configfile= args.config
  keyfile = args.keyfile
  cert = args.certfile
  url = args.url
  if(not os.path.isfile(configfile)):
    sys.exit("Config file %s does not exist" % configfile)

  
  config = ConfigParser.ConfigParser()
  config.read(configfile)

  nsip = config.get('default','ns_ip')
  username = config.get('default','ns_username')
  password = config.get('default','ns_password')

  ns_session = nitro_service(nsip,"HTTPS")
  ns_session.set_credential(username,password)

  ns_session.timeout=30

  try:
    ns_session.login()
  except nitro_exception as  e:
    print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
