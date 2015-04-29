#!/usr/bin/env python
# Tai Sakuma <sakuma@cern.ch>
import pandas as pd

##__________________________________________________________________||
d1 = pd.read_table('tbl_count_dataset.txt', delim_whitespace = True)
d2 = pd.read_table('tbl_dataset_info.txt', delim_whitespace = True)

d = pd.merge(d2, d1)
lumi = 4000
d.n = d.n*d.xsec/d.nevt*lumi
d.nvar = d.nvar*(d.xsec/d.nevt*lumi)**2
del d['nevt']
del d['xsec']
d = d.groupby(['process', 'met']).sum().reset_index()

f = open('tbl_yield_process.txt', 'w')
d.to_string(f, index = False)
f.write("\n")
f.close()

##__________________________________________________________________||
