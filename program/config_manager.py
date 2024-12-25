import json
import os

class config_manager:
    _CONFIG_FILE_ = "configs.json"

    def __init__(self, source_files, sourcce_directories, ourput_directories):
        self.source_files = source_files
        self.source_directories = sourcce_directories
        self.output_directories = ourput_directories

    def __init__(self):
        self.source_files = []
        self.source_directories = []
        self.output_directories = []

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

        self.print_config(config_name)
        self.config_file.close()
        
    def write_config(self, new_config_name, existing_configs):
        if not self.source_directories and not self.source_files:
            print("ERROR: please specify at least one source file (-f) or source directory (-d)")
            return

        if not self.output_directories:
            print("ERROR: please specify at least one output directory (-o)")
            return

        print("Creating new config: ", new_config_name)
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

    def source_files(self): return self.source_files
    def source_directories(self): return self.source_directories
    def output_directories(self): return self.output_directories

    def print_config(self, config_name):
        print("Running config ", config_name, ", which has the following parameters:")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        if len(self.source_files) > 0:
            print("Source Files:")
            for file in self.source_files:
                print(file)
        else:
            print("No source Files")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        if len(self.source_directories) > 0:
            print("Source Directories:")
            for dir in self.source_directories:
                print(dir)
        else:
            print("No Source Directories")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        if len(self.output_directories) > 0:
            print("Output Directories:")
            for output in self.output_directories:
                print(output)
        else:
            # TODO - This should be an error case - close the program and tell the user than an output is needed
            print("No Output Directories")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
