from Laboratory.common_classes.Classes import List, CList, Node


def double_link_list_to_circular_list(n: List) -> CList:
    result: CList = CList(n.get_head())
    _node: Node = n.get_head().get_right_link()
    while _node is not None:
        result.add(_node.get_data())
        _node = _node.get_right_link()
    return result
