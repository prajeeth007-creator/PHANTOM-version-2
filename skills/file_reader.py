def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()

        return content[:500]  # limit response size

    except:
        return "I cannot read that file."