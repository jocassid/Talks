#!/usr/bin/env python3


def volume(length, width, height):
    """This is what I'm testing.  Ordinarilly this would be in a separate
    file, possibly in a different directory"""
    return length * width * height


def test_volume_1():
    assert volume(1,4,9) == 36.0
    
def test_volume_2():
    assert volume(1,4,9) == 42.0
    
 
class TestSomeStuff:
    """Group tests into classes if you want"""
    
    def test_volume_1(self):
        assert volume(1,4,9) == 36.0
        
    def test_volume_2(self):
        assert volume(1,4,9) == 42.0



