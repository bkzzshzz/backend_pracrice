# so logic is basically about making decisions based on the given information(s). there's always an outcome of a logical statement 

# the operators like >, <, >=, <=, !,!=, == help in comparison

# operators like and, or not can also be used to comparre statements

from xml.dom.minidom import TypeInfo


is_homework_finished = True
is_today_friday = False
is_tomorow_holiday = False

if is_homework_finished and is_today_friday or is_tomorow_holiday:
    print("We go to bhatbhateni tomorrow")

if not is_tomorow_holiday:
    print("Wait for friday")
