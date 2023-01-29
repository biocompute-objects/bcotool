from visual_comparator import VisualComparator


def test_same():
    overlapList = []
    # Append the actual overlaps.
    overlapList.append(["a", "b", "c"])

    # Append BCO 1 task list
    overlapList.append(["a", "b", "c"])

    # Append BCO 2 task list
    overlapList.append(["a", "b", "c"])
    return overlapList


def test_steps_before_overlap():
    overlapList = []
    # Append the actual overlaps.
    overlapList.append(["a", "b", "c"])

    # Append BCO 1 task list
    overlapList.append(["1", "a", "b", "c"])

    # Append BCO 2 task list
    overlapList.append(["2", "a", "b", "c"])
    return overlapList


def test_uneven_steps_before_overlap():
    overlapList = []
    # Append the actual overlaps.
    overlapList.append(["a", "b", "c"])

    # Append BCO 1 task list
    overlapList.append(["1", "a", "b", "c"])

    # Append BCO 2 task list
    overlapList.append(["2", "3", "a", "b", "c"])
    return overlapList


def test_uneven_steps_before_after_overlap():
    overlapList = []
    # Append the actual overlaps.
    overlapList.append(["a", "b", "c"])

    # Append BCO 1 task list
    overlapList.append(["1", "a", "b", "c", "d", "e"])

    # Append BCO 2 task list
    overlapList.append(["2", "3", "a", "b", "c"])
    return overlapList


def test_one_more_steps():
    overlapList = []
    # Append the actual overlaps.
    overlapList.append(["a", "b", "e"])

    # Append BCO 1 task list
    overlapList.append(["a", "b", "e"])

    # Append BCO 2 task list
    overlapList.append(["a", "b", "c", "d", "e"])

    return overlapList


# ol = test_uneven_steps_before_overlap()
ol = test_uneven_steps_before_after_overlap()
# ol = test_steps_before_overlap()
v = VisualComparator(ol, width=450, height=1000)
v.visualize()
v.finalize()
v.show()
