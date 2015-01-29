#!/usr/bin/env python
"""Gather and send first and last names."""
import cgi
FORM = cgi.FieldStorage()
print """Content-type:text/html

Your birthday is:   %s
<br/>
Your main hobby is: %s
<br/>
<br/>
<br/>
<form method="post" action="bday_hobby.py">
    <textarea name="name" cols="40" rows="5">\
Enter your name here... </textarea>
    <br/>
    <textarea name="family" cols="40" rows="5">\
Enter your family name here... </textarea>
    <br/>
    <input type="submit" value="Submit">
</form>""" % (FORM.getvalue('bday'), FORM.getvalue('hobby'))
