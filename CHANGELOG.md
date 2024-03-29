# Changelog

### V0.1.0 02/15/2024

- Initial Python build, port from BASIC

### V1.0.0 02/16/2024

- Fixed several errors during saving
- Fixed incorrect file path when loading
- Adjusted normalization minimum

### V2.0.0 02/17/2024

- Rewrote from ground up, for the fourth time
	- Enter .html file with table containing season data
	- Program will parse all drivers and save a text file

### V2.1.0 02/18/2024

- Added ability to view .html files inside Program
- Added print statements during calculation to show what is currently happening in the even that there is an error
- Fixed error in compensation formula
- Added settings menu to change calculation parameters

### V2.2.0 02/19/2024

- Added additional checks for normalization and weights
- Removed unnecessary print() statements
- Added int() statement to ratings as they are being saved to avoid unnecessary decimals
- Removed changelog from program, just takes up space

### V2.2.1 02/19/2024

- Fixed bug that penalized drivers for having better average starts and finishes

### V2.3.0 02/20/2024

- Added roster editor functionality to rating calculator program

### V2.3.1 02/20/2024

- Fixed future compatibility issue with pandas library

### V2.4.0 03/03/2024

- Added compatibility for championship stats that use podiums instead of top fives and top tens
- Removed settings option due to the fact I will not be offering this compiled, so all parameters can be easily adjusted by the user using any text editor
	- For the purposes of this program, these will be refered to as Traditional Motorsport Standings, as opposed to NASCAR-Style Standings