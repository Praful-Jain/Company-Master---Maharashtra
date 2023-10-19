import csv
import matplotlib.pyplot as plt
from datetime import datetime

csv_file = r'Maharashtra.csv'

with open(csv_file,encoding='ISO-8859-1') as file:
    csv_reader = csv.DictReader(file)
    
    business_activities = {}
    x=set()
    for row in csv_reader:
        try:
            date=row['DATE_OF_REGISTRATION']
            date_obj = datetime.strptime(date,'%d-%m-%y')
            year = date_obj.year
            
            
            if year>=2012 and year<=2021:
                if year not in business_activities:
                    business_activities[year]={}
                
                business = row['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']
                if business not in business_activities[year]:
                        business_activities[year][business]=0
                business_activities[year][business]+=1    
        except ValueError:
            pass
        
        
business_activities = dict(sorted(business_activities.items()))
for year in business_activities:
    business_activities[year] = dict(sorted(business_activities[year].items(),key = lambda x : x[1],reverse=True))
 
# final dictionary will store top-5 business _activities between 2012-2021
final={}
for year in business_activities:
    i=0
    final[year]={}
    for business in business_activities[year]: 
        final[year][business]=business_activities[year][business]
        i+=1    
        if(i==5):    break
        
        
for year in final:
    print(year , "-----")
    print(final[year])
    print()
    
        
 #Prepare data for the plot
labels = list(final.keys())
data = {business: [final[year].get(business, 0) for year in final] for business in final[labels[0]]}

# Plotting the grouped bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.15
index = range(len(labels))

for i, business in enumerate(data):
    ax.bar([x + bar_width * i for x in index], data[business], bar_width, label=business)

ax.set_xlabel('Years')
ax.set_ylabel('Frequency')
ax.set_title('Top 5 Business Activities Over the Years in Maharashtra')
ax.set_xticks([x + bar_width * 2 for x in index])
ax.set_xticklabels(labels)
ax.legend()

plt.show()

