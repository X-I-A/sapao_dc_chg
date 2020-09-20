# SAP Analysis For Office Data Source Migration
## Purpose
When user change the data source of SAP Analysis, all layout is lost even if the data structure of two data source is exactly the same.

Espacially in the migration procedure, we can lost a lot of time due to this missed functionality

## Howto Guide
1. Get the Analysis Office Cube String
2. Save the Analysis Office Cube String as the origin.txt
3. Launch the main.py with the following syntax: `python3 main.py <source_cube_name> <destination_cube_name>'
4. The result will be saved to result.txt

## Analysis Office Cube String
1. Unzip the Analysis Office File to a directory
2. Find and open the .bin file which contains the Anaysis Office
3. Each Cube String is store as base64 encoded String
