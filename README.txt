CR2WU-NLU
CR2 Water Use estimations , No-Land Use (NLU) sectors in m3/s (1950-2020)

Project ANID/FSEQ210001
FONDAP Research Center (CR)2 (ANID/FONDAP/15110009)
Juan P. Boisier, Camila Alvarez-Garreton, Rodrigo Marinao


In the current directory you will find two folders ("csv" and "GeoJSON"):

1.----> "csv": contains the time series of NLU water uses of the TISHi/ANID-Sequía project. Each file is a time series, where each row corresponds to an annual date, and each column corresponds to a territorial unit that was specified as an id of commune, province, region, or nation.
1.1.------------> "Total": This folder contains four files that summarize (add up) all the uses (all), for each territorial unit. Aditionally, it houses the total water uses folders of all sectors of level 1.
1.1.X.--------------------> Sector "X" of level 1 (e.g. "Mining"): This folder contains four files that summarize (add up) all the uses contained in level 1, for each territorial unit. Aditionally, it houses the total water uses folders of all sectors of level 2.
1.1.X.Y.--------------------------> Sector "Y" of level 2  (e.g. "Metallic"): This folder contains four files that summarize (add up) all the uses contained in level 2, for each territorial unit. Aditionally (and if apply), it houses the total water uses folders of all sectors of level 3.
1.1.X.Y.Z.-------------------------------> Sector "Z" of level 3  (e.g. "Silver"): This folder contains four files corresponding to the use of level 3, for each territorial unit.

2.----> "GeoJSON": Contains vector maps with the territorial units of the country, that correspond to communes, provinces, regions and the entire nation. Each polygon was assigned a unique id that allows associating the territorial units with the columns of the time series.
