import re

http_regex = re.compile(r'''(
            (http(s)?://)?      # http(s) part 
            (www\.)?            # optional www part
            ([a-zA-Z0-9-_.])+   # domain name part
            (\.)                # dot
            ([a-z]{2,6})        # zone part
)''', re.VERBOSE)

text = u'lgjdsljgg http://sdkjfsdlf.com fasljflljj www.tal.co влоалуко44до https://df344.444.co' \
       'dlsjl owieu щoeru http://www.ggg33.hr www.ghg.jhjh.ll'

for i, sites in enumerate(http_regex.findall(text)):
    print(str(i+1) + '.', sites[0])
