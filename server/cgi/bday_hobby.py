#!/usr/bin/env python
"""Gather and send main hobby and birthday."""
import cgi
FORM = cgi.FieldStorage()
print """Content-type:text/html

Your first name is: %s
<br/>
Your last name is:  %s
<br/>
<br/>
<br/>
<form method="post" action="name_family.py">
    <textarea name="bday" cols="40" rows="5">\
Enter your birthday here... </textarea>
    <br/>
    <textarea name="hobby" cols="40" rows="5">\
Enter your main hobby here... </textarea>
    <br/>
    <input type="submit" value="Submit">
</form>""" % (FORM.getvalue('name'), FORM.getvalue('family'))
