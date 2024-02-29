import subprocess

numberplate = "".join(input("Enter numberplate: ").split()).upper()

address = f"https://ww1.vehicleinformation.uk/preview5?vrm={numberplate}&veh=yes"

data = str(subprocess.check_output(['curl', address]))

removedtop = data.split(numberplate)[1]

splitted = removedtop.split("<strong class=\"text-uppercase\">")

make = splitted[1].split("> ")[1].split("<")[0]
colour = splitted[2].split("<")[0]
year = splitted[3].split("<")[0]

print(f"Make: {make}\nColour: {colour}\nYear: {year}")