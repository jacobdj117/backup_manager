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
            if not os.path.isdir(destination):
                dir_created = self.make_output_directory(destination)
                if not dir_created: continue
            else:
                print("Output contents before copies")
                self.print_dir_contents_single(destination)

            revision_suffix = self.get_revision(destination)

            for directory in self.source_directories:
                normalized_directory = os.path.normpath(directory)
                directory_name = os.path.basename(normalized_directory) + revision_suffix
                new_directory_name = os.path.join(destination, directory_name)
                shutil.copytree(directory, new_directory_name)
        
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("Output contents After copies")
        self.print_dir_contents_all()

    def make_output_directory(self, path):
        response = input("The specified output directory " + path + " does not exist.  Create? (y/n)")
        response = response.lower()
        while(True):
            if response == "y" or response == "n": break
            response = input("Unexpected entry.  use 'y' for yes and 'n' for no")

        if response == "n": return False
        print("Creating directory:", path)
        os.mkdir(path)
        return True

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
    
    def print_dir_contents_all(self):
        for dir in self.output_directories:
            self.print_dir_contents_single(dir)

    def print_dir_contents_single(self, dir):
        if not os.path.isdir(dir): return
        print("Contents of output directory ", dir, ":")
        for item in os.listdir(dir):
            print(item)
        print("- - - - - - - - - - - - - - - - - - - - ")
