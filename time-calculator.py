def add_time(start, duration, day=None):
  pmOrAm = start[len(start)-2:len(start)]
  start = start[0: len(start)-3]
  start_hrs, start_mins = start.split(":")
  duration_hrs, duration_mins = duration.split(":")
  if day != None:
    day = day.lower()
    # print(day)
#   print(pmOrAm)
#   print(start_hrs, " ", start_mins)
#   print(duration_hrs, " ", duration_mins)
  
  ################
  to_add_to_hrs = int((int(start_mins) + int(duration_mins)) / 60)
  
  new_time_hrs = (int(start_hrs) + int(duration_hrs) + int(to_add_to_hrs)) % 12
  if new_time_hrs == 0:
    new_time_hrs=12
  new_time_mins = (int(start_mins) + int(duration_mins))%60
#   if new_time_hrs <=11 and pmOrAm =="AM":
    # new_time_am_or_pm = "AM"
#   else:
    # new_time_am_or_pm = "PM"
  #military hrs
#   print()
  new_time_am_or_pm = "AM"
  if pmOrAm == "PM":
    start_hrs = str(int(start_hrs) + 12)
#   print(start_hrs)
  total_mins = (int(duration_hrs) + int(start_hrs)) * 60
  total_mins = total_mins + int(duration_mins) + int(start_mins)
  total_days = int(total_mins / 60 / 24)
#   print(start_hrs + " " + duration_hrs)
  if((total_mins/60)%24 <= 11):
    new_time_am_or_pm = "AM"
  else:
    new_time_am_or_pm = "PM"
#   print(total_days)
  new_day = None
  if day !=None:
    mydays = {"sunday": 0, "monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6}
    mydays_rev = {0: "Sunday",1: "Monday",2: "Tuesday",3: "Wednesday",4: "Thursday",5: "Friday",6: "Saturday"}
    day_number = mydays[day]
    # print(day_number)
    new_day_number = (day_number + total_days)%7
    new_day = mydays_rev[new_day_number]
  fn_time = str(new_time_hrs) + ":" + str(new_time_mins).rjust(2, "0")
  fn_time = fn_time + " " + new_time_am_or_pm
  if(new_day!=None):
    fn_time = fn_time + ", " + new_day
#   print(total_days)
  if (total_days != 0):
    if total_days == 1:
      fn_time = fn_time + " " + "(next day)"
    else:
      fn_time =  fn_time + " "+ "(" + str(total_days) +" days later)"
  return (fn_time)
