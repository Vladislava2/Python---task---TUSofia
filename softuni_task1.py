import math
l = float(input("Въведи число: ")) * 100
w = float(input("Въведи число: ")) * 100
columns = ( w - 100 ) / 70
ranks = ( l / 120 )
seats = round(( ranks * columns ) - 3)
print(seats)
# w = широчина
# l = височина
# 70 = дължината на едно работно място
# 100 = място за коридора
# 3 = местата, които се губят заради входната врата и катедрата
# round = закръгляване


