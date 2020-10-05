import yaml


class Config:
    def __init__(self, path: str):
        self.path = path
        self.config = self.get_config()
        self.client_secret = self.config["client_secret"]

    def get_config(self):
        config_file = open(self.path)
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        return config


def generate_multi_line_highlight(entries: list, highlight: str = "") -> str:
    message = f"```{highlight}\n"
    for entrie in entries:
        message += entrie
    message += "\n```"
    return message

def clean_mention(mention) -> str:
    return mention[3:-1]

def make_mention(_id) -> str:
    return f"<@!{_id}>"
