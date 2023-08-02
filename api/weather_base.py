import random


class WeatherApi:
    def get_temperature(self):
        """気温の取得"""
        temperature = random.randint(-4, 32)
        return temperature

    def get_humidity(self):
        """湿度の取得"""
        humidity = random.randint(40, 80)
        return humidity

    def get_pressure(self):
        """気圧(hPa)の取得"""
        pressure = random.randint(940, 1080)
        return pressure

    def get_UV_level(self):
        """UV レベルの取得"""
        UV_level = random.randint(1, 5)
        return UV_level

    def get_people_level(self):
        """賑わい具合の取得"""
        people_level = random.randint(1, 5)
        return people_level
