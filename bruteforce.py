class BruteForce():
    def __init__(self,temp,maxlen,charset,stop):
        self.charset=charset
        self.temp=temp
        self.maxlen=maxlen
        self.stop=stop
        self.completed=False
    
    def incr(self,index):
        if len(self.temp)<=self.maxlen and self.temp!=self.stop:
            if(abs(index)>len(self.temp)):
                    self.temp.insert(0,self.charset[0])
                    
            else:
                if(self.temp[index]==self.charset[-1]):
                    self.temp[index]=self.charset[0]
                    self.incr(index-1)
                else:
                        self.temp[index]=self.charset[self.charset.index(str(unichr(self.temp[index])))+1]
        else:
            self.completed=True
                          
             
    def getTemp(self):
        return str(self.temp)