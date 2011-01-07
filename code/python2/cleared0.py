# cleared.py
# Mark L. Chang
#
# my first python program
#
# MUST DO:
#  * log into SIS and set the appropriate Session and Year
#  * Check your employee ID in 'Biographical', enter it below for 'myid'
#  * Run from the COMMAND LINE - you will be prompted for user/pass

import urllib, httplib, re
from HTMLParser import HTMLParser

# config
myid = '5501522'
advisee_id_list = []
advisee_chooser_url = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/ids.cgi'
advisee_finder_url = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/main.cgi'
registration_clearance_url = 'https://sis.olin.edu/cgi-bin/faculty/stuadv/addclr.cgi'

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        if tag == 'input':
            #print "Got %s tag attr %s" % (tag, attrs)
            name = attrs[1]
            value = attrs[2]
            if name[1] == 'advisee_id':
                advisee_id = value[1]
                print "Found advisee ID %s" % advisee_id
                advisee_id_list.append(advisee_id)

# get list of advisees
# submit: command = "Select From Advisee List"
form_data = urllib.urlencode({"command": "Select From Advisee List"})
print 'Opening URL to find list of advisees...'
advisee_finder_results = urllib.urlopen(advisee_finder_url,form_data)
advisee_finder_html = advisee_finder_results.read()
advisee_finder_results.close()

# grab the student IDs and names into a dictionary
p = MyHTMLParser()
p.feed(advisee_finder_html)
print "Got these advisees now: "
print advisee_id_list

# cycle through names and IDs to find out if they are cleared for registration
# hidden: user_id
# text: id
# submit: ids_command = Get Name

for advisee in advisee_id_list:
    print 'Selecting ID %s...' % advisee
    form_data = urllib.urlencode({'user_id': myid, 'id': advisee, 'ids_command': 'Get Name'})

    print form_data
    advisee_chooser_results = urllib.urlopen(advisee_chooser_url,form_data)
    print advisee_chooser_results
    
    advisee_chooser_html = advisee_chooser_results.read()
    advisee_chooser_results.close()

    print 'Getting clearance status...'
    clearance_results = urllib.urlopen(registration_clearance_url)
    clearance_html = clearance_results.read()
    clearance_results.close()
    html_lines = clearance_html.splitlines()
    advisee_name = html_lines[29]
    is_not_cleared = re.search(r'The student is NOT cleared', clearance_html)
    if is_not_cleared:
        print advisee_name + ' is not cleared for registration'
    else:
        print advisee_name + ' is cleared for registration'
    print '---------------'
    
