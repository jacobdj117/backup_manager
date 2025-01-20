# About

Backup Manager is a tool used to create redundant and incremental copies of a target directory to a local filesystem.  It's ideal use case is to assist with projects that are too large for for an online backup service, such as git, to be economical.  For example, the use case that inspired the creation of this tool is backing up music projects, which can end up containing hundreds of audio files, Digital Audio Workstation (DAW) (project files), signal chains, MIDI maps, and even video files if a song will be released with an accompanying video.


It is recommended that the system that will run the tool has access to multiple hard drives, either through a physical, local connection, or through a network.  This will allow the redundant copies to be made on different physical devices, safeguarding against equipment failure.

# Usage

## Usage Overview

### Backups
Backup Manager focuses on copying one or more source directories to one or more output directories.  Each output directory will receive a copy of each input directory.  For example, consider the following file system:

```
c:/source_1
  |-> (project files)
c:/source_2
  |-> (project files)
c:/dest_1
  | -> (empty)
c:/dest_2
  | -> (empty)
```

the ```source_n``` directories would be large project directories, and the ```dest_n``` directories would be the destination directories.  After running Backup Manager, the file structure will be as follows:

```
c:/source_1
  |-> (project files)
c:/source_2
  |-> (project files)
c:/dest_1
  |-> source_1_v1
  |    |-> (project files)
  |-> source_2_v1
       |-> (project files)
c:/dest_2
  |-> source_1_v1
  |    |-> (project files)
  |-> source_2_v1
       |-> (project files)
```

Each subsequent use of Backup Manager for the same source and destination directories will add an additional copy of each ```source_n``` directory to each ```dest_n``` directory.  Each copy will have an incremented version number, such that the copies produced by the second run will be titled ```source_n_v2```.

### Configs

Because Backup Manager frequently needs to be used to perform the same operation multiple times to backup multiple stages of a project, it maintains a config file that can be used to easily rerun an operation multiple times.  This config file is a JSON file located in the directory that Backup Manager is run from (TODO - this should be the directory where Backup Manager is located).  Each config contains a title, a set of source directories, and a set of output directories.

The first time Backup Manager is run for a particular config, every source and destination directory must be specified along with the config's name.  On all subsequent runs for a particular config, only the config name needs to be specified.

### Commands

Backup Manager supports the following runtime arguments:

| Short Command | Long Command | Description |
|---------------|--------------|-------------|
|       -c      | --config     | The name of a config.  Creates the config if it does not exist, otherwise, runs the config.
|       -d      | --directory  | A path to a single source directory.  May be specified multiple times per run.
|       -h      | --help       | Print a help statement then close.
|       -l      | --list       | List the names of the existing configs.
|       -o      | --output     | A path to a single output directory.  May be specified multiple times per run.

### Examples

Given the following file system:
```
c:/source_1
  |-> (project files)
c:/source_2
  |-> (project files)
c:/dest_1
  | -> (empty)
c:/dest_2
  | -> (empty)
```

#### Example 1: Simple Backup

To create a backup of each source directory in each destination directory, use the following command.

```python <path to backup manager>/backup_manager.py -d "C:/source_1" -d "C:/source_2" -o "C:/dest_1" -o "C:/dest_2"```

#### Example 2: Config Creation

To create a backup of each source directory in each destination directory and save the operation as a new config, use the following command.

```python <path to backup manager>/backup_manager.py -c example_config -d "C:/source_1" -d "C:/source_2" -o "C:/dest_1" -o "C:/dest_2"```

#### Example 3: Config Usage

To run an operation stored in a previously created config, use the following command:

```python <path to backup manager>/backup_manager.py -c example_config```

# Release Notes

* v0.1 - Initial release.  Contains all the basic config management and file copying functionality
* v0.2 - User Experiance Improvements.  Adds ability to view the names of stored configs, a help command, and displayes of progress to the user.