import os
import json
import yaml

config = str(os.getenv('CONFIG'))

if config:
    config_data = json.loads(config)
    seed = open('seed.yml', 'w+')
    yaml.dump(config_data, seed)
else:
    raise Exception('No Config Provided!')