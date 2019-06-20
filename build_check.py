import os

build = int(os.environ.get('BUILD_NUMBER'))


if not build%3 == 0:
    print (f'Error: build ran {build} times')
    exit(1)
