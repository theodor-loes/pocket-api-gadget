import urequests


class Api:
    def request(self, method: str, url: str, headers = None, json = dict(), timeout = 10):
        if method.upper() == 'GET':
            if headers == None:
                response = urequests.get(url, timeout=timeout)
            else:
                response = urequests.get(url, headers=headers, timeout=timeout)
        elif method.upper() == 'POST':
            if headers == None:
                response = urequests.post(url, json=json, timeout=timeout)
            else:
                response = urequests.post(url, json=json, headers=headers, timeout=timeout)
        elif method.upper() == 'PUT':
            if headers == None:
                response = urequests.put(url, json=json, timeout=timeout)
            else:
                response = urequests.put(url, json=json, headers=headers, timeout=timeout)
        else:
            raise ValueError(f'{method} is an invalid method')
        
        return response.json()