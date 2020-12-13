file_input = open("input1213.txt", "r")
#file_input = open("test_input.txt", "r")

lines = file_input.readlines()
bus_list = lines[1].strip().split(',')
buses = []
for n in  range(len(bus_list)):
	if bus_list[n] != 'x':
		buses.append((int(bus_list[n]), n))
print(buses)

def do_it3a(original_base, base_magnitude, next_bus, next_bus_offset):
	base = base_magnitude[0]
	magnitude = base_magnitude[1]
	done = False
	mult = 0
	while not done:
		modulo = (base + next_bus_offset) % next_bus
		#waiting = next_bus - modulo
		if modulo == 0:
			done = True
			magnitude *= next_bus
		else:
			base += magnitude
	print(f'base {base}, magnitude {magnitude}')
	return (base, magnitude)

original_base = buses[0][0]
base_magnitude = (buses[0][0], buses[0][0])
for n in range(1, len(buses)):
	base_magnitude = do_it3a(original_base, base_magnitude, buses[n][0], buses[n][1])
print(base_magnitude)

file_input.close()