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
            elif arg == "-h" or arg == "--help":
                self.show_help()
                exit()
            elif arg == "-l" or arg == "--list":
                self.list_configs = True
                index = index + 1
            elif arg == "-o" or arg == "--output":
                if index + 1 >= arg_count: return
                self.output_directories.append(self.args[index + 1])
                index = index + 2
            
            else:
                index = index + 1
    
    def show_help(self):
        print("-c  --config    | Specify the name of a config to run.  If the config exists,")
        print("                | the source and output paths stored in it will be used.  If")
        print("                | the config does not exist, a new config with the specified")
        print("                | name will be created using the -d, -f and -o arguments provided")
        print("-d  --directory | A directory to be backed up.  Specify the whole path.  If the")
        print("                | path containes spaces, it must be enclosed in quotes.  Multiple")
        print("                | directories may be specified by using multiple -d arguments")
        print("-f  --file      | A file to be backed up.  Specify the whole path.  If the")
        print("                | path containes spaces, it must be enclosed in quotes.  Multiple")
        print("                | paths may be specified by using multiple -f arguments")
        print("-h  --help      | Display this help readout")
        print("-l  --list      | Display the names of all existing configs")
        print("-o  --output    | A path to place the specified input files and directories.")
        print("                | Specify the whole path.  If the path contains spaces, enclose")
        print("                | it in quotes.  Multiple outputs may be specified bu using")
        print("                | -o arguments")
        