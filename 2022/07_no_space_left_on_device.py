from functools import cached_property

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.direct_file_size = 0

    @cached_property
    def size(self):
        return self.direct_file_size + sum(child.size for child in self.children.values())

def read_directory(file, directory):
    file.readline() # ls command

    # Parse ls output
    line = '' # Thre's probably a better way to disappear this error
    while (line := file.readline()) and line[0] != '$':
        parts = line.split(' ')
        if parts[0] == 'dir':
            new_dir_name = parts[1].strip()
            directory.children[new_dir_name] = Directory(new_dir_name)
        else:
            size = int(parts[0])
            directory.direct_file_size += size

    # Parse child directories
    while (parts := line.split()) and parts[1] == 'cd' and parts[2] != '..':
        dir_name = parts[2]
        read_directory(file, directory.children[dir_name])
        line = file.readline()

def sum_of_max_size(directory, max_size):
    size_sum = 0
    if directory.size <= max_size:
        size_sum += directory.size
    size_sum += sum(sum_of_max_size(child, max_size) for child in directory.children.values())
    return size_sum

def smallest_of_min(directory, req_size):
    child_options = [smallest_of_min(child, req_size) for child in directory.children.values()]
    filtered = [opt for opt in child_options if opt >= req_size]
    if filtered:
        return min(filtered)
    else:
        return directory.size

def main():
    with open("07input.txt", encoding='UTF-8') as file:
        initial_cd = file.readline()
        root = Directory(initial_cd.split(' ')[2].strip())
        read_directory(file, root)
    # print(sum_of_max_size(root, 100000))
    req_size = 30000000 - (70000000 - root.size)
    print(smallest_of_min(root, req_size))

if __name__ == "__main__":
    main()
