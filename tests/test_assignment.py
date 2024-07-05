import pathlib
import os
import re
import urllib.request

def file_basic_check(f):
    # Test file existence and not empty
    assert pathlib.Path(f).is_file()
    assert pathlib.Path(f).stat().st_size > 0

def file_regex(f, regex):
    # Test the content of a file against a regex
    with open(f) as fi:
        text = fi.read()
        return re.search(regex, text)
    
def test_q1a():
    file_basic_check('q1a.txt')

def test_extract_thumbs():
    file_basic_check('extract_thumbs.sh')
    
def test_brute_force():
    file_basic_check('brute_force.sh')


