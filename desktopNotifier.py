import time
from plyer import notification
import codecs
from topNews import topNews

ICON_PATH = "F:\Python Learning\python_All\Desktop Notifier\icon.ico"

# fetch news items
newsItems = topNews()

for item in newsItems:

    try:
        notification.notify(title='Breaking News',
            message=codecs.decode(item['title']),
            app_name='Desktop Notifier',app_icon=ICON_PATH,
            ticker="Hello World!",timeout=10,toast=False)
    except ValueError:
        continue
    
    time.sleep(10)
    
    

time.sleep(5)





