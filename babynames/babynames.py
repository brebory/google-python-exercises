#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import string

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  with open(filename) as f:
    data = f.read()
    rank_dict = {}
    results = []

    # Grab the date from the correct <h2> or <h3>
    date = re.search(r"<h\d\D+(\d+)</h\d>", data)
    # Store tuples of all matches in the form (rank, boy_name, girl_name)
    matches = re.findall(r"<[\w\s]+=\"\w+\"><\w+>(\d+)</td><td>(\w+)</td><td>(\w+)</td>", data)
    results.append(date.group(1))

    # Convert tuples to dict, make sure to only update first occurance of each name
    for match in matches:
      rank, boy_name, girl_name = match
      if boy_name not in rank_dict:
        rank_dict[boy_name] = rank
      if girl_name not in rank_dict:
        rank_dict[girl_name] = rank

    # Format the results, then return the sorted list
    for key, value in rank_dict.items():
      results.append("%s %s" % (key, value))

    return sorted(results)

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names_list = extract_names(filename)
    formatted_list =  "\n".join(names_list) + "\n"
    if summary:
      with open(filename + ".summary", "w") as f:
        f.write(formatted_list)
    else:
      print formatted_list
  
if __name__ == '__main__':
  main()