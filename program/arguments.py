class arguments:
    def __init__(self, args):
        self.args = args

        self.source_directories = []
        self.source_files = []
        self.output_directories = []

        self.config_name = ""
        self.save_config = False

        self.get_args()
        return

    def get_args(self):
        arg_count = len(self.args)
        index = 1

        while index < arg_count:
            arg = self.args[index]

            # Manal transfer
            if arg == "-f" or arg == "--file":
                if index + 1 >= arg_count: return
                self.source_files.append(self.args[index + 1])
                index = index + 2
            elif arg == "-d" or arg == "--directory":
                if index + 1 >= arg_count: return
                self.source_directories.append(self.args[index + 1])
                index = index + 2
            elif arg == "-o" or arg == "--output":
                if index + 1 >= arg_count: return
                self.output_directories.append(self.args[index + 1])
                index = index + 2

            # Stored transfer
            elif arg == "-c" or arg == "--config":
                if index + 1 >= arg_count: return
                self.config_name = self.args[index + 1]
                index = index + 2
            elif arg == "-s" or arg == "--save":
                self.save_config = True
                index = index + 1

            # Default
            else:
                index = index + 1