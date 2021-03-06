#!/usr/bin/env python
""" I will now try to run some estimations.
"""

import os
if True:
    cwd = os.getcwd()
    os.chdir('../../respy')
    assert os.system('./waf distclean; ./waf configure build > allout.txt 2>&1 ') == 0
    os.chdir(cwd)
else:
    print('not compiling')

import sys
import time
from respy import RespyCls, estimate
sys.path.insert(0, '/home/peisenha/Dropbox/business/office/workspace/software/repositories/organizations/restudToolbox/package/respy/tests')



#respy_obj = RespyCls('model.respy.ini')
#simulate(respy_obj)
#x, crit_val = estimate(respy_obj)
print('working PYTHON')
respy_obj = RespyCls('model.respy.ini')
#respy_obj.attr['version'] = 'PYTHON'
#respy_obj.attr['optimizer_used'] = 'SCIPY-POWELL'
start = time.time()

x, crit_val = estimate(respy_obj)
end = time.time()
print(end - start, crit_val)