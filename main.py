''' A column salary chart with minimum and maximum values.
This example shows the capability of exporting a csv file from ColumnDataSource.

'''
from os.path import dirname, join

import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import (Button, ColumnDataSource, CustomJS, DataTable,
                          NumberFormatter, RangeSlider, TableColumn)


global df

def load_data():
    global df
    df = pd.read_csv(join(dirname(__file__), 'ookFiles300K.csv'))
    return df

# def load_new_data():
#     global df2
#     df2 = pd.read_csv(join(dirname(__file__), 'largeFiles600K_update.csv'))
#     return df2

source = ColumnDataSource(data=load_data())
columns = [
    TableColumn(field="id", title="ID"),
    TableColumn(field="firstname", title="First Name"),
    TableColumn(field="lastname", title="Last Name"),
    TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
    TableColumn(field="years_experience", title="Experience (years)"),
    TableColumn(field="birthday", title="Birthday"),
    TableColumn(field="startdate", title="Start Date"),
    TableColumn(field="email", title="Email"),
    TableColumn(field="country", title="Country")
]

data_table = DataTable(source=source, columns=columns, width=1000)


# Second Table
source2 = ColumnDataSource()
columns2 = [
    TableColumn(field="id", title="ID"),
    TableColumn(field="firstname", title="First Name"),
    TableColumn(field="lastname", title="Last Name"),
    TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
    TableColumn(field="years_experience", title="Experience (years)"),
    TableColumn(field="birthday", title="Birthday"),
    TableColumn(field="startdate", title="Start Date"),
    TableColumn(field="email", title="Email"),
    TableColumn(field="country", title="Country"),
    TableColumn(field='New_Column', title="New Column")

]
source2 = ColumnDataSource(data=dict(id=[], firstname=[], lastname=[], salary=[], years_experience=[],birthday=[], startdate=[], email=[], country=[], New_Column=[]))
data_table2 = DataTable(source=source2, columns=columns2, width=1000)


def update_scen_tab():
    global df
    df['New_Column']=0   # here can be a long lambda function process
    new_data = dict(df)
#    del new_data["index"]
    source2.stream(new_data)
    return




button = Button(label="Calculate", button_type="success")
button.on_click(update_scen_tab)


layout = column(data_table, button, data_table2)
curdoc().add_root(layout)
curdoc().title = "Append and reload CSV"


