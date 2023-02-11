import pandas

data = pandas.read_csv("central_park_squirrel_data.csv")
color_list = ["Gray", "Cinnamon", "Black"]
g_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
r_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
b_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [g_squirrels, r_squirrels, b_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")