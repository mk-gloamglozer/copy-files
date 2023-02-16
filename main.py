import os
import shutil
import sys


def scan_dir(origin_dir_root, bucket_dir_name, new_dir_root):
    # get all files in the directory
    print('Scanning: ' + origin_dir_root)
    files = os.listdir(origin_dir_root)
    print('found' + str(files))
    # loop through the files
    for file in files:
        # check if the file is a directory
        if os.path.isdir(os.path.join(origin_dir_root, file)):
            # if it is, call the handle_dir function
            handle_dir(origin_dir_root, bucket_dir_name, new_dir_root, file)
        else:
            # if it is not, call the handle_file function
            handle_file(origin_dir_root, bucket_dir_name, new_dir_root, file)


def handle_dir(origin_dir_root, bucket_dir_name, new_dir_root, dir):
    new_dir = os.path.join(new_dir_root, dir)
    os.mkdir(new_dir)
    # scan the new directory
    scan_dir(os.path.join(origin_dir_root, dir), bucket_dir_name, new_dir)


def handle_file(origin_dir_root, bucket_dir_name, new_dir_root, file):
    # remove the file extension
    file_name = os.path.splitext(file)[0]
    bucket_file = file_in_bucket(file_name, bucket_dir_name)
    if bucket_file:
        print('Found: ' + bucket_file)
        # copy the file from the bucket to the new directory
        to_file = os.path.join(new_dir_root, bucket_file)
        from_file = os.path.join(bucket_dir_name, bucket_file)

        # print message
        print('Copying: ' + from_file + ' to ' + to_file)
        shutil.copy(from_file, to_file)
        print('Done')

# check if the file is in the bucket
# if it is, return file name of the file in the bucket
# if it is not, return False


def file_in_bucket(file_name, bucket_dir_name):
    # get all files in the bucket
    files = os.listdir(bucket_dir_name)

    # loop through the files
    for file in files:
        # remove the file extension
        matchFile = os.path.splitext(file)[0]
        if file_name == matchFile:
            return file


# get origin bucket and new from cmd line args
origin_dir_root = sys.argv[1]
bucket_dir_name = sys.argv[2]
new_dir_root = sys.argv[3]

# if the new directory already exists, delete it
if os.path.exists(new_dir_root):
    shutil.rmtree(new_dir_root)

# make the new directory
os.mkdir(new_dir_root)

scan_dir(origin_dir_root, bucket_dir_name, new_dir_root)
