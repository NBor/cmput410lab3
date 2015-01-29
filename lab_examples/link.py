#!/usr/bin/env python
"""Linking CGI script."""
print 'Content-type:text/html'
print
print '<html><head><title>Test URL Encoding</title>'
print '<a href=\"http://127.0.0.1:8888/test_urlencode.py?first=Jack&last=Trades\">Link</a>'
print '</head></html>'
