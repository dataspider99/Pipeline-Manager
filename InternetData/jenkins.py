class JenkinsCodeRunner(object):
    jserver = None
    def __init__(self,url,job,user=None,passwd=None):
        self.url = url
        self.user = user
        self.passwd = passwd
        self.job = job
        
JenkinsCodeRunner("http://s1:8090",user="admin",passwd="indian@007#")