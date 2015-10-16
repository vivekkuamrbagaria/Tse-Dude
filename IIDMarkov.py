import time, SimpleDude, CommonFunctions, sys
StartTime = time.time()
# From terminal

if len( sys.argv )> 1 :
    SequenceLength = int( float( sys.argv[1] ) )
else:
    SequenceLength = int( 1e2 )

if len( sys.argv )> 2 :
    flipProbab = float( sys.argv[2] )
else:
    flipProbab = 0.1

if len( sys.argv )> 3:
    ContextLengthMin = int( sys.argv[3] )
else:
    ContextLengthMin = 1


if len( sys.argv )> 4:
    ContextLengthMax = int( sys.argv[4] )
else:
    ContextLengthMax = 6




Ratio = .7
markovTransitionProbab = .75
shouldIprint =  lambda x, y: False

Obj = SimpleDude.System( MarkovSequenceLength = SequenceLength, ContextLengthMin = ContextLengthMin, ContextLengthMax = ContextLengthMax, flipProbab=flipProbab, shouldIprint = shouldIprint)
Obj.IIDMarkov(markovTransitionProbab)
# 
# for i in range(len(I)):
#     if ( I[i] != O[i] ):
#         print( i )
#         print( "In", I[i-3:i+4])
#         print( "Re", C[i-3:i+4])
#         print( "Ou", O[i-3:i+4], "\n")
#         a= 10
print( "total execution time", time.time() - StartTime)
