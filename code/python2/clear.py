#!/usr/bin/env python
#
# python sis clearing tool for your advisees
# version 1.00
#
# requires:
#  BeautifulSoup
#  httplib2
###

import cgi
import cgitb; cgitb.enable()

import sys
import httplib2
import BeautifulSoup
import re
from time import sleep
from urllib import urlencode

# ---------- defines ----------
DEBUG = False
VERBOSE = True
SESSION = 'SP'
YEAR = '2009'
URL_SIS = 'https://sis.olin.edu/cgi-bin/faculty'
URL_SESSIONYEAR = 'https://sis.olin.edu/cgi-bin/faculty/setopt.cgi'
URL_ADVISEE_CHOOSER = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/ids.cgi'
URL_ADVISEE_FINDER = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/main.cgi'
URL_CLEARANCE = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/addclr.cgi'

# ---------- strings ----------

htmlLoginForm = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
   <head>
      <title>SIS Advisee Clearance Tool</title>
   </head>
   <body>
     <h1>
        SIS Clearance Shortcut Tool
     </h1>
     <p>
        No guarantees that this program won't blow up your
        computer and end the universe.
     </p>
     <p>
        This program caches your credentials (username and password)
        in <i>cleartext</i> on the next page. If this bothers you,
        a) don't use the program, or b) make sure to close your browser
        completely when you are done. It was too much work to do it
        otherwise. Everything transmitted between compters is secured
        using SSL, so the only security hole is inside your browser.
     </p>
     <p>
        This script will modify students for <b>%s %s</b>.
     </p>
     <form method="post" action="clear.py">
       <p>
         Olin login: <input type="text" name="username" />
         Password: <input type="password" name="password" />
         <input type="submit" value="Login" />
         <input type="hidden" name="state" value="login" />
       </p>
     </form>
   </body>
</html>
""" 

htmlHeader = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
   <head>
      <title>%s</title>
   </head>
   <body>

"""

htmlClearanceFormStart = """
     <form method="post" action="clear.py">
       <p>
         <input type="hidden" name="state" value="clear" />
         <input type="hidden" name="username" value="%s" />
         <input type="hidden" name="password" value="%s" />
         <input type="hidden" name="facultyid" value="%s" />

"""

htmlClearanceAdvisee = """
         <input type="radio" name="%s" value="True" %s />Cleared
         <input type="radio" name="%s" value="False" %s />Not Cleared | %s
         <br />
"""

htmlClearanceFormEnd = """
      </p>
      <p>
        <input type="submit" value="Commit" />
      </p>
     </form>
   </body>
</html>

"""

# ---------- funcs ----------
def printHeader():
    print "Content-type: text/html"
    print

def printLoginForm():
    printHeader()
    print htmlLoginForm % (SESSION, YEAR)

def printClearanceForm(adviseeList,facultyId,username,password):
    print htmlClearanceFormStart % (username,password,facultyId)
    for advisee in adviseeList:
        if advisee['cleared']:
            checked = ['checked="checked"','']
        else:
            checked = ['','checked="checked"']
        print htmlClearanceAdvisee % (advisee['id'],
                                      checked[0],
                                      advisee['id'],
                                      checked[1],
                                      advisee['name'])
        sys.stdout.flush()
    print htmlClearanceFormEnd

def openHttp(username,password):
    h = httplib2.Http()
    h.add_credentials(username,password)
    return h

def setSessionYear():
    formData = {"prog":"UNDG", 
                "sess":SESSION, 
                "yr":YEAR, 
                "action":URL_SIS,
                "setopt_command":"Submit Options"}
    formDataEncoded = urlencode(formData)
    resp, content = h.request(URL_SESSIONYEAR,"POST", formDataEncoded)
    if resp['status'] != '200':
        return False
    else:
        return True

def getFacultyId():
    resp, content = h.request(URL_ADVISEE_FINDER,"GET")
    if resp['status'] != '200':
        return None
    else:
        soup = BeautifulSoup.BeautifulSoup(content)
        facultyId = soup.findAll('input',attrs={'type':'hidden','name':'user_id'})[0]['value']
        return facultyId

def getAdviseeList():
    formData = {"command": "Select From Advisee List"}
    formDataEncoded = urlencode(formData)
    resp, content = h.request(URL_ADVISEE_FINDER,"POST",formDataEncoded)
    if resp['status'] != '200':
        return None
    else:
        soup = BeautifulSoup.BeautifulSoup(content)
        adviseeList = [ {'name':x('td')[1].string.strip(),'id':x('td')[2].string} for x in soup.form.table('tr',attrs={'class':'glbdatadark'})]
        return adviseeList

def setAdvisee(adviseeId,facultyId):
    formData = {'user_id': facultyId, 
                'id': adviseeId,
                'ids_command': 'Get Name'}
    formDataEncoded = urlencode(formData)
    resp, content = h.request(URL_ADVISEE_CHOOSER,"POST",formDataEncoded)
    if resp['status'] != '200':
        return False
    else:
        return True

def isAdviseeCleared():
    resp, content = h.request(URL_CLEARANCE,"GET")
    if resp['status'] != '200':
        return None
    else:
        soup = BeautifulSoup.BeautifulSoup(content)
        if soup('input',attrs={'name':'command'})[0]['value']=='Remove Clearance':
            return True
        elif soup('input',attrs={'name':'command'})[0]['value']=='Add Clearance':
            return False
        else:
            return None

