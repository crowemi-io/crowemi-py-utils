import base64
import json


class Helper():
    @staticmethod
    def convert_config(b64: str | None) -> dict | None:
        if b64:
            try:
                config = base64.b64decode(b64).decode("utf-8")
                return json.loads(config)
            except Exception as e:
                print(f"crowemi-py-utils: Error reading config file: {e}")
                raise e
