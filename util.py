import pandas as pd 

def get_data(PATH):
    df = pd.read_csv(PATH) 
    df["Date"] = pd.to_datetime(df["Date"])
    df['Year'] = df['Year'].astype(str)
    # print (df.info())
    return df

def get_demo_data (PATH):
    df = pd.read_csv(PATH) 
    custOrders = df.groupby(['Customer_Age', 'Country','Customer_Gender'])['Revenue'].count().reset_index()
    custOrders.rename(columns={"Revenue":"Order_Count"}, inplace=True)
    return custOrders

def get_demo_data_global (PATH):
    df = pd.read_csv(PATH) 
    custOrdersGlobal = df.groupby(['Customer_Age','Customer_Gender'])[['Revenue']].count().reset_index()
    custOrdersGlobal.rename(columns={"Revenue":"Order_Count"}, inplace=True)
    return custOrdersGlobal

def get_rev_line_data (PATH):
    df = pd.read_csv(PATH) 
    rev_by_year_ctry = df.groupby(["Year","Country"])[["Revenue"]].sum().reset_index()
    return rev_by_year_ctry

def get_rev_item_data (PATH):
    df = pd.read_csv(PATH) 
    rev_item_count_df= df.groupby(["Product", "Year","Month","Country"])[["Revenue", "Order_Quantity"]].sum().reset_index()
    return rev_item_count_df

def get_top_10_items (PATH):
    df = pd.read_csv(PATH) 
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    rev_item_count_df= df.groupby(["Product","Country", "Year","Month"])[["Revenue"]].sum().reset_index().copy()
    return rev_item_count_df

# df = pd.read_csv("sales_data.csv") 
# rev_by_year_ctry = df.groupby(["Year","Country"])[["Revenue"]].sum().reset_index()
# rev_by_year_ctry.to_csv("seeRev.csv")







