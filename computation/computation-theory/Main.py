'''
Created on Jul 11, 2013

@author: Emmanuel <eruyome@gmail.com> Chourdakis
'''

import pydot


def dfsmToGraph(DFSM):
    graph = pydot.Dot(graph_type = 'digraph', orientation='landscape')
    
    K, S, s, F, delta = DFSM # Unpacking of values
    
    graph.add_node(pydot.Node('start', shape='point'))
    
    for k in K:
        if k in F:
            graph.add_node(pydot.Node(k, shape="doublecircle"))
        else:
            graph.add_node(pydot.Node(k, shape="circle"))
            
    graph.add_edge(pydot.Edge('start',s))
    
    for d in delta:
        q = d[0][0]
        a = d[0][1]
        qs = d[1]
        
        graph.add_edge(pydot.Edge(q,qs,label=a))
        
    
    return graph


    


def applyDFSM(DFSM, Tape, Verbose=False):
    '''
        Runs the Deterministic finite-state machine `DFSM1`
        with input the string `Tape`. Returns `True` if 
        the string of symbols is accepted or `False` if not.
        
        Arguments:
        --`DFSM`: A tuple of the form (K, Sigma, s, F, delta)
                   where:
                           -- `K`<set of `char`>: a set containing
                              all the possible states of the DFSM.
                           
                           -- `Sigma`<set of `char`>: a set containing
                              the symbol dictionary.
                              
                           -- `s`<`char`>: the starting state
                           
                           -- `F`<set of `char`>: a set of the final states
                           
                           -- `delta`: A set of tuples of the form ((q, s), q`) 
                              where q is the current state, s is the current symbol
                              on the tape and q` is the transition state.
                              
        --`Tape` <list of `char`>: A list of symbols representing the
                                   tape as an input to the dfsm.
                              
    '''
    
    K, S, s, F, delta = DFSM # Unpacking of values
    
    if Verbose:
        print "Started running the DFSM."
    
    for i in Tape:
        if Verbose:
            print "-- found symbol `%s`" % str(i)
        s = [m[1] for m in delta if m[0] == (s,i)][0] # New state
        
        if Verbose:
            print "-- new state is `%s`" % str(s)
        
        
    if s in F:
        if Verbose:
            print "Tape accepted."
        return True
    else:
        if Verbose:
            print "Tape not accepted."
        return False


def exampleDFSM1():
    ''' Example Deterministic FSM for the language
        L(M) = {w \in {a, b}* : w has an even number of b's}
        
        Example taken from 
        'Elements of the Theory of Computation 2nd Ed' - H. Lewis, Ch. Papadimitriou
        Greek Edition pg. 91. 
        
    '''
    
    # Example FSM.
    
    K = {'q0','q1'}
    Sigma = {'a','b'}
    s = 'q0'
    F = {'q0'}
    delta = {(('q0','a'),'q0'),\
             (('q0','b'),'q1'),\
             (('q1','a'),'q1'),\
             (('q1','b'),'q0')}
    
    
    DFSM1 = (K, Sigma, s, F, delta)
    
    # Example tape
    
    Tape1 = ['a','a','b','b','a']
    
    if applyDFSM(DFSM1, Tape1, Verbose=True):
        print "String: %s is accepted by DFSM1" % str(Tape1)
    else:
        print "String: %s is not accepted by DFSM1" % str(Tape1)
    
    graph = dfsmToGraph(DFSM1)
    graph.write_png('dfsm1.png')
    
    
def exampleDFSM2():
    ''' Example Deterministic FSM for the language
        L(M) = {w \in {a, b}* : w does not have three consequent b's}
        
        Example taken from 
        'Elements of the Theory of Computation 2nd Ed' - H. Lewis, Ch. Papadimitriou
        Greek Edition pg. 92. 
        
    '''
    # Example FSM.
    
    K = {'q0','q1','q3'}
    Sigma = {'a','b'}
    s = 'q0'
    F = {'q0','q1','q2'}
    
    delta = {(('q0','a'),'q0'),\
             (('q0','b'),'q1'),\
             (('q1','a'),'q0'),\
             (('q1','b'),'q2'),\
             (('q2','a'),'q0'),\
             (('q2','b'),'q3'),\
             (('q3','a'),'q3'),\
             (('q3','b'),'q3')}
    
    
    DFSM2 = (K, Sigma, s, F, delta)
    
    # Example tape
    
    Tape2 = ['a','a','b','b','b','a','b','a','b']
    
    if applyDFSM(DFSM2, Tape2, Verbose=True):
        print "String: %s is accepted by DFSM2" % str(Tape2)
    else:
        print "String: %s is not accepted by DFSM2" % str(Tape2)
    
    graph = dfsmToGraph(DFSM2)
    graph.write_png('dfsm2.png')    
        

if __name__ == '__main__':
    print "Computation theory algorithms."
    exampleDFSM1()
    exampleDFSM2()
    # Sample sets.
    
    

    
        