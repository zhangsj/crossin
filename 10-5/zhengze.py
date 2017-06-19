import re
text = "site sea sue sweet see case sse ssee loses"
m = re.findall(r"\bs\S*e\b", text)
if m:
    print m
else:
    print 'not match'