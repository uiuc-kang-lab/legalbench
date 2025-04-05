from pathlib import Path
import yaml

d = {}

for task in Path("tasks").glob("*"):
    print(task.name)
    prompt = task / "base_prompt.txt"
    d[task.name] = prompt.read_text().replace("’", "'")

yaml.dump(d, open("prompts.yml", "w"))
