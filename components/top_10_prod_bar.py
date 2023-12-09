import plotly.express as px
from dash import dcc, html, Input, Output,Dash,callback

def render(data):
    
    @callback(
        Output("top10_bar","children"),
        Input("year_drop_top_10", "value"),
        Input("month-dropdown-top-10","value"),
        Input ("top_10_country_drop", "value")       
    )
    def update_bar_chart(year, month, ctry):
        filtered_data = data.query("Year in @year and Month in @month and Country in @ctry")
        if filtered_data.shape[0] == 0:
            return html.Div("No data Selected", id="top10_bar")     
        top10 = filtered_data.nlargest(10,["Revenue"])
        fig = px.bar(top10, 
                    x = "Product",
                    y = "Revenue",
                    color = 'Country',
                    title= "Top Selling Products by Year and Month"
                    )
        fig.update_layout(yaxis_tickprefix = '$', yaxis_tickformat = ',.2f')
        return html.Div(dcc.Graph(figure=fig), id="top10_bar")
    return html.Div(id="top10_bar")