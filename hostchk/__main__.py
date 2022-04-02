import argparse
import sys
from .hostchk import get_args, banner, bulk_req, prototype_req 


def main():
  
  """ Entry point to the script. 
  """
  parser = get_args()
  args = parser.parse_args()
  myfile = open(args.infile, "r")
  tempfile = open(args.infile, "r")
  lines = tempfile.readlines()
  outfile = open(args.outfile, "w")

  banner()
  return bulk_req(myfile, lines)
  
if __name__ =='__main__':
  sys.exit(main())
  #myfile.close()
  #outfile.close()
