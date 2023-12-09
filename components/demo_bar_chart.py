import plotly.express as px
from dash import dcc, html, Input, Output,Dash,callback

def render(data):
    @callback(
        Output("demo_bar_chart","children"),   
        Input ("demo_country_drop","value")        
    )
    def update_demo_bar_chart(country):
        cust_age_view = data.query("Country in @country")    
        if cust_age_view.shape[0] == 0:
            return html.Div("No data Selected", id="demo_bar_chart")
        fig = px.bar(cust_age_view, 
                     x="Customer_Age",
                     y="Order_Count",
                     color="Customer_Gender",
                     title= "Order Count by Gender, Age and Country"
                    )
        return html.Div(dcc.Graph(figure=fig), id="demo_bar_chart")
    return html.Div(id="demo_bar_chart")