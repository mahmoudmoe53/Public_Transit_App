import requests


class TflApi:
    def __init__(self):
        self.asdasd = 0  


    def get_parent_number(self, stop_name):
        response = requests.get(f"https://api.tfl.gov.uk/StopPoint/Search/{stop_name}")
        if response.status_code == 200:

            data = response.json()

            return data["matches"][0]["topMostParentId"]
        

    def get_child_number(self, parent_number):
        response = requests.get(f"https://api.tfl.gov.uk/StopPoint/{parent_number}")
        if response.status_code == 200:

            data = response.json()
            return data.get("modes")



    



            