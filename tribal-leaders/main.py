import pandas as pd
import numpy as np

# Read in data, store as dataframe
df = pd.read_csv("./data/tribal-leaders.csv", header = 0)

# drop uneeded columns
df = df.drop(df.columns[[1,2,3,4,6,8,9,11,12,13,18,20,23,24,25,26,29,30,31,32,33,34,35,36,37,38,39,40]],axis = 1)

# Combine first and last names into single column
df['Leader'] = df['FirstName'] + " " + df['LastName']

# pop the newly combined column off dataframe
leaders = df.pop('Leader')

# insert the leader column into index 1 on the dataframe
df.insert(loc=1,column='Leader',value=leaders)

# drop uneeded name columns
df = df.drop(['FirstName', 'LastName'], axis = 1)

# rename columns 'TribeFullName' to 'Tribe'
df = df.rename(columns={"TribeFullName": "Tribe", "JobTitle": "Title", "PhysicalAddress": "Physical Address", "DateElected": "Date Elected", "NextElection":"Next Election"})

# pop website links off datafram
#web_links = df.pop('WebSite')

# Get html table format from dataframe method
html_display = df.to_html(index=False, justify='center', table_id='ourTable', render_links=True, na_rep='')

# Open html file to write to
f = open("html/pyth.html", "w")

# Write inital tags
f.write("<!DOCTYPE html>\n\n")
f.write("<head>\n")
f.write("\t<title>Tribal Leaders</title>\n")
f.write("</head>\n\n")
f.write("<body>\n")

# search bar tags
f.write("\t<label style='color:white' for=\"myInput\">Search: </label>\n")
f.write("\t<input type=\"text\" id=\"myInput\" placeholder=\"Tribe\">\n")
f.write("\t<input type='text' id='myInputLeader' placeholder='Leader'>\n")
f.write("\t<br><br>\n")

# dataframe as table in html
f.write(html_display)

# add javascript
f.write("\n\t<script src=\"./display.js\"></script>\n")

# closing tags
f.write("</body>\n\n")
f.write("</html>\n")

# close file
f.close()
