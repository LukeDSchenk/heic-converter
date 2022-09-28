import logging

from app import ImgConverter

logging.basicConfig(format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s")

if __name__ == "__main__":
    app = ImgConverter()
    app.run()
