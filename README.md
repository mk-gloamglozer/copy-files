# Running script

`python3 main.py [origin_dir] [bucket_dir] [new_dir]`

where `origin_dir` is the directory containing the original files, `bucket_dir` is the directory containing all the exported files, and `new_dir` is the directory where the new files will be stored.

> **Note**: The script will create the `new_dir` if it does not exist and delete it and recreate it if it does.

# Example

`python3 main.py ./origin ./bucket ./new`

paths are relative to where the script is run from. The above example assumes the script is run from the same directory as the `README.md` file.
