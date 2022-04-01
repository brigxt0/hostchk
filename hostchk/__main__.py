import argparse 
from .hostchk import get_args, banner, bulk_req, prototype_req 


if __name__ == "__main__":
  
  """ Entry point to the script. 
  """
  parser = get_args()
  args = parser.parse_args()
  myfile = open(args.infile, "r")
  tempfile = open(args.infile, "r")
  lines = tempfile.readlines()
  outfile = open(args.outpfile, "w")

  banner()
  results = bulk_req(myfile, lines)
  #myfile.close()
  #outfile.close()
