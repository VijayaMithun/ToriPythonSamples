from geopy.geocoders import Nominatim

'''
#Sample1
ge=Nominatim(user_agent="Viji") 
loc=ge.geocode(input("Enter pin code"))
print("Details of Zipcode : \n", loc.address)

#pip install geopy
#562117
#571401
#522007
''' 
'''
#Sample2
def details(coord): #userdefined parameter function
    ge=Nominatim(user_agent="Viji")
    loc=ge.reverse(coord,exactly_one=True)
    add=loc.raw['address'] # address - compulsory 
    cit=add.get('city','')
    stat=add.get('state','')
    cou=add.get('country','')
    return  cit,stat,cou

print(details("12.9524765,77.5414361"))
'''
'''
#Sample3
ge=Nominatim(user_agent="Viji") 
loc=ge.geocode(input("Enter State : "))
print(loc.address)
'''
'''
#Sample4 
ge=Nominatim(user_agent="Viji")
add1="Kolathur, Chennai"
loc=ge.geocode(add1)
print("Lati and Long")
print(loc.latitude,loc.longitude)
'''
'''
#Sample5 
ge=Nominatim(user_agent="Viji")
loc=ge.geocode("13.1241127 80.2046276")
print("Address , Lati and Long : ",loc)
'''
'''
#Sample6
from geopy import distance
c1=("13.1241127 80.2046276")
c2=("12.994112,80.1708668")

print("Distance : ")
print(distance.distance(c1,c2).km," kms")
''' 
    
