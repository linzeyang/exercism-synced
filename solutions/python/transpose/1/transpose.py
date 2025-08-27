def transpose(lines):
    if not lines:
        return ""

    lines = lines.split("\n")

    num_columns = len(lines)
    num_rows = max(len(line) for line in lines)

    out = []

    for i in range(num_rows):
        new_line = []
        for j in range(num_columns):
            try:
                new_line.append(lines[j][i])
            except IndexError:
                new_line.append("$")
        new_line = "".join(new_line).rstrip("$")
        new_line = new_line.replace("$", " ")
        out.append(new_line)

    return "\n".join(out)
