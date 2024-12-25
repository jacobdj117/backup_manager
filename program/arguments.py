class arguments:
    def __init__(self, args):
        self.args = args

        self.source_directories = []
        self.source_files = []
        self.output_directories = []

        self.config_name = ""

        self.list_configs = False

        self.get_args()
        return

    def get_args(self):
        arg_count = len(self.args)
        index = 1

        while index < arg_count:
            arg = self.args[index]
            if arg == "-c" or arg == "--config":
                if index + 1 >= arg_count: return
                self.config_name = self.args[index + 1]
                index = index + 2
            elif arg == "-d" or arg == "--directory":
                if index + 1 >= arg_count: return
                self.source_directories.append(self.args[index + 1])
                index = index + 2
            elif arg == "-f" or arg == "--file":
                if index + 1 >= arg_count: return
                self.source_files.append(self.args[index + 1])
                index = index + 2
            elif arg == "-l" or arg == "--list":
                self.list_configs = True
                index = index + 1
            elif arg == "-o" or arg == "--output":
                if index + 1 >= arg_count: return
                self.output_directories.append(self.args[index + 1])
                index = index + 2
            
            else:
                index = index + 1