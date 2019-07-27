#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(debug='False' ,  url='mysql+pymysql://root:pass@mysql/mendako?charset=utf8', repository='.')
