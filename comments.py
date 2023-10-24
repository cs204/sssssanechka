import sm

x1 = '''def f(x):  # func
   if x:   # test
     # comment
     return 'foo' '''

x2 = '''#initial comment
def f(x):  # func
   if x:   # test
     # comment
     return 'foo' '''


class CommentsSM(sm.SM):
    startState = 'code'  # fix this

    def getNextValues(self, state, inp):
        # your code here
        if state == 'code':
            if inp == '#':
                return ('comment', '#')
            else:
                return ('code', None)
        else:
            if inp == '\n':
                return ('code', None)
            else:
                return ('comment', inp)


def runTestsComm():
    m = CommentsSM()
    # Return only the outputs that are not None
    print( 'Test1:',  [c for c in CommentsSM().transduce(x1) if not c==None])
    print( 'Test2:',  [c for c in CommentsSM().transduce(x2) if not c==None])
    # Test that self.state is not being changed.
    m = CommentsSM()
    m.start()
    [m.getNextValues(m.state, i) for i in ' #foo #bar']
    print( 'Test3:', [c for c in [m.step(i) for i in x2] if not c==None])

# execute runTestsComm() to carry out the testing, you should get:
runTestsComm()

#Test1: ['#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
#Test2: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
#Test3: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']


