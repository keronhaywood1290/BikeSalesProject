import plotly.express as px
from dash import dcc, html, Input, Output,Dash,callback

def render(data):
    @callback(
        Output("pie-chart","children"),      
        Input("year_drop","value"),
        Input("cat_drop", "value"),
        Input ("subcat_drop", "value")      
    )
    def update_pie_chart(years, cat, subcat):
        filtered_data = data.query("Year in @years and Product_Category in @cat and Sub_Category in @subcat")
        if filtered_data.shape[0] == 0:
            return html.Div("No data Selected", id="pie-chart")
        fig = px.pie(filtered_data, 
                     values="Revenue",
                     names="Sub_Category",
                     hole = 0.4,
                     title= "Revenue by Year and Category"
                    )
        fig.update_layout(
            yaxis_tickprefix = '$',
            yaxis_tickformat = ',.2f'
        )
        return html.Div(dcc.Graph(figure=fig), id="pie-chart")
    return html.Div(id="pie-chart")