import os

build = int(os.environ.get('BUILD_NUMBER'))

print (f'job is ran by: {os.environ.get("PROMOTED_JOB_NAME")}')
print (f'job name is: {os.environ.get("JOB_NAME")}')
if not build%3 == 0:
    print (f'Error: build ran {build} times')
    exit(1)
