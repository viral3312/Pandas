         # Dependencies and Setup
import pandas as pd
import numpy as np
# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"
# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

               #Player count
#keep only "SN"
sn_keep=purchase_data["SN"]
sn_df=pd.DataFrame(sn_keep)
#Identify unique values 
unique=sn_df["SN"].unique()
#Count total number of players
total_players=len(sn_df["SN"].value_counts())
#convert into dataframe
player_count=pd.DataFrame({"Total Players":total_players},index=[0])
player_count


            #Purchasing analysis
#Calculation of data series
unique_items=len(purchase_data["Item ID"].unique())
Average_price= purchase_data["Price"].mean()
#count "Item Name"
Number_purchase=len(purchase_data["Item Name"])
#Calculate totalrevenue
Total_revenue=purchase_data["Price"].sum()
#Create a datafrome for above variables
purchase_analysis=pd.DataFrame({"Number of Unique items":[unique_items],"Average Price":[f"${Average_price:.2f}"],
                                "Number of Purchases":[Number_purchase],"Total Revenue":[f"${Total_revenue}"]
                               })
#print purchase analysis
purchase_analysis

                #Gender Demographics
#create dataframe and remove duplicates
abc=["SN","Gender"]
genderDF=purchase_data[abc]
#Remove duplicates
gender_df=genderDF.drop_duplicates()
#Total counts
total_count=len(gender_df["SN"].value_counts())
#count values
gender_count=gender_df["Gender"].value_counts()
#calculate percent for gender
gender_percent=((gender_count/total_count)*100).round(2)
#convert into dataframe
gender_demographics=pd.DataFrame({
    "Total Count":gender_count,
     "Percentage of Players":gender_percent
    })
#print gender demographic
gender_demographics

        
        #purchasing analysis
#groupby gender
gender_group=purchase_data.groupby("Gender")

#basic calculation
average_price=gender_group["Price"].mean()
average_price=average_price.round(2)
purchase_count=gender_group["Item Name"].count()
total_purchase=gender_group["Price"].sum()
average_total_purchase=(total_purchase/gender_count).round(2)
#Create dataframe
purchase_analysis=pd.DataFrame({
    "Purchase Count":purchase_count,"Average Purchase Price":average_price,
    "Total Purchase Value":total_purchase,"Avg Total Purchase per Person":average_total_purchase
})
#Change format
purchase_analysis_final=purchase_analysis.style.format({"Average Purchase Price":"${:.2f}",
                                                        "Avg Total Purchase per Person":"${:.2f}"
                                                      })
#Final output
purchase_analysis_final


        #Age demographics
#create dataframe and remove duplicates
xyz=["Age","SN"]
age_df=purchase_data[xyz]
age_demo_df=age_df.drop_duplicates()

#Create bins
age_bin=[0,9.99,14,19,24,29,34,39,999]
age_group= ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

#create table
age_demo_df["Age Ranges"]=pd.cut(age_demo_df["Age"],age_bin, labels=age_group)
age_demo_count=age_demo_df.groupby(["Age Ranges"])
#count values
SN_total_count=age_demo_count["SN"].count()
age_percent=(SN_total_count/total_count)*100
age_percent=age_percent.round(2)
age_percent

#create dataframe
age_tbl=pd.DataFrame({
    "Total Count":SN_total_count, "Percentage of Players":age_percent
})
#print final output
age_tbl



            #Purchasing analysis
#Create bins
age_bin=[0,9.99,14,19,24,29,34,39,999]
age_group= ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]
#group by agegroup
purchase_data["Age Ranges"]=pd.cut(purchase_data["Age"],age_bin, labels=age_group)
purchase_ana_df=purchase_data.groupby(["Age Ranges"])
#basic calculation
age_purchase_count=purchase_ana_df["Item Name"].count()
age_average_price=purchase_ana_df["Price"].mean()
age_total_purchase=purchase_ana_df["Price"].sum()
age_avg_total_purchase_person=(age_total_purchase/SN_total_count).round(2)
#Create dataframe
age_purchase_ana=pd.DataFrame({
    "Purchase Count":age_purchase_count,
    "Average Purchase Price":age_average_price,
    "Total Purchase Value":age_total_purchase,
    "Avg Total Purchase per Person":age_avg_total_purchase_person
})
#change format
final_age_purchase_ana=age_purchase_ana.style.format({"Average Purchase Price":"${:.2f}",
                                                        "Total Purchase Value":"${:.2f}",
                                                        "Avg Total Purchase per Person":"${:.2f}"
                                                      })
#final output
final_age_purchase_ana


            #Top Spendars
#Basic calculation
spendar_purchase_count=purchase_data.groupby("SN")["Price"].count()
spendar_average_price=purchase_data.groupby("SN")["Price"].mean().round(2)
spendar_total_purchase=purchase_data.groupby("SN")["Price"].sum()
#Create dataframe
spendar_df=pd.DataFrame({
    "Purchase Count":spendar_purchase_count,
    "Average Purchase Price":spendar_average_price,
    "Total Purchase Value":spendar_total_purchase
})
#format

#sorting
spendar_sort=spendar_df.sort_values("Total Purchase Value",ascending=False )
# top five values
spendar_final=spendar_sort.head(5)
#Format the dataframe
spendar_final["Average Purchase Price"]=spendar_final["Average Purchase Price"].map("${:.2f}".format)
spendar_final["Total Purchase Value"]=spendar_final["Total Purchase Value"].map("${:.2f}".format)
#Final output
spendar_final


            #most popular items
#Retrive columns
popular_df=pd.DataFrame(purchase_data.groupby(["Item ID","Item Name"])["Purchase ID"].count())
popular_df.head()

# Perform basic calculation
popular_df["Item Price"]=purchase_data.groupby(["Item ID","Item Name"])["Price"].mean()
popular_df["Total Purchase Value"]=purchase_data.groupby(["Item ID","Item Name"])["Price"].sum()
popular_df=popular_df.rename(columns={"Purchase ID": "Purchase Count"})

#Format
popular_df["Item Price"]=popular_df["Item Price"].map('${:,.2f}'.format)
popular_df["Total Purchase Value"]=popular_df["Total Purchase Value"].map('${:,.2f}'.format)
# sorting
popular_sort=popular_df.sort_values("Purchase Count", ascending=False)


#final output

popular_sort_final=popular_sort.head()
popular_sort_final


            #Most profitable items
most_profitable=popular_sort.sort_values("Total Purchase Value", ascending=False)
most_profitable.head()