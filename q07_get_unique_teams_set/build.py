# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    ipl_data = read_ipl_data_csv(path,'|S50')
    team_1 = np.unique(ipl_data[:,3])
    team_2 = np.unique(ipl_data[:,4])
    teams = set(np.concatenate((team_1,team_2),axis=0))
    return teams
    
get_unique_teams_set()


