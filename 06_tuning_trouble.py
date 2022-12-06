def get_line(file_name):
    with open(file_name, encoding='UTF-8') as file:
        for line in file:
            return line
    raise Exception('File is empty')
    
def find_first_marker(line, marker_len):
    for i in range(marker_len, len(line) + 1):
        potential_marker = line[i - marker_len : i]
        pm_as_list = [*potential_marker]
        if len(pm_as_list) == len(set(pm_as_list)):
            return i
    raise Exception('Did not find a marker')

def main():
    line = get_line('06input.txt')
    first_marker = find_first_marker(line, marker_len=14)
    print(first_marker)

if __name__ == "__main__":
    main()
