import yaml
import Objects


class Config:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.map = yaml.safe_load(f)
            self.checks()
            f.close()

    def checks(self):
        try:
            self.map['db']
        except KeyError:
            raise KeyError('Config is incompatible')

    def build_object(self):
        return Objects.ConfigStruct(**self.map)
