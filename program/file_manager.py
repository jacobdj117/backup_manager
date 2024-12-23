import os
import shutil

class file_manager:
    def __init__(self, source_files, sourcce_directories, ourput_directories):
        self.source_files = source_files
        self.source_directories = sourcce_directories
        self.output_directories = ourput_directories
        return
    
    def perform_copies(self):
        for destination in self.output_directories:
            revision_suffix = self.get_revision(destination)

            # for file in self.source_files:
            #     shutil.copy(file, destination)

            for directory in self.source_directories:
                normalized_directory = os.path.normpath(directory)
                directory_name = os.path.basename(normalized_directory) + revision_suffix
                new_directory_name = os.path.join(destination, directory_name)
                shutil.copytree(directory, new_directory_name)

    def get_revision(self, path):
        highest_existing_revision = 0

        for file in os.listdir(path):
            filename = os.path.splitext(file)
            split_file = filename[0].rsplit("_v", 1)
            if len(split_file) == 1:
                return "_v1"
            
            if int(split_file[1]) > highest_existing_revision:
                highest_existing_revision = int(split_file[1])

        return "_v" + str(highest_existing_revision + 1)