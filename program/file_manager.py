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
        for file in self.source_files:
            for destination in self.output_directories:
                shutil.copy(file, destination)

        for directory in self.source_directories:
            for destination in self.output_directories:
                shutil.copytree(directory, destination)

    def initialize_config(self, config_name):
        self.config_file = open(self._CONFIG_FILE_, "a+")
        self.config_file.seek(0)

        if os.stat(self._CONFIG_FILE_).st_size > 0:
            print("size > 0")
            configs = json.load(self.config_file)

            # if not found
            self.write_config(config_name, configs)
        else:
            print("size = 0")
            self.write_config(config_name, "")

        self.config_file.close()
        
    def write_config(self, new_config_name, existing_configs):
        new_config = {
                        new_config_name: {
                        "source_files": self.source_files,
                        "source_directories": self.source_directories,
                        "output_directories": self.output_directories
                    }
                }

        if existing_configs == "":
            print("no existing")
            json.dump(new_config, self.config_file, indent=4)
            return
        print("existing")
        existing_configs.update(new_config)
        self.config_file.close()
        self.config_file = open(self._CONFIG_FILE_, "w")
        json.dump(existing_configs, self.config_file, indent=4)
