import subdomainScan
import threading
import thread
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

parser.add_option('-t', '--threads',
    action="store", dest="numThread",
    help="Number of threads")



options, args = parser.parse_args()

domain=options.domain
charset=bytearray(options.charset)
maxlen=options.maxlen
minlen=options.minlen
filename=options.filename
numThread=options.numThread

temp1=bytearray("aaaa")

temp2=bytearray("haaa")
temp3=bytearray("maaa")
temp4=bytearray("taaa")
charset=bytearray("abcdefghijklmnopqrstuvwxyz1234567890-")
#domain="fb.com"
#subdomainScan.scan(charset,5,domain,temp1)
#thread.st(subdomainScan.scan(charset,5,domain,temp1))
print("dfghj")
threading.Thread(target=subdomainScan.scan,args=(charset,5,domain,temp1,temp2)).start()
threading.Thread(target=subdomainScan.scan,args=(charset,5,domain,temp2,temp3)).start()
threading.Thread(target=subdomainScan.scan,args=(charset,5,domain,temp3,temp4)).start()
threading.Thread(target=subdomainScan.scan,args=(charset,5,domain,temp4,"----")).start()
'''
thread.start_new_thread(subdomainScan.scan(charset,5,domain,temp3))
#thread.start_new_thread(subdomainScan.scan(charset,5,domain,temp4))


t1=thread.thread(target=subdomainScan.scan,args=(charset,5,domain,temp1))
t2=Thread(target=subdomainScan.scan,args=(charset,5,domain,temp2))
t3=Thread(target=subdomainScan.scan,args=(charset,5,domain,temp3))
t4=Thread(target=subdomainScan.scan,args=(charset,5,domain,temp4))
'''




