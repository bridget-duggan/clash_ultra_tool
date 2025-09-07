import requests

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjljZmI2ZWViLTU4MDEtNDZhMS04NzU2LTMyNmYwNTc0NmYyNSIsImlhdCI6MTc1NzI0NDAyOCwic3ViIjoiZGV2ZWxvcGVyLzNmZjljYjdhLWUyYzItODM0NS0xNGFhLTk3ZDE4OTlmNDBmYSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjQ3LjU0LjM2LjE1MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.1lzZEMGEqDqiQp87YXgNd7eLKk_C2ptEkUYQzA2Oebcr9fRM_b_fMl-Fz2ukhuXZiGV5UvYLDKQ7y90xbnPawA'

HEADERS = {
    'Accept': 'application/json',
    'authorization': f'Bearer {TOKEN}'
}


def get_user(user_id):
    # Return user profile information
    try:
        response = requests.get(f'https://api.clashofclans.com/v1/players/{user_id}', headers=HEADERS)

        if response.status_code != 200:
            error_json = response.json()
            print(f"API error {response.status_code}: {error_json.get('reason', error_json)}")
            return None
    
        user_json = response.json()
        return user_json
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"JSON decode error: {e}")


def search_clans(name = 'test'):
    # Search all clans
    try:
        response = requests.get(f'https://api.clashofclans.com/v1/clans?name={name}', headers=HEADERS)

        if response.status_code != 200:
            error_json = response.json()
            print(f"API error {response.status_code}: {error_json.get('reason', error_json)}")
            return None
    
        clans_json = response.json()
        return clans_json
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"JSON decode error: {e}")


print(get_user('Wiggles012'))
print(search_clans('Ducati Demons'))