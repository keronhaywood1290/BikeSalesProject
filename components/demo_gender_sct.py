import plotly.express as px
from dash import dcc, html, Input, Output,Dash,callback

def render (data):
    fig=px.scatter(data, x="Customer_Age",
                         y="Order_Count", 
                         color = "Customer_Gender", 
                         title="Global Order Count by Gender and Age"
                         )
    return html.Div(dcc.Graph(figure=fig), id="demo_scatter_chart")