import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

wood.rename(columns = {
  "Supplier" : "supplier",
  "Rank" : "rank_s",
  "Name" : "name",
  "Park" : "park",
  "Location" : "location",
  "Year Built" : "year_built",
  "Points" : "points",
  "Year of Rank" : "year_of_rank"
}, inplace = True)

steel.rename(columns = {
  "Supplier" : "supplier",
  "Rank" : "rank_s",
  "Name" : "name",
  "Park" : "park",
  "Location" : "location",
  "Year Built" : "year_built",
  "Points" : "points",
  "Year of Rank" : "year_of_rank"
}, inplace = True)

print (wood.supplier.nunique())
print (steel.supplier.nunique())

print (wood.head())
print (steel.head())

# write function to plot rankings over time for 1 roller coaster here:
def coaster_rankings(coaster_name, park_name, material):
  if material == 'wood':
    select_all_coaster_datas = wood[(wood.name == coaster_name) & (wood.park == park_name)]
    
  if material == "steel":
    select_all_coaster_datas = steel[(steel.name == coaster_name) & (steel.park == park_name)]
    
  #if (material != "wood") & (material !="steel"):
    #print("error in materials/Can't find rollar coaster")
    
  x_values = select_all_coaster_datas.year_of_rank
  y_values = select_all_coaster_datas.rank_s
  outcome = plt.figure(figsize = (10,8))
  plt.plot(range(len(x_values)), y_values, marker = "o", linewidth = 2, color = "green")
  ax = plt.subplot()
  ax.set_xticks(range(len(x_values)))
  ax.set_xticklabels(x_values)
  ax.invert_yaxis()
  plt.xlabel("Year of Ranking")
  plt.ylabel("Ranking")
  plt.title("Ranking for " + coaster_name + " Over Time")
  plt.show()

coaster_rankings("El Toro", "Six Flags Great Adventure", "wood")  

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def coaster_rankings(coaster_name1, park_name1, material1, coaster_name2, park_name2, material2):
  if material1 == 'wood':
    select_all_coaster_datas1 = wood[(wood.name == coaster_name1) & (wood.park == park_name1)]
  if material2 == "wood":
    select_all_coaster_datas2 = wood[(wood.name == coaster_name2) & (wood.park == park_name2)]
    
  if material1 == "steel":
    select_all_coaster_datas1 = steel[(steel.name == coaster_name1) & (steel.park == park_name1)]
  if material2 == "steel":
    select_all_coaster_datas2 = steel[(steel.name == coaster_name2) & (steel.park == park_name2)]
    
  #Now plot the first line.   
  x_values1 = select_all_coaster_datas1.year_of_rank
  y_values1 = select_all_coaster_datas1.rank_s
  plt.figure(figsize = (10,8))
  plt.plot(range(len(x_values1)), y_values1, marker = "o", linewidth = 2, label = coaster_name1)
  ax = plt.subplot()
  ax.set_xticks(range(len(x_values1)))
  ax.set_xticklabels(x_values1)
  ax.invert_yaxis()
  plt.xlabel("Year of Ranking")
  plt.ylabel("Ranking")
  plt.title("Ranking for Two Roller Coaster Over Time")

  #Now plot the second line.
  x_values2 = select_all_coaster_datas2.year_of_rank
  y_values2 = select_all_coaster_datas2.rank_s
  plt.plot(range(len(x_values2)), y_values2, marker = "o", linewidth = 2, label = coaster_name2)
  
  plt.legend()
  plt.show()

  
coaster_rankings("El Toro", "Six Flags Great Adventure", "wood", "Boulder Dash", "Lake Compounce", "wood")

plt.clf()

# write function to plot top n rankings over time here:
def plot_top_n(material, n):
  #Select all the datas that are top n.
  top_n_rankings = material[material.rank_s <= n]

  #Select one specific roller coaster's datas.
  for one_roller_coaster_name in set(top_n_rankings.name):
      one_roller_coaster_datas = top_n_rankings[top_n_rankings.name == one_roller_coaster_name]
      plt.plot(one_roller_coaster_datas.year_of_rank, one_roller_coaster_datas.rank_s, marker = '*', label = one_roller_coaster_name)
  plt.legend()
  plt.title("Top " + str(n) + " Roller Coasters' Rankings")
  plt.xlabel("Year of Rank")
  plt.ylabel("Rankings")
  ax = plt.subplot()
  
  plt.show()


plot_top_n(steel, 4)

plt.clf()

# load roller coaster data here:
roller_coasters = pd.read_csv("roller_coasters.csv")
print (roller_coasters.head())

# write function to plot histogram of column values here:
def plot_his(column, dataframe):
  datas_to_plot = dataframe[column]
  plt.hist(datas_to_plot.dropna(), normed = True)
  plt.title("The Distribution of " + column + " for Roller Coasters")
  plt.xlabel(column)
  plt.ylabel("Frequency")
  plt.show()

plot_his('speed', roller_coasters)
plot_his('length', roller_coasters)

# bar chart
roller_coasters.rename(columns={
  'num_inversions':'inversions',
  'material_type':'material'}, inplace = True)

def number_of_inversions(roller_coasters, park):
  park_data = roller_coasters.park
  inversions_data = park_data.inversions
  roller_coaster = park_data.name
  plt.bar(range(len(roller_coaster)), inversions_data)
  plt.title("Inversions Roller Coaster")
  plt.xlabel("Roller Coaster Name")
  plt.ylabel("Inversions")
  ax = plt.subplot()
  ax.set_xticks(range(len(roller_coaster_name)))
  ax.set_xticklabels(roller_coaster_name, rotation = 30)
  plt.show()
  
#number_of_inversions(roller_coasters,'Bobbejaanland')
plt.clf()

#plot pie chart
def pie_chart(roller_coasters):
  status_operating = roller_coasters.status.operating
  status_closed = roller_coasters.status.closed.definitely
# pie number one
  plt.pie(status_operating, labels = status, 
  autopct = '%0.1f%%')
  plt.axis('equal')

 # pie number two 
  plt.pie(status_closed, labels = status, 
  autopct = '%0.1f%%')
  plt.axis('equal')
  plt.show()
  
#pie_chart(roller_coasters)
#plt.clf()
  
# function to create scatter plot
def scatter_function(roller_coasters, park, name):
  scatter_park = roller_coaster.park
  scatter_name = roller_coaster.name
  plt.scatter(scatter_park, scatter_name)
  plt.title('Relationship between' + park + 'and' + name)
  plt.xlabel('Park')
  plt.ylabel('Roller Coaster Name')
  plt.show()

plt.clf()





