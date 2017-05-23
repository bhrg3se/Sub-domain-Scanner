import subdomainScan
import threading
import thread


'''

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
maxlen=int(options.maxlen)
minlen=int(options.minlen)
filename=options.filename
numThread=int(options.numThread)


'''
domain="facebook.com"
charset=bytearray("abcdefghijklmnopqrstuvwxyz1234567890-")
maxlen=5
minlen=1
filename="out.txt"
numThread=5

tempList=list()

for i in xrange(numThread):
    temp=bytearray()
    if(i==0):
        for j in xrange(minlen):
            temp.append(charset[0])
    else:
        temp.append(charset[i*len(charset)/numThread])
        for j in xrange(maxlen-1):
            temp.append(charset[0])
    
    tempList.append(temp)
    print(temp)


temp=bytearray()    
for i in xrange(maxlen):
    temp.append(charset[-1])
print(temp)


for i in xrange(len(tempList)-1):
    threading.Thread(target=subdomainScan.scan,args=(charset,5,domain,tempList[i],tempList[i+1])).start()

'''
thread.start_new_thread(subdomainScan.scan(charset,5,domain,temp3))
#thread.start_new_thread(subdomainScan.scan(charset,5,domain,temp4))


t1=thread.thread(target=subdomainScan.scan,args=(charset,5,domain,temp1))
t2=Thread(target=subdomainScan.scan,args=(charset,5,domain,temp2))
t3=Thread(target=subdomainScan.scan,args=(charset,5,domain,temp3))
t4=Thread(target=subdomainScan.scan,args=(charset,5,domain,temp4))
'''




