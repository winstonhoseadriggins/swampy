# cleared.py
# Mark L. Chang
#
# my first python program
#
# MUST DO:
#  * log into SIS and set the appropriate Session and Year
#  * Check your employee ID in 'Biographical', enter it below for 'user_id'
#  * Run from the COMMAND LINE - you will be prompted for user/pass

import urllib, httplib, re
from HTMLParser import HTMLParser

# config
user_id = ''
ids = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        if tag == 'input':
            #print "Got %s tag attr %s" % (tag, attrs)
            name = attrs[1]
            value = attrs[2]
            if name[1] == 'advisee_id':
                advisee_id = value[1]
                print "Found advisee ID %s" % advisee_id
                ids.append(advisee_id)

def get_url(url, data=None):
    """download html from (url); (data) is a dictionary of form data
    """
    if data == None:
        fp = urllib.urlopen(url)
    else:
        form_data = urllib.urlencode(data)
        fp = urllib.urlopen(url, form_data)
        
    html = fp.read()
    fp.close()
    return html

# get list of advisees
print 'Opening URL to find list of advisees...'
url = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/main.cgi'
data = dict(command='Select From Advisee List')
html = get_url(url, data)

# grab the student IDs and names into a dictionary
p = MyHTMLParser()
p.feed(html)
print "Got these advisees now: "
print ids

# cycle through names and IDs to find out if they are cleared for registration

for advisee_id in ids:
    print 'Selecting ID %s...' % advisee_id
    url = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/ids.cgi'
    d = dict(user_id=user_id, id=advisee_id, ids_command='Get Name')
    html = get_url(url, data)

    print 'Getting clearance status...'
    url = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/addclr.cgi'
    fp = urllib.urlopen(url)
    html = get_url(url)

    lines = html.splitlines()
    advisee_name = lines[29]
    is_not_cleared = re.search(r'The student is NOT cleared', html)
    if is_not_cleared:
        print advisee_name + ' is not cleared for registration'
    else:
        print advisee_name + ' is cleared for registration'
    print '---------------'
    
