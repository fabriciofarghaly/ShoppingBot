# WebServer

This is a simple Flask web server to facilitate the infomation sharing between a ShoppingBot's ARuCo Tag scanner and the associated iOS App "ShoppingBot"

## Usage
0. (Optional) In this directory run `python json_loader.py` and enter item infomation and itemIDs.
    * itemIDs should be the ids associated with the ARuCo tags on each item.
1. In this directory run `python app.py`
    * Take note of them line `Running on http://<ip address>:8080/`, this will be needed to configure the iOS app to communicate with each running server instance.

