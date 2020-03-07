#!/usr/bin/env python
# coding: utf-8

# # Self-Practice 1 (Housing)
# 
# This is my self-practice to enhance my skill in Python coding. The practice below is based on a random dataset that I downloaded from Kaggle and codes that I learned from DataQuest. 
# 
# In the practice below, the dataset that I downloaded is on housing of an unspecificed location. I will 'play around' with the dataset to extract useful information such as types of house and liveable houses. 

# # 1. Import Dataset

# In[1]:


from csv import reader

opened_file = open('/Users/aimannazmi/Desktop/Housing.csv')
read_file = reader(opened_file)
housing = list(read_file)
housing_header = housing[0]
real_housing = housing[1:]


# # 2. Explore Dataset

# In[2]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
explore_data(real_housing, 0, 5, False)


# # 3. Houses based on Price

# In[3]:


expensive_house = []
cheap_house = []
medium_house = []

for house in real_housing:
    price = float(house[1])
    if price > 100000:
        expensive_house.append(house)
    elif price < 50000:
        cheap_house.append(house)
    else:
        medium_house.append(house)
        
        
print('Expensive house:', len(expensive_house))
print('Cheap house:', len(cheap_house))
print('Medium house:', len(medium_house))
print('\n')
print(len(expensive_house) + len(cheap_house) + len(medium_house))


# # 4. Liveable Houses
# 
# Criteria of livable houses (in my own definition):
# 
# 1. Price is lower than 50,000
# 2. Aircond is required
# 3. Lotsize is bigger than 4000

# In[4]:


best_house = []

for house in real_housing:
    price = float(house[1])
    lotsize = float(house[2])
    aircond = house[10]
    if price < 50000 and aircond == "yes" and lotsize > 4000:
        best_house.append(house)
        
print('Number of best houses:', len(best_house))
print('\n')
print(best_house)


# # 5. Number of rooms

# In[5]:


bedroom_counting = {}

for i in real_housing:
    bedroom = i[3]
    if bedroom in bedroom_counting:
        bedroom_counting[bedroom] += 1
    else:
        bedroom_counting[bedroom] = 1
        
print(bedroom_counting)


# # Conclusion
# 
# In conclusion, there are four houses that I should look into if I seriously consider to buy a house since all of them match the criteria that I set for a liveable house. 
# 
# P.S:
# For this practice, I used coding skills that I learned from DataQuest such as importing csv, list and for loops, frequency tables, and function. 
# 

# In[ ]:




