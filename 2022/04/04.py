sections = []

with open('input.txt', 'r') as file:
    section = []
    for line in file:
        l = line.strip()
        section.append(int(l.split('-')[0]))
        section.append(int(l.split(',')[0].split('-')[1]))
        section.append(int(l.split(',')[1].split('-')[0]))
        section.append(int(l.split('-')[2]))
        
        sections.append(section.copy())
        section.clear()

#print(sections)

def puzzle1(sections):
    count = 0
    for section in sections:
        if section[0] >= section[2] and section[1] <= section[3]:
            count += 1
        elif section[2] >= section[0] and section[3] <= section[1]:
            count += 1

    return count

def puzzle2(sections):
    count = 0

    for section in sections:
        if section[1] == section[2] or section[3] == section[0]:
            count += 1
        elif section[1] <= section[3] and section[1] >= section[2]:
            count += 1
        elif section[3] <= section[1] and section[3] >= section[0]:
            # 4-8,2-6
            count += 1
        elif section[0] >= section[2] and section[1] <= section[3]:
            count += 1
        elif section[2] >= section[0] and section[3] <= section[1]:
            count += 1

    return count


print(puzzle1(sections))
print(puzzle2(sections))