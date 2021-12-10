import pandas as pd
import os
import numpy

d = "C:/Users/Dzeki/PycharmProjects/BERT/data/xml_data"
absolute_path = []
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    absolute_path.append(str(full_path))

    # print(full_path)

col = pd.read_parquet("data/xml_data/pubmed20n0001.parquet.gz").columns
print(col)

print(absolute_path)
# absolute_path_2 = absolute_path[0:10]
data = []
for file in absolute_path :
    data.append(pd.read_parquet(file))
    # print(data)

# print(data)
arr = numpy.array(data)
print(arr.shape)
newarr = arr.reshape((arr.shape[0]*arr.shape[1]), arr.shape[2])
# print(newarr[0:2])

f = pd.DataFrame(newarr, columns=col)
f.to_csv('Pubmed_dataframe.csv', index=False)



# # data = pd.read_parquet("data/xml_data/pubmed20n0001.parquet.gz")
# # print(data.iloc[35]["Abstract"])
#
# data_to_dataframe = {'PubMedID': data["PubMedID"], 'Title': data["Title"], 'Abstract': data["Abstract"]}
# #
# # # Create DataFrame
# df = pd.DataFrame(data_to_dataframe)
# #
# # # Print the output.
# print(df.iloc[0:35,1])

