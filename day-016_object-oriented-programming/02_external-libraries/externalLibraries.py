from prettytable import PrettyTable

table = PrettyTable()
table.header = True
table.header_style = "upper"
table.add_column("FOOD", ["Oat", "Banana", "Spinach", "Almond"])
table.add_column("CATEGORY", ["grain",  "fruit", "vegetable", "legume"])
table.align = "c"
table.valign = "m"

print(table)
