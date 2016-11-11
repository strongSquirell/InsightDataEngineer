def look_for_friend(k1, k2, d, n):
    visited = set()
    current_level = set([k1])
    for i in xrange(n):
        next_level = set()
        for x in current_level:
            visited.add(x)
            for child in d[x]:
                if k2 == child:
                    return True
                else:
                    if child not in visited:
                        next_level.add(child)
        current_level = next_level
    return False


def main():
    path1 = "./paymo_input/"
    path2 = "./paymo_output/"

    connections = dict()

    with open(path1 + "batch_payment.txt", "r") as f:
        next(f)
        for l in f:
            row = l.split(",")
            n1, n2 = map(int, row[1:3])
            connections.setdefault(n1, set()).add(n2)
            connections.setdefault(n2, set()).add(n1)

    with open(path1 + "stream_payment.txt", "r") as f:
        next(f)
        output_file1 = open(path2 + "output1.txt", "w")
        output_file2 = open(path2 + "output2.txt", "w")
        output_file3 = open(path2 + "output3.txt", "w")
        for l in f:
            row = l.split(",")
            n1, n2 = map(int, row[1:3])
            if look_for_friend(n1, n2, connections, 1):
                output_file1.write("trusted\n")
                output_file2.write("trusted\n")
                output_file3.write("trusted\n")
            else:
                output_file1.write("unverified\n")
                if look_for_friend(n1, n2, connections, 2):
                    output_file2.write("trusted\n")
                    output_file3.write("trusted\n")
                else:
                    output_file2.write("unverified\n")
                    if look_for_friend(n1, n2, connections, 3):
                        output_file3.write("trusted\n")
                    else:
                        output_file3.write("unverified\n")
            connections.setdefault(n1, set()).add(n2)
            connections.setdefault(n2, set()).add(n1)
        output_file1.close()
        output_file2.close()
        output_file3.close()

if __name__ == "__main__":
    main()
