# Jerome Martinez
# Michael Pace
# C S 373
# SpherePFD.py

import sys

# ------------
# pfd_read
# ------------

def pfd_read (r) :
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
    tasks = int(l[0])
    rules = int(l[1])
    
    assert tasks > 0
    assert rules > 0

    pred_list = [[]]*(tasks+1)
    
    for curr_r in range(0, rules):
        line = r.readline()
        temp = line.split()
        
        for x in range(0, len(temp)):
            temp[x] = int(temp[x])
            
        pred_list[temp[0]] = temp[2:]


    
    succ_list = []
    for x in range(0, len(pred_list)):
        succ_list.append([])
    
    for curr_pred in range(1, len(pred_list)):
        for curr_succ in pred_list[curr_pred]:
            
            succ_list[curr_succ].append(curr_pred)

    return pred_list, succ_list 

def pfd_solve (r, w):
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    p = pfd_read(r)
    pred_list = p[0]
    succ_list = p[1]

    #print "pred_list", pred_list
    #print "succ_list", succ_list
    pfd_eval(pred_list, succ_list)

def pfd_eval (pred_list, succ_list):
    zero_pred = []
    output_string = ""

    for vert in range(1, len(pred_list)):
        if pred_list[vert] == []:
            zero_pred.append(vert)

    # NOTES TO SELVES:
    # below, originally had for vert in zero_pred: instead of while loop, but
    # this didn't work, since it looks like the for loop structure only
    # checked the elements of zero_pred before beginning to iterate, but
    # not after each iteration.
    # so as a while loop, we're safe, since it continues to check that condition.
    while len(zero_pred):
        vert = zero_pred[0]
        pred_count = 0
        min_vert = 0
        min_vert_count = 200
        
        for succ in succ_list[vert]:
            pred_count = len(pred_list[succ])

            if pred_count < min_vert_count:
                min_vert = succ
                min_vert_count = pred_count
            
            pred_list[succ].remove(vert)  

            if len(pred_list[succ]) == 0:
                zero_pred.append(succ)
                #print vert
        
        output_string += str(vert) + " "
        zero_pred.remove(vert)
        
    print output_string[:-1]
    #print "zero_pred", zero_pred
    #print "pred_list", pred_list

# ----
# main
# ----

pfd_solve(sys.stdin, sys.stdout)
