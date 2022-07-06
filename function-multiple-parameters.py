opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table (apps_data, 10)
print (content_ratings_ft)
print (' ')

ratings_ft = freq_table (apps_data, 7)
print (ratings_ft)
print (' ')

genres_ft = freq_table (apps_data, 11)
print (genres_ft)