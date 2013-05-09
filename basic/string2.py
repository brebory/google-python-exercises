#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
	l = len(s)
	if l < 3:
		s = s
	elif s[-3:l] == "ing":
		s += "ly"
	else:
		s += "ing"
	return s

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
	notindex = s.find("not")
	badindex = s.find("bad")
	if (notindex < badindex) and (notindex >= 0):
		s = s.replace(s[notindex:badindex + 3], "good")
	return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
	la, lb = (len(a), len(b))
	result = ""
	if la % 2 == 0:
		if lb % 2 == 0:
			result = a[0:la / 2] + b[0:lb / 2] + a[(la / 2):la + 1] + b[(lb / 2):lb + 1]
		else:
			result = a[0:la / 2] + b[0:int(lb / 2) + 1] + a[(la / 2):la + 1] + b[int((lb / 2)) + 1:lb + 1]
	else:
		if lb % 2 == 0:
			result = a[0:int(la / 2) + 1] + b[0:lb / 2] + a[int((la / 2)) + 1:la + 1] + b[(lb / 2):lb + 1]
		else:
			result = a[0:int(la / 2) + 1] + b[0:int(lb / 2) + 1] + a[int((la / 2)) + 1:la + 1] + b[int((lb / 2)) + 1:lb + 1]
	return result



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
