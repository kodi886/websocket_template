import os
import json

# Read config.json file or create if it doesn't exist
config_file = "config.json"
def list_all_folders(config_file):
    if not os.path.exists(config_file):
        root_path = input("Enter root path: ")
        config_data = {"root_path": root_path}
        with open(config_file, "w") as f:
            json.dump(config_data, f)
    else:
        with open(config_file, "r") as f:
            config_data = json.load(f)
        root_path = config_data["root_path"]

    # Read issue_path or prompt user for input
    issue_path = config_data.get("issue_path")
    if not issue_path:
        issue_path = input("Enter issue path: ")
        config_data["issue_path"] = issue_path
        with open(config_file, "w") as f:
            json.dump(config_data, f)

    # Read all folders starting with "MOLY" in issue_path
    folder_list = [folder for folder in os.listdir(issue_path) if folder.startswith("MOLY")]
    return folder_list


def find_all_elt(folder_path):
    # Read all files in the folder
    file_list = os.listdir(folder_path)
    # Filter the files with .elt extension
    elt_list = [elt for elt in file_list if elt.endswith(".elt")]
    return elt_list