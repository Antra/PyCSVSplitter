import pandas as pd
import numpy as np

delimiter = ';'
org_file = 'test.csv'
df = pd.read_csv(org_file, delimiter=delimiter)

groups = df.groupby(np.arange(len(df.index))/10000)
for (frameno, frame) in groups:
    filename = groups.get_group(frameno).values[0][0].replace(':', '')
    #frame.to_csv("%s.csv" % filename, sep=delimiter, header=True, index=False, encoding="ISO-8859-1")
    frame.to_csv(f'{filename}.csv', sep=delimiter, header=True,
                 index=False, encoding="ISO-8859-1")
