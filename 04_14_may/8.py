exam_time_hour = int(input())
exam_time_minutes = int(input())
arrival_time_hour = int(input())
arrival_time_minutes = int(input())

exam_time = (exam_time_hour * 60) + exam_time_minutes
arrival_time = (arrival_time_hour * 60) + arrival_time_minutes

hours = 0
minutes = 0
total = 0

if (exam_time - 30) <= arrival_time <= exam_time:
    print("On time")
if arrival_time > exam_time:
    print("Late")
if arrival_time < (exam_time - 30):
    print("Early")

if (exam_time - 60) < arrival_time < exam_time:
    print(f"{exam_time - arrival_time} minutes before the start")
if arrival_time <= (exam_time - 60):
    minutes = exam_time - arrival_time
    if arrival_time >= 60:
        hours = minutes // 60
        minutes = minutes % 60
    print(f"{hours}:{minutes:02} hours before the start")
if exam_time + 60 > arrival_time > exam_time:
    print(f"{arrival_time - exam_time} minutes after the start")
if arrival_time >= (exam_time + 60):
    minutes = arrival_time - exam_time
    if arrival_time >= 60:
        hours += 1
        minutes = minutes - 60
    print(f"{hours}:{minutes:02} hours after the start")
