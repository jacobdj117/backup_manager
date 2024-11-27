import sys

from program.arguments import arguments
from program.file_manager import file_manager

arguments = arguments(sys.argv)

if arguments.config_name != "":
    file_manager = file_manager()
    file_manager.initialize_config(
        arguments.config_name,
        arguments.save_config)
else:
    file_manager = file_manager(
        arguments.source_files,
        arguments.source_directories,
        arguments.output_directories
    )
