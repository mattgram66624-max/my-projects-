import os 

structure = {
    "my_scraper": {
        "data":{},
        "logs":{},
        "main.py":(""),
        "scraper.py":"",
        "requairements.txt":"",
        "README.md":""

    }
}

def create_structure(base_path, blueprint):
    for name,content in blueprint.items():
        current_path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, content)
        else:
            with open(current_path, 'w')as f:
                f.write(content)
        print(f"successfully generated project structure at: {os.path.abspath(base_path)}")

if __name__ == "__main__":
    create_structure(".",structure)