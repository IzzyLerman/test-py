def print_and_delete(folder, filename):
    faasr_get_file(local_file=filename, local_folder="/tmp", remote_file=filename, remote_folder=folder)
    local_path = f"/tmp/{filename}"
    with open(local_path, 'r') as f:
        print(f"downloaded content: {f.readline()}")
    faasr_delete_file(remote_file=filename, remote_folder=folder)
    print("file deleted -- returning True")
    return True
