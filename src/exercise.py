from request import get_info_today, get_info_a_year_ago

def get_total_amount_clp_today():
	entries_filter = get_info_today()
	return _total(entries_filter)

def get_comparative():
	entries_filter = get_info_a_year_ago()
	total_a_year_ago = _total(entries_filter)
	total_today =  get_total_amount_clp_today()
	return _calculate_increase_percentage(total_today, total_a_year_ago)

def get_amount_lost():
		total_today = get_total_amount_clp_today()
		lost = total_today * 0.8 / 100
		return round(lost, 2)

def _total(entries_filter):
    total = 0
    for entry in entries_filter:
     amount = float(entry[1])
     price  = float(entry[2])
     total_entry = amount * price
     total += total_entry

    return round(total, 2)

def _calculate_increase_percentage(today, a_year_ago):
     value = ((today - a_year_ago) / a_year_ago) * 100
     return round(value, 2)
     