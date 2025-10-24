from gunicorn.app.base import BaseApplication
from .api import app

# import multiprocessing


class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def run():
    options = {
        "bind": "0.0.0.0:5050",
        "workers": 2,  # (multiprocessing.cpu_count() * 2) + 1,
    }
    StandaloneApplication(app, options).run()
