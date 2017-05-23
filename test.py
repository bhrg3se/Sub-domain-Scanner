import optparse

parser = optparse.OptionParser()

parser.add_option('-x', '--max-length',
    action="store", dest="maxlen",
    help="Maximum length, default is 4 characters", default="4")
parser.add_option('-n', '--min-length',
    action="store", dest="minlen",
    help="Minimum length, default is 1 character", default="1")
parser.add_option('-c', '--char-set',
    action="store", dest="charset",
    help="Character set used to brute-force, default is a-z,1-9,-", default="abcdefghijklmnopqrstuvwxyz1234567890-")

parser.add_option('-d', '--domain',
    action="store", dest="domain",
    help="Domain name. eg: google.com")

parser.add_option('-f', '--file',
    action="store", dest="filename",
    help="Save output to a file")

options, args = parser.parse_args()

print(options.filename)