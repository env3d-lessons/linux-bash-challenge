import pytest
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

@pytest.fixture
def q1a_results():
    print('fixture')
    return os.popen('bash q1a.txt').readlines()

def test_q1a_exec_check_0(q1a_results):
    assert len(q1a_results) > 0, "no results produced"

def test_q1a_exec_check_1(q1a_results):
    assert len([ url for url in q1a_results if 'thumbs.redditmedia.com' in url]) == len(q1a_results), (
        "all links must contain thumbs.redditmedia.com")

def test_q1a_exec_check_2(q1a_results):
    print(q1a_results)
    assert len([ url for url in q1a_results if
                 url.endswith('gif\n') or url.endswith('jpg\n') or url.endswith('png\n')]
               ) == len(q1a_results), "all links must end with gif, jpg, or png"    
    
def test_extract_thumbs():
    file_basic_check('extract_thumbs.sh')


@pytest.fixture
def path_pics():
    os.popen('./extract_thumbs.sh pics').read()
    yield pathlib.Path('./thumbs_pics')
    os.popen('rm -r ./thumbs_pics').read()
    
def test_extract_thumbs_exec_1(path_pics):
    assert path_pics.is_dir()

def test_extract_thumbs_exec_2(path_pics):
    assert len( list(path_pics.glob('*.gif')) +
                list(path_pics.glob('*.jpg')) +
                list(path_pics.glob('*.png'))
               ) > 0
    
def test_brute_force():
    file_basic_check('brute_force.sh')

def test_brute_force_content():
    assert file_regex('brute_force.sh', 'curl.*10k-most-common.txt.*head'), (
        "Must curl the password file")
    assert file_regex('brute_force.sh', 'learn.operatoroverload.com/~jmadar/protected/index.html'), (
        "Must curl to the protected url")
    
def test_brute_force_exec():
    result = os.popen('./brute_force.sh').read()
    assert 'brute force attack :D' in result, "Incorrect secret message"
    
