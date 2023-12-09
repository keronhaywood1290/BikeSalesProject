import plotly.express as px
from dash import html, dcc, Output, Input,Dash, callback

def render(data):
    @callback(
        Output("rev_line_chart","children"),
        Input("select_year_sldr","value")     
    )
    def update_line_chart(years):
        filtered_data = data.query("Year in @years")
        if filtered_data.shape[0] == 0:
            print("True")
            return html.Div("No data Selected", id="rev_line_chart")
        fig = px.line(filtered_data, 
                      x="Year",
                      y="Revenue",
                      color="Country",
                      title= "Revenue by Country"
                    )
        fig.update_layout(
            # autosize=False,
            yaxis_tickprefix = '$',
            yaxis_tickformat = ',.2f'
        )
        return html.Div(dcc.Graph(figure=fig), id="rev_line_chart")
    return html.Div(id="rev_line_chart")