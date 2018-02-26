# Project Title

Notification creation dashboard

## Features and vision
Build a notification & scheduling dashboard using django
It will support the following attributes
Header
Content
Image

In addition to this, it should take two more inputs.
Date & time which notification should be sent
List of users

This information should be saved in backend & the notification would be scheduled to be sent at the scheduled time. 
Create a dummy function to send notification. Something like the one below

def send_notification(user_id, notification_payload)
    return True/False
    
where notification_payload would look something like
{
    "header": "Free"
    "content" "1 year subscription is free with 2 year"
    "image_url": "http://google.com/anything.jpg"
}

finally DRF

## Contributing

Feel free to contribute

## Acknowledgments

* Vibhor Singhal sir of zopper for concept
* Inspiration
* bucky tutorials for getting me started with django
* ofcourse official documentation
