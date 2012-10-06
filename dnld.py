# use :%s/^\d\+.*\d\+\s\+//gc 
# to remove useless thing
f = open('chart.txt')
import mechanize
import cookielib
import os
# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

dateProcess = os.popen(r"date +%W-%Y")
dateProcessOutput = dateProcess.readlines()[0][:-1]
mkdirPrcess = os.popen(r"mkdir ~/Music/"+dateProcessOutput)
number = 1
for line in f:
  r = br.open('http://google.com')
  br.select_form(nr=0)
  br.form['q']=line + " mp3"
  br.submit()
  for l in br.links(url_regex='mp3skull.com'):
    print l.url
    br.open(l.url)
    for p in br.links(url_regex='mp3$'):
      line = line.replace("\t"," ")
      filename = os.environ['HOME'] + "/Music/"+dateProcessOutput+"/"+str(number)+".mp3"
      # print filename
      print (br.retrieve(p.url,filename)[0])
      statinfo = os.stat(filename)
      if statinfo.st_size < 5000000:
	os.popen("rm "+filename)
	continue
      number = number + 1
      break
    break
  #if l:
   # print l[0]['url']
        
        #r = br.open(l)
        #print r
