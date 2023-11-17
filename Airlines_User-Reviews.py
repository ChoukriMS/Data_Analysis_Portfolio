import pandas as pd
reviews = pd.read_csv("Airlines_User-Reviews_Raw.csv")
reviews.info()

##
print(reviews.count()-reviews.drop_duplicates().count())
#Duplicate are not usefull in our case 
reviews = reviews.drop_duplicates()
