#!/usr/bin/python
"""Repair self-links that are linked from the patch but not defined in the
patch to point back to the main encoding spec.

Ad-hoc re-based parsing is used. Since the input is always expected to be
well-formed HTML and limited in scope, this is good enough.

Modifies "patch.html" by default. It will operate on other file(s) instead if
they are specified on the command-line. Always operates in-place.
"""

import fileinput
import functools
import re
import sys


def read_ids(files):
  """Read all id attributes from the specified HTML files and return them as a
  set.
  """
  ids = set()
  pattern = re.compile(r'\bid="([^"<>]+)"')
  for line in fileinput.input(files):
    for match in pattern.finditer(line):
      ids.add(match.group(1))
  return ids


def replace_links(files, ids):
  """Rewrite the specified HTML files in place. Any self-link that is not
  contained in ids is prepended with https://encoding.spec.whatwg.org/.
  """
  def replace_one_link(match):
    if match.group(1) in ids:
      return match.group(0)
    return 'href="https://encoding.spec.whatwg.org/#%s"' % match.group(1)

  pattern = re.compile(r'\bhref="#([^\"<>]+)"')
  for line in fileinput.input(files, inplace=True):
    sys.stdout.write(pattern.sub(replace_one_link, line))


def main(arguments):
  """Substitute links in the files specified in the arguments. If the arguments
  are empty, defaults to "patch.html".
  """
  files = arguments if arguments else ['patch.html']
  ids = read_ids(files)
  replace_links(files, ids)


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
