import subdomainScan
import threading
import thread

temp1=bytearray("aaaa")

temp2=bytearray("haaa")
temp3=bytearray("maaa")
temp4=bytearray("taaa")
charset=bytearray("abcdefghijklmnopqrstuvwxyz1234567890-")
domain="fb.com"
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




