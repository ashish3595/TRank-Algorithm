import MySQLdb
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import decimal
import json as simplejson

class DecimalJSONEncoder(simplejson.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)


db = MySQLdb.connect("localhost", "root", "123xyz", "twitterDB")
cursor = db.cursor()

x1 = []
y1 = []
y2 = []

sql = "select scr_name, avg(fav_count), avg(fav_inf) from htag5 group by scr_name;"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    x1.append(row[0])
    y1.append(simplejson.dumps(decimal.Decimal(row[1]), cls=DecimalJSONEncoder))
    y2.append(simplejson.dumps(decimal.Decimal(row[2]), cls=DecimalJSONEncoder))

data1 = [
    go.Bar(
        x=x1,
        y=y1,
        marker=dict(
            color='green'
            ),
        opacity=0.6
    )
]
data2 = [
    go.Bar(
        x=x1,
        y=y2,
        marker=dict(
            color='black'
            ),
        opacity=0.6
    )
]

layout1 = go.Layout(
    title='Mapping Average Favourite Count For A User For Hashtag #Meditation',
    xaxis=dict(
        title='User Screen Name'
    ),
    yaxis=dict(
        title='Average Favourite Count of User'
    )
)

layout2 = go.Layout(
    title='Mapping Average Favourite Influence For A User For Hashtag #Meditation',
    xaxis=dict(
        title='User Screen Name'
    ),
    yaxis=dict(
        title='Average Favourite Influence of User'
    )
)

fig1 = go.Figure(data=data1, layout=layout1)
fig2 = go.Figure(data=data2, layout=layout2)

py.plot(fig1, filename='htag5_fav_count', validate=False)
py.plot(fig2, filename='htag5_fav_inf', validate=False)

del x1[:]
del y1[:]
del y2[:]

db.close()