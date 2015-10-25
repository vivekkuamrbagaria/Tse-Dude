import time, SimpleDude, CommonFunctions, sys
StartTime = time.time()
# From terminal
if len( sys.argv )> 1 :
    flipProbab = float( sys.argv[1] )
else:
    flipProbab = 0.02

if len( sys.argv )> 2:
    ContextLengthMin = int( sys.argv[2] )
else:
    ContextLengthMin = 3


if len( sys.argv )> 3:
    ContextLengthMax = int( sys.argv[3] )
else:
    ContextLengthMax = 10
    

if len( sys.argv )> 4:
    ReadLength = int( sys.argv[4] )
else:
    ReadLength = 200
    

    
filename = '../original/genome_data.fasta'
ReadLength = 100


shouldIprint =  lambda x, y: True

Obj = SimpleDude.System( ContextLengthMin = ContextLengthMin, ContextLengthMax = ContextLengthMax, flipProbab=flipProbab, shouldIprint=shouldIprint)
Obj.ReadSimulation( filename, ReadLength = ReadLength )
print( "total execution time", time.time() - StartTime)
