import sys

from program.arguments import arguments
from program.file_manager import file_manager

arguments = arguments(sys.argv)
file_manager = file_manager(
        arguments.source_files,
        arguments.source_directories,
        arguments.output_directories
    )

if arguments.config_name != "":
    file_manager.initialize_config(arguments.config_name)

file_manager.perform_copies()
