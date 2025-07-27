def print_and_delete(folder, filename):
    tmp_dir.mkdir(parents=True, exists_ok=True)
    faasr_get_file(local_file=filename, local_folder="/tmp", remote_file=filename, remote_folder=folder)
    with open(f"{filename}", 'r') as f:
        print(f"downloaded content: {f.readline()}")
    faasr_delete_file(remote_file=filename, remote_folder=folder)
    print("file deleted -- returning True")
    return True
