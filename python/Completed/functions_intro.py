# think about scope here. The function can read the variables that come before, but will not alter them

m = 120
mp = 60

def calc_road_trip_time(miles,mph):
    return miles/mph

total_time = calc_road_trip_time(miles,mph)

print(total_time)
