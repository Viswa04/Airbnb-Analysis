import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option("display.max_columns", None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

st.set_page_config(page_title="Airbnb Analysis", layout="wide")

df = pd.read_csv("C:/Users/user/Desktop/Guvi/Visual studio code/Airbnb/Airbnb.csv")

select = option_menu("", ["Home", "Data Exploration", "About"], orientation="horizontal",
                     icons=["house-fill", "bar-chart-fill", "info-square-fill"])

if select == "Home":

    image = Image.open("C:/Users/user/Desktop/Pics/airbnb.jpg")
    st.image(image)

    st.header(":red[Introduction]")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
            San Francisco home, and has since grown to over 4 million Hosts who have
            welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')


if select == "Data Exploration":
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["***PRICE ANALYSIS***", "***AVAILABILITY ANALYSIS***", "***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***", "***TOP CHARTS***"])

    with tab1:
        st.title(":red[**PRICE ANALYSIS**]")

        country = st.selectbox("Select the Country", df["country"].unique())
        col1,col2 = st.columns(2)

        with col1:

            df1 = df[df["country"] == country]
            df1.reset_index(drop=True, inplace=True)

            room = st.selectbox("Select the Room Type", df["Room_Type"].unique())

            df2 = df1[df1["Room_Type"] == room]
            df2.reset_index(drop=True, inplace=True)

            df_bar = pd.DataFrame(df2.groupby("Property_Type")[["Price", "Review_scores", "No_of_reviews"]].sum())
            df_bar.reset_index(inplace=True)

            fig_bar = px.bar(df_bar, x="Property_Type", y="Price", title="Price based on Property Type", width=500, height=500)
            st.plotly_chart(fig_bar)
        
        with col2:

            property = st.selectbox("Select the Property Type", df2["Property_Type"].unique())

            df3 = df2[df2["Property_Type"] == property]
            df3.reset_index(drop=True, inplace=True)

            df_pie = pd.DataFrame(df3.groupby("host_response_time")[["Price", "Bedrooms"]].sum())
            df_pie.reset_index(inplace=True)

            fig_pie = px.pie(df_pie, values="Price", names="host_response_time", title="Price based on Host Response Time", width=600, height=500)
            st.plotly_chart(fig_pie)
        
        col1,col2 = st.columns(2)
        with col1:

            hostresponse = st.selectbox("Select the Host Response Time", df3["host_response_time"].unique())

            df4 = df3[df3["host_response_time"] == hostresponse]
            df4.reset_index(drop=True, inplace=True)

            df_bar1 = pd.DataFrame(df4.groupby("Bed_Type")[["Min_Nights", "Max_nights", "Price"]].sum())
            df_bar1.reset_index(inplace=True)

            fig_bar1 = px.bar(df_bar1, x="Bed_Type", y=["Min_Nights", "Max_nights"], title="Minimum Nights & Maximum Nights", width=500, height=500)
            st.plotly_chart(fig_bar1)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_bar2 = pd.DataFrame(df4.groupby("Bed_Type")[["Bedrooms", "Beds", "Accommodates", "Price"]].sum())
            df_bar2.reset_index(inplace=True)

            fig_bar2 = px.bar(df_bar2, x="Bed_Type", y=["Bedrooms", "Beds", "Accommodates"], title= "Beds, Bedrooms & Accomodates", width=600, height=500)
            st.plotly_chart(fig_bar2)
    
    with tab2:

        df_a = pd.read_csv("C:/Users/user/Desktop/Guvi/Visual studio code/Airbnb/Airbnb.csv")

        st.title(":red[**AVAILABILITY ANALYSIS**]")
        country_a = st.selectbox("Select the Country_a", df_a["country"].unique())

        df1_a = df_a[df_a["country"] == country_a]
        df1_a.reset_index(drop=True, inplace=True)

        property_a = st.selectbox("Select the Property Type_a", df1_a["Property_Type"].unique())
        col1,col2 = st.columns(2)

        with col1:

            df2_a = df1_a[df1_a["Property_Type"] == property_a]
            df2_a.reset_index(drop=True, inplace=True)

            df_a_sun = px.sunburst(df2_a, path=["Room_Type", "Bed_Type", "is_location_exact"], values="availability_30", width=500, height=500, title="Availability_30", color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sun)
        
        with col2:

            df_a_sun_60 = px.sunburst(df2_a, path=["Room_Type", "Bed_Type", "is_location_exact"], values="availability_60", width=500, height=500, title= "Availability_60", color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sun_60)
        
        col1,col2 = st.columns(2)

        with col1:

            df_a_sun_90 = px.sunburst(df2_a, path=["Room_Type", "Bed_Type", "is_location_exact"], values="availability_90", width=500, height=500, title= "Availability_90", color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sun_90)
        
        with col2:

            df_a_sun_365 = px.sunburst(df2_a, path=["Room_Type", "Bed_Type", "is_location_exact"], values="availability_365", width=500, height=500, title= "Availability_365", color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(df_a_sun_365)
        
        roomtype_a = st.selectbox("Select the Room Type_a", df2_a["Room_Type"].unique())

        df3_a = df2_a[df2_a["Room_Type"] == roomtype_a]

        df_bar_a = pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30", "availability_60", "availability_90", "availability_365", "Price"]].sum())
        df_bar_a.reset_index(inplace=True)

        fig_bar_a = px.bar(df_bar_a, x="host_response_time", y=["availability_30", "availability_60", "availability_90", "availability_365"], title = "AVAILABILITY BASED ON HOST RESPONSE TIME", hover_data="Price", width=1200)
        st.plotly_chart(fig_bar_a)
    
    with tab3:

        st.title(":red[LOCATION ANALYSIS]")

        df_l = pd.read_csv("C:/Users/user/Desktop/Guvi/Visual studio code/Airbnb/Airbnb.csv")

        country_l = st.selectbox("Select the Country_l", df_l["country"].unique())

        df1_l = df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop=True, inplace=True)

        property_l = st.selectbox("Select the Property Type_l", df1_l["Property_Type"].unique())

        df2_l = df1_l[df1_l["Property_Type"] == property_l]
        df2_l.reset_index(drop=True, inplace=True)

        def select_df(val):
            if val == str(df2_l["Price"].min())+' '+str("to")+' '+str(differ_max_min*0.30 + df2_l["Price"].min())+' '+str("(30% of Value)"):

                df_val_30 = df2_l[df2_l["Price"] <= differ_max_min*0.30 + df2_l["Price"].min()]
                df_val_30.reset_index(drop=True, inplace=True)
                return df_val_30
            
            elif val == str(differ_max_min*0.30 + df2_l["Price"].min())+' '+str("to")+' '+str(differ_max_min*0.60 + df2_l["Price"].min())+' '+str("(30% to 60% of Value)"):

                df_val_60 = df2_l[df2_l["Price"] >= differ_max_min*0.30 + df2_l["Price"].min()]
                df_val_60_1 = df_val_60[df_val_60["Price"] <= differ_max_min*0.60 + df2_l["Price"].min()]
                df_val_60_1.reset_index(drop=True, inplace=True)
                return df_val_60_1
            
            elif val == str(differ_max_min*0.60 + df2_l["Price"].min())+' '+str("to")+' '+str(df2_l["Price"].max())+' '+str("(60% to 100% of Value)"):

                df_val_100 = df2_l[df2_l["Price"] >= differ_max_min*0.60 + df2_l["Price"].min()]
                df_val_100.reset_index(drop=True, inplace=True)
                return df_val_100
        
        differ_max_min = df2_l["Price"].max()-df2_l["Price"].min()

        val = st.radio("Select the Price Range",[str(df2_l["Price"].min())+' '+str("to")+' '+str(differ_max_min*0.30 + df2_l["Price"].min())+' '+str("(30% of Value)"),
                                                 str(differ_max_min*0.30 + df2_l["Price"].min())+' '+str("to")+' '+str(differ_max_min*0.60 + df2_l["Price"].min())+' '+str("(30% to 60% of Value)"),
                                                 str(differ_max_min*0.60 + df2_l["Price"].min())+' '+str("to")+' '+str(df2_l["Price"].max())+' '+str("(60% to 100% of Value)")])
        
        df_val = select_df(val)

        df_val_gr = pd.DataFrame(df_val.groupby("Accommodates")[["Cleaning_Fee","Bedrooms","Beds","Extra_People"]].sum())
        df_val_gr.reset_index(inplace=True)

        fig_1 = px.bar(df_val_gr, x="Accommodates", y=["Cleaning_Fee","Bedrooms","Beds"], title="ACCOMODATES", hover_data="Extra_People", color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1200)
        st.plotly_chart(fig_1)

        roomtype_l = st.selectbox("Select the Room Type_l", df_val["Room_Type"].unique())

        df_val_room = df_val[df_val["Room_Type"] == roomtype_l]

        fig_2 = px.bar(df_val_room, x=["street","host_location","host_neighbourhood"], y="market", title="MARKET", hover_data=["Name","host_name","market"], color_discrete_sequence=px.colors.sequential.Greens_r, width=1200)
        st.plotly_chart(fig_2)

        fig_3 = px.bar(df_val_room, x="government_area", y=["host_is_superhost","host_neighbourhood", "Cancellation_Policy"], title="GOVERNMENT AREA", hover_data=["Guests_Included","location_type"], color_discrete_sequence=px.colors.sequential.Aggrnyl_r, width=1200)
        st.plotly_chart(fig_3)
    
    with tab4:

        st.title(":red[GEOSPATIAL VISUALIZATION]")

        st.write("")
        st.write("")
        st.write("")

        fig_map = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="Price", size="Accommodates", color_continuous_scale="rainbow",hover_name="Name",mapbox_style="carto-positron", zoom=1)
        fig_map.update_layout(height=800, width=1200, title="Geospatial Visualization")
        st.plotly_chart(fig_map)
    
    with tab5:

        df_t = pd.read_csv("C:/Users/user/Desktop/Guvi/Visual studio code/Airbnb/Airbnb.csv")

        country_t = st.selectbox("Select the Country_t", df_t["country"].unique())

        df1_t = df_t[df_t["country"] == country_t]
        df1_t.reset_index(drop=True, inplace=True)

        property_t = st.selectbox("Select the Property Type_t", df1_t["Property_Type"].unique())

        df2_t = df1_t[df1_t["Property_Type"] == property_t]
        df2_t.reset_index(drop=True, inplace=True)

        df_price = pd.DataFrame(df2_t.groupby("host_neighbourhood")["Price"].agg(["sum","mean"]))
        df_price.reset_index(inplace=True)
        df_price.columns = ["host_neighbourhood", "Total_Price", "Average_Price"]

        df1_price = pd.DataFrame(df2_t.groupby("host_location")["Price"].agg(["sum","mean"]))
        df1_price.reset_index(inplace=True)
        df1_price.columns = ["host_location", "Total_Price", "Average_Price"]

        col1,col2 = st.columns(2)

        with col1:

            fig1_price = px.bar(df_price, y="Average_Price", x="host_neighbourhood", title = "Average Price based on Host Neighbourhood", width=500, height=500)
            st.plotly_chart(fig1_price)
        
        with col2:

            fig2_price = px.bar(df_price, y="Total_Price", x="host_neighbourhood", title= "Total Price based on Host Neighbourhood", width=500, height=500)
            st.plotly_chart(fig2_price)
        
        col1,col2 = st.columns(2)

        with col1:

            fig3_price = px.bar(df1_price, y="Average_Price", x="host_location", title="Average Price based on Host Location", width=500, height=500, color_discrete_sequence=px.colors.sequential.Rainbow_r)
            st.plotly_chart(fig3_price)
        
        with col2:

            fig4_price = px.bar(df1_price, y="Total_Price", x="host_location", title="Total Price based on Host Location", width=500, height=500, color_discrete_sequence=px.colors.sequential.Rainbow_r)
            st.plotly_chart(fig4_price)
        
        roomtype_t = st.selectbox("Select the Room Type_t", df2_t["Room_Type"].unique())

        df3_t = df2_t[df2_t["Room_Type"] == roomtype_t]
        df3_sort = df3_t.sort_values(by = "Price")
        df3_sort.reset_index(drop=True, inplace=True)

        df3_top = df3_sort.head(100)

        fig1_top = px.bar(df3_top, x="Name", y="Price", color_continuous_scale= "rainbow", title="Min Nights, Max Nights & Accomodates", width=1200, height=500, hover_data=["Min_Nights", "Max_nights", "Accommodates"])
        st.plotly_chart(fig1_top)

        fig2_top = px.bar(df3_top, x="Name", y="Price", color_continuous_scale= "greens", title = "Beds, Bedrooms, Bed Type & Accomodates", width=1200, height=500, hover_data=["Accommodates", "Bed_Type", "Beds", "Bedrooms"])
        st.plotly_chart(fig2_top)

