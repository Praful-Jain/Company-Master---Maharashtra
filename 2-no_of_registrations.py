import csv
import matplotlib.pyplot as plt
from datetime import datetime

csv_file = r'Maharashtra.csv'

with open(csv_file, encoding="latin-1") as file:
    csv_reader = csv.DictReader(file)
    
    # Dictionary to store number of registrations per year
    reg_year={}
    for row in csv_reader:
        date = row['DATE_OF_REGISTRATION']      #fetch date string from csv file
        
        try:
            date_obj = datetime.strptime(date,'%d-%m-%y')   # Convert the string to a datetime object
            year = date_obj.year                            #Extract the year from the datetime object
            if year>2021:
                year-=100
        except ValueError:
            pass
        
        if year not in reg_year:
            reg_year[year]=0
        reg_year[year]+=1
        
        
reg_year=dict(sorted(reg_year.items()))

for i in reg_year:
    print(i," : ",reg_year[i])

# Plotting the bar graph
plt.bar(reg_year.keys(),reg_year.values())
plt.xlabel('Year')
plt.ylabel('No. of registrations')
plt.title('Bar Plot of company registration by year')
plt.show()