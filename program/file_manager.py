import shutil

class file_manager:
    _CONFIG_FILE_ = "configs.csv"

    def __init__(self, source_files, sourcce_directories, ourput_directories):
        self.source_files = source_files
        self.source_directories = sourcce_directories
        self.output_directories = ourput_directories
        return
    
    def __init__(self):
        self.source_files = []
        self.source_directories = []
        self.output_directories = []
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

        if not self.read_config(config_name):
            self.create_config(config_name)

        self.config_file.close()

    def read_config(self, config_name):
        for line in self.config_file:
            print(line)
        return False
    
    def create_config(self, config_name):
        self.config_file.write(config_name + "\n")
        return