if select == "About":

    st.header(":red[Project Title :]")
    st.subheader("***AIRBNB ANALYSIS***")

    st.header(":red[Skill take away from Project:]")
    st.write("***Python scripting***")
    st.write("***Data Preprocessing***")
    st.write("***Data Visualization***")
    st.write("***EDA***")
    st.write("***Streamlit***")
    st.write("***MongoDB***")

    st.header(":red[Approach:]")
    
    st.subheader(":orange[1.MongoDB connection and Data Retrieval:]")
    st.write('''***Connected to the MongoDB Atlas database and retrieved data from Airbnb dataset for analysis.***''')

    st.subheader(":orange[2.Data Cleaning and Preparation:]")
    st.write('''***Airbnb dataset is cleaned and handled the missing values, removed duplicates and transformed datatype as necessary***''')

    st.subheader(":orange[3.Exploratory Data Analysis (EDA):]")
    st.write('''***EDA is done to understand the distribution and patterns in the data. Explored relationship between
             variables and identify potential insights.***''')
    
    st.subheader(":orange[4.Data Visualization:]")
    st.write('''***Created visualizations to represent key metrics and trends. Used Matplot, Seaborn and plotly
             to visualize the charts, graphs and maps.***''')
    
    st.subheader(":orange[5.Geospatial Visualization:]")
    st.write('''***Developed Streamlit application that utilizes the Geospatial data from Airbnb dataset and created
             interactive maps to visualize the distribution of listings across different locations, allowing users to 
             explore prices, ratings, and other relevant factors.***''')






        







 





