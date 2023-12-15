def hash(string: str):
    curr = 0
    for ch in string:
        curr += ord(ch)
        curr *= 17
        curr %= 256
    return curr

def main():
    line = ''
    with open("15-input.txt", encoding='UTF-8') as file:
        line = file.readline().strip()
    vals = line.split(',')
    
    # Part 1

    hashes = [hash(x) for x in vals]
    print(sum(hashes))


    # Part 2

    labels = [x.split('=')[0].split('-')[0] for x in vals]
    commands = [x[len(labels[i]):] for i, x in enumerate(vals)]
    
    boxes = [([],[]) for _ in range(0, 256)]

    for i, label in enumerate(labels):
        box_labels, box_focal_lens = boxes[hash(label)]
        if commands[i][0] == '-':
            if label in box_labels:
                found_idx = box_labels.index(label)
                box_labels.pop(found_idx)
                box_focal_lens.pop(found_idx)
        else:
            focal_len = int(commands[i][1:])
            if label in box_labels:
                found_idx = box_labels.index(label)
                box_focal_lens[found_idx] = focal_len
            else:
                box_labels.append(label)
                box_focal_lens.append(focal_len)
    
    score = 0
    for b, box in enumerate(boxes):
        box_labels, box_focal_lens = box
        for i, lens in enumerate(box_focal_lens):
            score += (b + 1) * (i + 1) * lens
    
    print(score)
    
if __name__ == "__main__":
    main()
