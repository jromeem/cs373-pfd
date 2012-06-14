# Jerome Martinez
# Michael Pace
# C S 373
# SpherePFD.py

print "hello world!"


import sys

# ------------
# pfd_read
# ------------

def pfd_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array on int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True


def pfd_solve (r, w):
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """

    """
    List of vertices []

    for each vertex :
        no. of predecessor: int
        list of all predecessors: [int]
        list of successors: [int]

    container of 0-predcessor vertices: [int]

    for each 0-pred vertex in container:
        find 0-pred vertices 
        find the lowest value in the 0-pred list
        print that vertex
        decrement the pred-count each of the successors
