import requests


class TflApi:
    def __init__(self):
        pass  


    def get_parent_number(self, stop_name):

        '''gets the initial value required to get the naptanid'''

        response = requests.get(f"https://api.tfl.gov.uk/StopPoint/Search/{stop_name}")
        if response.status_code == 200:
            data = response.json()
            return data["matches"][0]["topMostParentId"]
        

    def get_child_number(self, parent_number, stop_letter):

        '''returns the naptanid'''

        if "Stop " in stop_letter:
            stop_letter = stop_letter.replace("Stop ", "")
        
        response = requests.get(f"https://api.tfl.gov.uk/StopPoint/{parent_number}")
        if response.status_code == 200:
            data = response.json()
            
            for child in data.get("children", []):
                if child.get("stopLetter") == stop_letter:
                    return child.get("naptanId") 
            return None
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None

    def get_live_arrivals(self, naptan_id):

        '''returns a timetable of upcoing buses'''

        response = requests.get(f"https://api.tfl.gov.uk/StopPoint/{naptan_id}/Arrivals")
        if response.status_code == 200:
            data = response.json()
            expected_arrivals = [item.get("expectedArrival") for item in data]
            return expected_arrivals
        else:
            print(f"Failed to fetch arrivals data: {response.status_code}")
            return None