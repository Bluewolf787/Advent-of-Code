data = []
seeds = []
seed_to_soil = []
soil_to_fer = []
fer_to_water = []
water_to_light = []
light_to_temp = []
temp_to_hum = []
hum_to_loc = []

with open('./input.txt', 'r') as file:
    headline = ''
    for line in file:
        if 'seeds' in line:
            seeds = [int(seed) for seed in line.split(': ')[1].strip().split()]

        if 'map' in line:
            headline = line.strip()

        if 'seed-to-soil' in headline:
            if '' == line.strip() or 'map' in line:
                continue
            seed_to_soil.append((int(line.split(' ')[0].strip()), int(line.split(' ')[1].strip()), int(line.split(' ')[2].strip())))
        elif 'soil-to-fertilizer' in headline:
            if '' == line.strip() or 'map' in line:
                continue
            soil_to_fer.append((int(line.split(' ')[0].strip()), int(line.split(' ')[1].strip()), int(line.split(' ')[2].strip())))
        elif 'fertilizer-to-water' in headline:
            if '' == line.strip() or 'map' in line:
                continue
            fer_to_water.append((int(line.split(' ')[0].strip()), int(line.split(' ')[1].strip()), int(line.split(' ')[2].strip())))
        elif 'water-to-light' in headline:
            if '' == line.strip() or 'map' in line:
                continue
            water_to_light.append((int(line.split(' ')[0].strip()), int(line.split(' ')[1].strip()), int(line.split(' ')[2].strip())))
        elif 'light-to-temperature' in headline:
            if '' == line.strip() or 'map' in line:
                continue
            light_to_temp.append((int(line.split(' ')[0].strip()), int(line.split(' ')[1].strip()), int(line.split(' ')[2].strip())))
        elif 'temperature-to-humidity' in headline:
            if '' == line.strip() or 'map' in line:
                continue
            temp_to_hum.append((int(line.split(' ')[0].strip()), int(line.split(' ')[1].strip()), int(line.split(' ')[2].strip())))
        elif 'humidity-to-location' in headline:
            if '' == line.strip() or 'map' in line:
                continue
            hum_to_loc.append((int(line.split(' ')[0].strip()), int(line.split(' ')[1].strip()), int(line.split(' ')[2].strip())))

def transform(list, obj):
    des = 0
    transformed = False
    for a, b, c in list:
        if obj >= b and obj <= c + b:
            des = (obj - b) + a
            transformed = True
        
    if not transformed:
        des = obj
    transformed = False

    return des 


def find_lowest_loc(locs):
    lowest = 999999999999
    for loc in locs:
        if lowest > loc:
            lowest = loc

    return lowest

def part1():
    soilds = []
    for seed in seeds:
        soilds.append(transform(seed_to_soil, seed))
    fers = []
    for soil in soilds:
        fers.append(transform(soil_to_fer, soil))
    waters = []
    for fer in fers:
        waters.append(transform(fer_to_water, fer))
    lights = []
    for water in waters:
        lights.append(transform(water_to_light, water))
    temps = []
    for light in lights:
        temps.append(transform(light_to_temp, light))
    hums = []
    for temp in temps:
        hums.append(transform(temp_to_hum, temp))
    locs = []
    for hum in hums:
        locs.append(transform(hum_to_loc, hum))

    print(find_lowest_loc(locs))


part1() # 551761867
