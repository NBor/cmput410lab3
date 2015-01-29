#!/usr/bin/env python
"""Form."""
print """Content-type:text/html

<form method="post" action="test_form.py">
<textarea name="comments" cols="40" rows="5">
Enter Comments here...
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""
