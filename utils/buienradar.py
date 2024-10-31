from buienradar.buienradar import get_data, parse_data
from buienradar.constants import CONTENT, RAINCONTENT, SUCCESS

class BuienradarWeather:
    def __init__(self):
        """
        Initialize the weather object with optional coordinates and timeframe.

        :param latitude: Latitude for the location (default is 52.1)
        :param longitude: Longitude for the location (default is 5.10)
        :param timeframe: Minutes to look ahead for precipitation forecast (5..120)
        """

        self.weather_data = None

    @classmethod
    def fetch_weather_data(cls, latitude: float = 52.1, longitude: float = 5.10, timeframe: int = 45):
        """
        Fetch and parse weather data from Buienradar.
        
        :return: Parsed weather data, or None if fetching or parsing fails
        """
        result = get_data(latitude=latitude, longitude=longitude)
        if result.get(SUCCESS):
            data = result[CONTENT]
            raindata = result[RAINCONTENT]
            weather_data = parse_data(data, raindata, latitude, longitude, timeframe)
            return weather_data
        else:
            print("Failed to retrieve data from Buienradar.")
            return None

buienradar_instance = BuienradarWeather()
