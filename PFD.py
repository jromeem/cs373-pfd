# Jerome Martinez
# Michael Pace
# C S 373
# PFD.py

import sys

# --------
# pfd_read
# --------

def pfd_read (r) :
    """
    reads first line of ints
    r is a  reader
    return tasks and rules
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    tasks = int(l[0])
    rules = int(l[1])
    
    assert tasks > 0
    assert rules > 0

    return tasks, rules


# ----------
# build_pred
# ----------

def build_pred (r, tasks, rules):
    """
    builds the list of predecessors
    r is the reader
    tasks is the number of tasks
    rules is the number of rules
    return predecessor list
    """
    assert tasks > 0
    assert rules > 0
    
    pred_list = [[]]*(tasks+1)
    for curr_r in range(0, rules):
        line = r.readline().split()
        
        for x in range(0, len(line)):
            line[x] = int(line[x])
        
        pred_list[line[0]] = line[2:]

    assert len(pred_list) > 0
    return pred_list


# ----------
# build_succ
# ----------

def build_succ (pred_list):
    """
    builds the list of successors
    pred_list is the predecessor list
    returns the successor list
    """
    assert len(pred_list) > 0
    
    succ_list = []
    # allocating memory for a list of succesor lists
    for x in range(0, len(pred_list)):
        succ_list.append([])
    
    for curr_pred in range(1, len(pred_list)):
        for curr_succ in pred_list[curr_pred]:
            
            succ_list[curr_succ].append(curr_pred)

    assert len(succ_list) > 0
    return succ_list 


# --------
# pfd_eval
# --------

def pfd_eval (pred_list, succ_list):
    """
    main function that computes the file dependency algorithm
    pred_list is the predecessor list
    succ_list is the successor list
    returns list of values to be outputed
    """
    assert len(pred_list) == len(succ_list)
    
    zero_pred = []
    size = 2 * (len(pred_list)) - 1
    output = []*size

    # find all the starting vertices that are independent
    for vert in range(1, len(pred_list)):
        if pred_list[vert] == []:
            zero_pred.append(vert)

    assert len(zero_pred) > 0
    
    while len(zero_pred):
        # here is our organization
        zero_pred = sorted(zero_pred)
        vert = zero_pred[0]
        
        assert vert == min(zero_pred)
        
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
        
        output += [str(vert)]
        output += [" "]
        zero_pred.remove(vert)

    assert len(zero_pred) == 0
    return output[:-1]


# ---------
# pfd_print
# ---------

def pfd_print (w, int_list):
    """
    prints everything in the list
    w is the writer
    int_list is the list to be outputed
    """
    for x in int_list:
        w.write(x)


# ---------
# pfd_solve
# ---------

def pfd_solve (r, w):
    """
    read first line, build lists, eval, print
    r is a reader
    w is a writer
    """
    tasks, rules = pfd_read(r)
    pred_list = build_pred(r, tasks, rules)
    succ_list = build_succ(pred_list)
    
    output = pfd_eval(pred_list, succ_list)
    pfd_print(w, output)
