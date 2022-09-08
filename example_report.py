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
    
    # imagine we have tiny pygmy shrew 
    #heart_rate = 1000
    #max_heart_rate = 1300
    # ugh this does not work b/c ppg simulate assumes humans w/ max 200 BPM :(
    #Skipping random IBI modulation, since the offset_weight 0.1 leads to physiologically implausible wave durations of 53.99999999999565 milliseconds.
    heart_rate = 40
    max_heart_rate = 90
    ppg = nk.ppg_simulate(sampling_rate=sampling_rate, heart_rate=heart_rate, burst_number=50)
    
    report = str(pathlib.Path("docs", "myreport.html"))
    # if parent path does not exist, create it
    pathlib.Path(report).resolve().parent.mkdir(parents=True, exist_ok=True)
    method="elgendi"
    
    
    ppg_clean_kwargs={"method": "nabian2018", "heart_rate": heart_rate}
    ppg_findpeaks_kwargs={"mindelay": 60/max_heart_rate}
    nk.ppg_process(ppg, sampling_rate=sampling_rate, report=report)