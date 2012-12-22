#!/usr/bin/env python
print "Content-Type: text/html"
print
print """\
<html><body>
<form method="post" action="process_check.py">
Red<input type="checkbox" name="color" value="red">
Green<input type="checkbox" name="color" value="green">
<input type="submit" value="Submit">
</form>
</body></html>
"""
