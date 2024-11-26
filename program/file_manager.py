import shutil

class file_manager:
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