import os
import pathlib
import sys

if __name__ == "__main__":
    
    # importing neurokit2 as a submodule so that it's always the same version
    repo_name = "neurokit2-ppg-report-example"
    submodule_parent_dir = "lib"
    submodule_name = "NeuroKit"
    
    repo_path = os.getcwd()
    base_dir = os.path.basename(repo_path)
    while base_dir != repo_name:
        repo_path = os.path.dirname(os.path.abspath(repo_path))
        base_dir = os.path.basename(repo_path)
    
    submodule_path = os.path.join(repo_path, submodule_parent_dir, submodule_name)
    sys.path.insert(0, submodule_path)

    import neurokit2 as nk
    
    # load biosignal data
    data = nk.data(dataset="bio_resting_5min_100hz")
    # get PPG channel
    ppg = data["PPG"]
    # sampling rate in file name
    sampling_rate = 100
    nk.ppg_process(ppg, sampling_rate=sampling_rate, report="myreport.html")