def getClearedStatus(adviseeList,facultyId):
    if VERBOSE:
        print "<pre>"
        sys.stdout.write("[")
        for x in range(0,len(adviseeList)):
            sys.stdout.write(".")
        sys.stdout.write("]\n[")
        sys.stdout.flush()
    for advisee in adviseeList:
        setAdvisee( advisee['id'], facultyId)
        advisee['cleared'] = isAdviseeCleared()
        if advisee['cleared'] == None:
            print "Oops. Can't seem to get clearance status for %s" % advisee['name']
            return None
        else:
            if DEBUG:
                print "%s<br />" % advisee
                sys.stdout.flush()

            if VERBOSE:
                sys.stdout.write("=")
                sys.stdout.flush()

    if VERBOSE:
        sys.stdout.write("]\n")
        print "</pre>"
        print "<br />"
        sys.stdout.flush()
    
    return adviseeList

def getAllForm(theform, nolist=False):
    """
    Passed a form (cgi.FieldStorage
    instance) return *all* the values.
    This doesn't take into account
    multipart form data (file uploads).
    It also takes a keyword argument
    'nolist'. If this is True list values
    only return their first value.
    """
    data = {}
    for field in theform.keys():                
        # we can't just iterate over it, but must use the keys() method
        if type(theform[field]) ==  type([]):
            if not nolist:
                data[field] = theform.getlist(field)
            else:
                data[field] = theform.getfirst(field)
        else:
            data[field] = theform[field].value
    
    return data

def setClearance(cleared):
    if cleared:
        form_data = urlencode({"command": "Add Clearance"})
    else:
        form_data = urlencode({"command": "Remove Clearance"})

    resp, content = h.request(URL_CLEARANCE,"POST",form_data)
    if resp['status'] != '200' and resp['status'] != '500':
        print "I had problems setting clearance!"
        sys.exit()

# ---------- main ----------

# grab form entries
form = cgi.FieldStorage()

# pick off our state from hidden form field
state = form.getvalue('state','none')

# program logic
if state == 'none':
    printLoginForm()
elif state == 'login':
    username=form.getvalue('username')
    password=form.getvalue('password')
    if username == None or password == None:
        # oops, send user back
        printLoginForm()
    else:
        printHeader()
        h = openHttp(username,password)
        print htmlHeader % "Clear Your Advisees"
        print """
<p>
Loading your advisees from SIS. Be patient. This takes about 3 seconds
per advisee!
</p>
"""
        sys.stdout.flush()

        # get faculty ID
        if DEBUG:
            print "Getting your faculty SIS ID<br />"
            print "Please wait about 3 seconds<br />"
            sys.stdout.flush()
        facultyId = getFacultyId()
        if facultyId == None:
            print "Oops. I think there was an authentication error! Try again."
            sys.exit()
        else:
            if DEBUG: print "Your faculty id is %s<br />" % facultyId

        # set session/year
        if DEBUG:
            print "Now setting session/year to %s %s<br />" % (SESSION, YEAR)
            print "Please wait about 3 seconds<br />"
            sys.stdout.flush()
        if not setSessionYear():
            print "Oops. Problem setting session and year!"
            sys.exit()
        else:
            if DEBUG: print "Session correctly set<br />"

        # get advisee list
        if DEBUG:
            print "Getting a list of your advisees<br />"
            print "Please wait about 3 seconds<br />"
            sys.stdout.flush()
        adviseeList = getAdviseeList()
        if adviseeList == None:
            print "Oops. Problem fetching the advisee list!"
            sys.exit()
        else:
            if DEBUG: print "Got list your advisees<br />"

        # update advisee list with cleared status
        if DEBUG:
            print "Getting clearance status for each advisee<br />"
            print "Please wait about 3 seconds per advisee<br />"
            sys.stdout.flush()
        adviseeList = getClearedStatus(adviseeList,facultyId)
        if adviseeList == None:
            print "Oops. Problem setting cleared status for your advisees!"
            sys.exit()

        # print the form to update clearance
        printClearanceForm(adviseeList,facultyId,username,password)
        sys.exit()

elif state == 'clear':
    username = form.getvalue('username')
    password = form.getvalue('password')
    facultyId = form.getvalue('facultyid')
    if username == None or password == None:
        # oops, send user back
        printLoginForm()
        sys.exit()

    # else
    printHeader()
    print htmlHeader % "Clearance Results"
    h = openHttp(username,password)

    # grab all form things
    formDict = getAllForm(form)
    # and remove the ones we already consumed
    del formDict['username']
    del formDict['password']
    del formDict['state']
    del formDict['facultyid']
    # leaving behind just the advisee list

    print "<p>Setting clearance for %s students. This will take about 3 seconds per student.</p>" % len(formDict)
    sys.stdout.flush()

    if VERBOSE:
        print "<pre>"
        sys.stdout.write("[")
        for x in range(0,len(formDict)):
            sys.stdout.write(".")
        sys.stdout.write("]\n[")
        sys.stdout.flush()

    for id,cleared in formDict.iteritems():
        if DEBUG: 
            print "Setting clearance on ", id, cleared, "<br />"
            sys.stdout.flush()
        if not setAdvisee(id,facultyId):
            print "Oops, I had trouble setting advisee to %s" % id
            sys.exit()

        if cleared=='True':
            setClearance(True)
        else:
            setClearance(False)

        if VERBOSE:
            sys.stdout.write("=")
            sys.stdout.flush()

    print "]</pre>"
    print "<p>Done setting clearances</p>"
    print "<p>Now, wasn't that easier than SIS?</p>"
    print "</body></html>"
