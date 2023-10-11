from pyghthouse import Pyghthouse

from config import UNAME, API_TOKEN


class LighthouseConnector:

    def __init__(self):
        self.__p = Pyghthouse(UNAME, API_TOKEN)
        self.__p.start()

    def draw(self, img: list):
        self.__p.set_image(img)

    def get_empty_image(self) -> list:
        return Pyghthouse.empty_image()

    def stop(self) -> None:
        self.__p.stop()
