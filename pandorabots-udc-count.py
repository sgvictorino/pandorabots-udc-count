import csv
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="read Pandorabots logs from FILE", metavar="FILE")

args = parser.parse_args()
log_filename = args.filename
if log_filename is None:
    parser.print_help()
    import sys
    sys.exit(1)

with open(log_filename) as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    count_default_case_replies = 0
    for row in rd:
        try:
            if (row[7] == "*" or row[7] == "AIML MATCH FAIL *"):
                count_default_case_replies += 1
        except:
            pass

print("There are %s UDC fallbacks in the given logs." %
      count_default_case_replies)
