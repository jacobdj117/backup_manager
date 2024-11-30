import json
import os
import shutil

class file_manager:
    _CONFIG_FILE_ = "configs.json"

    def __init__(self, source_files, sourcce_directories, ourput_directories):
        self.source_files = source_files
        self.source_directories = sourcce_directories
        self.output_directories = ourput_directories
        return
    
    def perform_copies(self):
        for destination in self.output_directories:
            revision_suffix = self.get_revision(destination)
            print(revision_suffix)

            # for file in self.source_files:
            #     shutil.copy(file, destination)

            # for directory in self.source_directories:
            #     normalized_directory = os.path.normpath(directory)
            #     directory_name = os.path.basename(normalized_directory)
            #     new_directory_name = os.path.join(destination, directory_name)
            #     shutil.copytree(directory, new_directory_name)

    def get_revision(self, path):
        highest_existing_revision = 0

        for file in os.listdir(path):
            filename = os.path.splitext(file)
            split_file = filename[0].rsplit("_v", 1)
            if len(split_file) == 1:
                return "_v1"
            highest_existing_revision = split_file[1]

        return "_v" + str(highest_existing_revision)

    def initialize_config(self, config_name):
        self.config_file = open(self._CONFIG_FILE_, "a+")
        self.config_file.seek(0)

        if os.stat(self._CONFIG_FILE_).st_size > 0:
            configs = json.load(self.config_file)
            selected_config = configs.get(config_name)

            if not selected_config:
                self.write_config(config_name, configs)
                return

            self.source_files = selected_config["source_files"]
            self.source_directories = selected_config["source_directories"]
            self.output_directories = selected_config["output_directories"]
        else:
            self.write_config(config_name, "")

        self.config_file.close()
        
    def write_config(self, new_config_name, existing_configs):
        if not self.source_directories and not self.source_files:
            print("ERROR: please specify at least one source file (-f) or source directory (-d)")
            return

        if not self.output_directories:
            print("ERROR: please specify at least one output directory (-o)")
            return

        new_config = {
                        new_config_name: {
                        "source_files": self.source_files,
                        "source_directories": self.source_directories,
                        "output_directories": self.output_directories
                    }
                }

        if existing_configs == "":
            json.dump(new_config, self.config_file, indent=4)
            return
        existing_configs.update(new_config)
        self.config_file.close()
        self.config_file = open(self._CONFIG_FILE_, "w")
        json.dump(existing_configs, self.config_file, indent=4)
