# Pretty Project
This is a project management tool, for when you have countless files and need organizing.
## Usage
To run, just run the python script!
### Configuring
Use a file at the project root called project.toml to configure.
#### Syntax
Start with `[project]`. Set the project name with `name = <project name here>`.
Types are configured under `[[type]]`. Set a type name with `name = <type name here>`.
Then, to tell Pretty Project how to find files, use regex. This only applies to the name of the file, **not folder**.
Regex has 2 modes implemented. `some` and `all`. Some allows the regex to match anywhere in the filename. All needs the full name to match.
Configure regex like this: `regex = {match = .doc, mode = some}`
Example file:
```
```
[project]
name = "Toml Test"
[[type]]
name = "Natron composition"
regex = {match = ".ntp", mode = "some"}
[[type]]
name = "Olive project"
regex = {match = "[A-Z]*[a-z]*[0-9]*.ove", mode = "all"}
```
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
