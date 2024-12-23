import sys

from program.arguments import arguments
from program.config_manager import config_manager
from program.file_manager import file_manager

arguments = arguments(sys.argv)

if arguments.config_name != "":
    config_manager = config_manager(
        arguments.source_files,
        arguments.source_directories,
        arguments.output_directories
    )
    config_manager.initialize_config(arguments.config_name)
    source_files = config_manager.source_files
    source_directories = config_manager.source_directories
    output_directories = config_manager.output_directories
else:
    source_files = arguments.source_files
    source_directories = arguments.source_directories
    output_directories = arguments.output_directories

file_manager = file_manager(
        source_files,
        source_directories,
        output_directories
    )

file_manager.perform_copies()
