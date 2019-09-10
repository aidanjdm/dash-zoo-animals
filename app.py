import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Pick variables
tabtitle='forest'
myheading = 'Animals in the Forest'
myfavoritecolor='#1b5e20' # More colors are here: https://htmlcolorcodes.com/
x_list=['lemurs', 'pythons', 'birds of paradise']
y_list=[7, 4, 3]
mytitle='My favorite forest animals'
githublink='https://github.com/aidanjdm/dash-zoo-animals'

########### Set up the chart
mydata = [go.Bar(x=x_list,
                y=y_list,
                marker=dict(color=myfavoritecolor))]
mylayout = go.Layout(
    title = mytitle,
    xaxis = dict(title = 'Labels go here!'),
    yaxis = dict(title = 'Numbers go here!'))
myfigure = go.Figure(data=mydata, layout=mylayout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Display the chart
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(id='figure-1', figure=myfigure),
    html.A('Code on Github', href=githublink)])

########### Execute your code
if __name__ == '__main__':
    app.run_server()
