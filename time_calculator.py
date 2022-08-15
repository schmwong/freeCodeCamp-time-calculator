def add_time(start, duration, start_day=""):

	
	# Step 1: Convert to 24 hour format and remove period suffix, returns tuple (hour, minute)
	def to_24h():
		hour = int(start.split()[0].split(":")[0])
		minute = int(start.split()[0].split(":")[1])
		period = start.split()[1]
		if period == "PM":
			hour += 12
		return hour, minute


	# Step 2: Convert duration string to int values, returns tuple (hour, minute)
	def timedelta():
		hour = int(duration.split(":")[0])
		minute = int(duration.split(":")[1])
		return hour, minute


	# Step 3: Calculate minute and hour values for output time,
		# include carry values as per time arithmetic logic
	def new_minute():
		new_minute = to_24h()[1] + timedelta()[1]
		carry = 0
		if new_minute > 59:
			carry += 1
			new_minute -= 60
		return new_minute, carry


	def new_hour():
		new_hour = to_24h()[0] + timedelta()[0] + new_minute()[1]
		carry = 0
		if new_hour > 23:
			carry = int(new_hour/24) # gets number of days to add
			new_hour %= 24 # assign remainder to new hour value
		return new_hour, carry


	# Step 4: Format output time in 12 hour string with period suffix
	def to_12h():
		
		end_hour = new_hour()[0]
		# for midnight value
		if end_hour == 0:
			end_hour += 12
			period = "AM"
		# for early morning value
		elif end_hour > 23:
			end_hour -= 12
			period = "AM"
		# for afternoon value
		elif end_hour > 12:
			end_hour -= 12
			period = "PM"
		# for evening value
		elif end_hour > 11:
			period = "PM"
		# everything else would be in the morning
		else:
			period = "AM"
			
		end_minute = new_minute()[0]
		if end_minute < 10:
			end_minute = f"0{end_minute}" # zero pad single digit minutes
			
		return f"{end_hour}:{end_minute} {period}"


	# Step 5: Format string output for days elapsed
		# pad spaces in the strings
	def days_elapsed():
		elapsed = new_hour()[1]
		if elapsed == 1:
			return " (next day)"
		elif elapsed > 1:
			return f" ({elapsed} days later)"
		else:
			return ""
	

	# Step 6: Calculate optional end day
	day_names = [
		"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
	]

	
	def end_day():
		# Dictionary keys are day names: {"Monday": 0, ... "Sunday": 6}
		day_to_num = dict(zip(day_names, range(7)))
		
		# Dictionary keys are integers: {0: "Monday", ... 6: "Sunday"}
		num_to_day = dict(zip(range(7), day_names))
	
		if start_day.capitalize() in day_names:
			start_day_num = day_to_num[start_day.capitalize()]
			end_day_num = start_day_num + new_hour()[1]
			
			if end_day_num > 6:
				end_day_num %= 7
				# end_day_num -= 1

			return f", {num_to_day[end_day_num]}"
			
		else:
			return ""


	# Step 7: Putting it all together
	if start_day.capitalize() in day_names:
		new_time = f"{to_12h()}{end_day()}{days_elapsed()}"
	else:
		new_time = f"{to_12h()}{days_elapsed()}"
	
	return new_time