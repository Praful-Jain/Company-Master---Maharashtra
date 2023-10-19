import csv
import matplotlib.pyplot as plt
from datetime import datetime

main_file = r'Maharashtra.csv'
pin_file = r'pincode.csv'

pincode_district = {}

""" Here we will open and traverse the file containing pincode-district data and will store
 that data into a dictionary.So, that we don't need to traverse this file again and again 
 to find the district name. """
with open(pin_file) as file:
    pin_reader = csv.DictReader(file)

    for row in pin_reader:    
        pincode = row['Pin Code']
        pincode_district[pincode]=row['District']


with open(main_file,encoding='ISO-8859-1') as file:
    csv_reader = csv.DictReader(file)      # extract the main_file
    
    district_count = {}
    
    for row in csv_reader:
        date = row['DATE_OF_REGISTRATION']          #fetch date string from csv file
        
        try:
            date_obj = datetime.strptime(date,'%d-%m-%y')   # Convert the string to a datetime object
            year = date_obj.year                            #Extract year from datetime object
            if year>2021:
                year-=100
        except ValueError:
            pass
        
        # Now if year=2015 do further computation
        if year==2015:
            # to overcome 'IndexError' while slicing ... we used try-except block
            try: 
                address = row['Registered_Office_Address']
                # Slice 'address' from index 'len(address)-6' to end to get pincode
                pincode = address[len(address)-6:]      
                
                """ if this 'pincode' will be present in 'pincode_district' dictionary, we will
                  fetch it's district name and will increment it's count in 'district_count' """
                try:
                    district = pincode_district[pincode]
                    if district not in district_count:
                        district_count[district]=0
                    district_count[district]+=1
                except KeyError:
                    pass
            except IndexError:
                pass
            
for i in district_count:
    print(i," : ",district_count[i])
    
plt.bar(district_count.keys(),district_count.values())

plt.xlabel('District.')
plt.xticks(rotation=90)
plt.ylabel('No. of companies registered from a district in 2015.')
plt.title('Company registration in the year 2015 by the district.')
plt.show()