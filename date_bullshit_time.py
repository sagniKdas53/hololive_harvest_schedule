from datetime import datetime
import pytz

source_tm = datetime(2020, 9, 15, 10, 00, 00, 0000)
source_time_zone = pytz.timezone("Asia/Tokyo")
source_date_with_timezone = source_time_zone.localize(source_tm)
print(dir(datetime))
print(source_tm,source_time_zone,source_date_with_timezone)
target_time_zone = pytz.timezone('Asia/Kolkata')
noxw = datetime.now()
target_date_with_timezone = noxw.astimezone(target_time_zone)
print(noxw,noxw.tzinfo,target_date_with_timezone,target_date_with_timezone.tzinfo)
final_v = source_date_with_timezone.astimezone(target_time_zone)
print(final_v)