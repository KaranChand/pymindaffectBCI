import numpy as np
from mindaffectBCI.decoder.datasets import get_dataset
import matplotlib.pyplot as plt
from mindaffectBCI.decoder.analyse_datasets import analyse_dataset, analyse_datasets, debug_test_dataset, debug_test_single_dataset

datasetsdir = "datasets"

dataset_loader, dataset_files, dataroot = get_dataset('mindaffectBCI',exptdir=datasetsdir)
print("Got {} datasets\n".format(len(dataset_files))) # Got 16 datasets

# Analysis
analyse_datasets('mindaffectBCI',dataset_args=dict(exptdir=datasetsdir),
                 loader_args=dict(fs_out=100,stopband=((45,65),(5,25,'bandpass'))),
                 preprocess_args=None,
                 model='cca',test_idx=slice(10,None),clsfr_args=dict(tau_ms=450,evtlabs=('re','fe'),rank=1))

# All these outputs are useful and provide a nice summary.
# We should try to get them to be in a dashboard after MLOps