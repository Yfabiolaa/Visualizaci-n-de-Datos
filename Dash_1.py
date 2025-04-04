# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

"""# App layout
app.layout = [
    html.H1(children='My First App with Data, Graph, and Controls'),# H1 header
    html.Hr(), # Separador
    
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
]

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)"""

# App layout
app.layout = html.Div([
    html.H1(
        children='Interactive Dashboard: Data, Graphs, and Controls',
        style={'textAlign': 'center', 'color': '#333', 'fontFamily': 'Arial, sans-serif'}
    ),  # H1 header
    html.Hr(),  # Separator

    # Controls section
    html.Div([
        html.Label('Select a Metric:', style={'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=[
                {'label': 'Population', 'value': 'pop'},
                {'label': 'Life Expectancy', 'value': 'lifeExp'},
                {'label': 'GDP per Capita', 'value': 'gdpPercap'}
            ],
            value='lifeExp',
            id='controls-and-radio-item',
            style={'marginBottom': '20px'}
        )
    ], style={'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'marginBottom': '20px'}),

    # Data table
    html.Div([
        html.H4('Data Table', style={'textAlign': 'center'}),
        dash_table.DataTable(
            data=df.to_dict('records'),
            page_size=6,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left', 'padding': '5px'},
            style_header={'backgroundColor': '#f4f4f4', 'fontWeight': 'bold'}
        )
    ], style={'marginBottom': '20px'}),

    # Graphs section
    html.Div([
        html.H4('Histogram', style={'textAlign': 'center'}),
        dcc.Graph(figure={}, id='controls-and-graph'),
        html.H4('Scatter Plot', style={'textAlign': 'center', 'marginTop': '20px'}),
        dcc.Graph(figure={}, id='scatter-plot')
    ])
], style={'padding': '20px', 'fontFamily': 'Arial, sans-serif'})

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Output(component_id='scatter-plot', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graphs(col_chosen):
    # Histogram
    fig_hist = px.histogram(df, x='continent', y=col_chosen, histfunc='avg', title=f'Average {col_chosen} by Continent')
    fig_hist.update_layout(title_x=0.5)

    # Scatter plot
    fig_scatter = px.scatter(df, x='gdpPercap', y=col_chosen, color='continent', title=f'{col_chosen} vs GDP per Capita')
    fig_scatter.update_layout(title_x=0.5)

    return fig_hist, fig_scatter

# Run the app
if __name__ == '__main__':
    app.run(debug=True)