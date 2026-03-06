import os
from pathlib import Path
PARRENTDIR = "Content"

def update_lists():
    content_dir = Path(".")
    output_dir = Path("./lists")

    output_dir.mkdir(parents=True, exist_ok=True)

    collections = {
        "lifestyle": [],
        "reviews": []
    }

    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                update_path = Path(root) / file
                clean_path = full_path.replace("\\", "/")
                new_path = PARRENTDIR + clean_path[1:]
                display_name = os.path.splitext(file)[0].replace("_", " ")
                button_html = f'<button onclick="getfile(\'{new_path}\')">{display_name}</button> <br> \n'
                path_parts = update_path.parts
                if "lifestyle" in path_parts:
                    collections["lifestyle"].append(button_html)
                elif "reviews" in path_parts:
                    collections["reviews"].append(button_html)

    for category, buttons in collections.items():
        file_path = output_dir / f"{category}.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(buttons))
        print(f"{len(buttons)} files in ({file_path}) is up to date")

if __name__ == "__main__":
    update_lists()
