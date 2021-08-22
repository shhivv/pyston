
class Output:
    def __init__(self, json_response: dict):
        self._json_response = json_response
        self.langauge = json_response["language"]
        self.version = json_response["version"]
        self.code = json_response["run"]["code"]
        self.signal = json_response["run"]["signal"]
        self.output = json_response["run"]["output"]
        self.stdout = json_response["run"]["stdout"]
        self.stderr = json_response["run"]["stderr"]

    def __repr__(self):
        return self.output

    @property
    def success(self):
        return bool(self.stdout)

    @property
    def raw_json(self):
        return self._json_response
