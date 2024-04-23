from request import get_info

def get_total_amount_clp():
	entries_filter = get_info()
	total = 0
	for entry in entries_filter:
		amount = float(entry[1])
		price  = float(entry[2])
		total_entry = amount * price
		total += total_entry

	return round(total, 2)

