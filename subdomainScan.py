import dns.resolver
import bruteforce
res=dns.resolver.Resolver()

def scan(charset,maxlen,domain,temp,stop):
    
    br=bruteforce.BruteForce(temp,maxlen,charset,stop)
    while(len(br.getTemp())<=maxlen and br.completed==False):
        url=br.getTemp()+"."+domain
        #print("Checking "+url)
        try:
            a=res.query(url,"A")
            print("Subdomain found "+"www."+url+" IP:")
            for i in a:
                print(i)
        except :
            pass
        
        br.incr(-1)
    print("Done"+" "+temp+" "+stop)    