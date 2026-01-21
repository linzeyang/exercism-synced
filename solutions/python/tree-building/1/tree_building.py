class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return

    records.sort(key=lambda x: x.record_id)

    if records[0].record_id != 0 or records[-1].record_id != len(records) - 1:
        raise ValueError("Record id is invalid or out of order.")

    if records[0].parent_id != 0:
        raise ValueError("Node parent_id should be smaller than its record_id.")

    trees: list[Node | None] = [None] * len(records)

    trees[0] = Node(node_id=0)

    for idx in range(1, len(records)):
        record: Record = records[idx]

        if record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")

        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")

        trees[idx] = Node(node_id=idx)
        trees[record.parent_id].children.append(trees[idx]) # type: ignore

    return trees[0]
