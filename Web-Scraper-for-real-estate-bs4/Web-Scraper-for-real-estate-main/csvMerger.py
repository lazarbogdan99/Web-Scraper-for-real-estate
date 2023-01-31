from doctest import master
import os
import pandas as pd

master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if(file.startswith('page')):
        master_df = master_df.append(pd.read_csv(file))

master_df.to_csv('Master File ImobiliareRoNou.CSV' , index= False)

