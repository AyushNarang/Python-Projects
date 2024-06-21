from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

table = ColorTable(theme=Themes.OCEAN)

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
                ["Pikachu", "Electric"],
                ["Squirtle", "Water"],
                ["Charmander", "Fire"]
    ]
)

table.border = True
print(table)