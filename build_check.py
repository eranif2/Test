import os
import sys

print (f'The build ran by {sys.argv[1]}')
    
build = int(os.environ.get('BUILD_NUMBER'))
                                                    
      
if not build%3 == 0:
    print (f'Error: build ran {build} times')
    exit(1)
