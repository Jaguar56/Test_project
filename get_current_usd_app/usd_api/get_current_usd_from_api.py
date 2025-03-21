import requests

API_KEY = "1ea3b75f935fe85f2b210183"  # TODO спрятать API_KEY


def get_current_usd_from_api():
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
    try:
        response = requests.get(url)
    except Exception as error:
        return "Sorry, but API not working now, try later"
    try:
        data = response.json()
        conversion_rate_usd_to_rub = data["conversion_rates"]["RUB"]
        return conversion_rate_usd_to_rub
    except Exception as error:
        return "Conversion rate usd to rub not implemented in API"
