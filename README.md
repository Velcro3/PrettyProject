# Pretty Project
This is a project management tool, for when you have countless files and need organizing.
## Usage
To run, just run the python script!
### Requirements
- Python 3.11+
- PySide 6

If PySide is missing, use pip to install it. `pip install pyside6`

PySide6 is the library used for Qt bindings here.

You can also use the binaries in releases that were introduced in v1.1 bugfix 1. Note that the Mac Silicon binaries are BEST EFFORT, as I only have access to Linux, Intel Mac, and Windows. I have confirmed the binaries to work, at least on Linux/Intel Mac/Windows.
#### Note for Mac binaries
Follow these steps to make Mac run the app. You only need to do this once.
- Rename the file from .appfile to .app
- Right click (if on macbook this translates to ctrl+click) the file.
- Click Open in the context menu.
- Click Open in the warning.
After this, Mac will just run it without asking.
The reason it is .appfile, and not just .app is because GitHub releases don't allow you to upload files with the .app extension.
### Configuring
Use a file at the project root called project.toml to configure.
#### Syntax
Start with `[project]`. Set the project name with `name = <project name here>`.
Types are configured under `[[type]]`. Set a type name with `name = <type name here>`.
Then, to tell Pretty Project how to find files, use regex. This only applies to the name of the file, **not folder**.
Regex has 2 modes implemented. `some` and `all`. Some allows the regex to match anywhere in the filename. All needs the full name to match.
Configure regex like this: `regex = {match = .doc, mode = some}`
Ignoring files is done under `[ignore]` and follows this format: `ignoreme = "some"`. ignoreme is a RegEx field to tell Pretty Project how to find files to ignore, and "some" is the same as for include. Ignore has precedence over include, so with the example config below, ignoreme.ove would be ignored.
Example file:

```
[project]
name = "Toml Test"
[[type]]
name = "Natron composition"
regex = {match = ".ntp", mode = "some"}
[[type]]
name = "Olive project"
regex = {match = "[A-Z]*[a-z]*[0-9]*.ove", mode = "all"}
[ignore]
ignoreme = some
```
## Roadmap
- [x] Make a working welcome prompt
- [x] Make a file picker
- [x] Parse the TOML
- [x] Create a second window
- [x] Make a way for the second window to read the TOML
- [x] Confirm a working title
- [x] Finalize TOML
- [x] Create the UI for opening files
- [x] Actually open files
- [x] Finish this README.
- [x] Make binaries.
