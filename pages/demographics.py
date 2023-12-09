import dash
from dash import Dash, html
from dash import dcc, html, callback, Output, Input
import pandas
import plotly.express as px
import dash_bootstrap_components as dbc
import util
import os


PATH = os.path.join(os.getcwd(), "sales_data.csv")
data = util.get_demo_data(PATH)
sct_data=util.get_demo_data_global(PATH)


from components import ( 
                        demo_bar_chart_drop,
                        demo_bar_chart,
                        demo_gender_sct                
)
dash.register_page(__name__, name='Demographic Dashboard')

layout= html.Div(
        [
            dbc.Row(dbc.Col(html.H1("Demographic Dashboard"))),

            dbc.Row (
                [
                    dbc.Col(
                        [
                          demo_bar_chart_drop.render(data),
                        ],width=6

                    )
                ]

            ),

            dbc.Row(
                [
                dbc.Col(demo_bar_chart.render(data),width=6),
                dbc.Col(demo_gender_sct.render(sct_data),width=6)
                ]
            )
            
            
        ]

)



