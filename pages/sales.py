import dash
from dash import Dash, html,dcc, html, callback, Output, Input
import pandas
import plotly.express as px
import dash_bootstrap_components as dbc
import util
import os


# dash.register_page(__name__, path='/sales_dashboard', name='Sales Dashboard') 
PATH = os.path.join(os.getcwd(), "sales_data.csv")
data = util.get_data(PATH)
line_chart_sales_data = util.get_rev_line_data(PATH)
top_10_bar_chart_data = util.get_top_10_items(PATH)
# app = Dash(external_stylesheets=[dbc.themes.SPACELAB])

from components import ( 
                        year_drop, 
                        cat_drop,
                        subcat_drop,
                        pie_chart,   
                        rev_line_chart,
                        rev_sales_slider,
                        top_10_item_year_drop,
                        top_10_item_month_drop,
                        top_10_item_country_drop,
                        top_10_prod_bar             
)

dash.register_page(__name__, path='/', name='Revenue Dashboard') # '/' is home page
layout = html.Div(
    [
        dbc.Row(dbc.Col(html.H1("Revenue Dashboard"))),
            dbc.Row(
                [
                dbc.Col(
                    [
                    year_drop.render(data),               
                    cat_drop.render(data),
                    subcat_drop.render(data),    
                    pie_chart.render(data)                 
                    ],width=4), 

                    dbc.Col(

                        [
                            top_10_item_country_drop.render(top_10_bar_chart_data),
                            top_10_item_year_drop.render(top_10_bar_chart_data),
                            top_10_item_month_drop.render(top_10_bar_chart_data),                           
                            top_10_prod_bar.render(top_10_bar_chart_data)
                        ],width=4
                    ),

                     dbc.Col(
                        [
                        rev_sales_slider.render(line_chart_sales_data),
                        rev_line_chart.render(line_chart_sales_data)
                        ],width=4

                    ),
                                      
                ] 
            )
           
    ]
)