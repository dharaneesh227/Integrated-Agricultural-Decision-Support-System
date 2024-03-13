# decision_tree.py
from app import Decision_Node
class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        return val == self.value

    def match2(self, example):
        if example == 'True' or example == 'true' or example == '1':
            return True
        else:
            return False

    def __repr__(self):
        return "Is %s %s %s?" % (header[self.column], "==", str(self.value))


def class_counts(data):
    counts = {}
    for row in data:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


class Leaf:
    def __init__(self, data):
        self.predictions = class_counts(data)


class Decision_Node:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def print_tree(node, spacing=""):
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return
    print(spacing + str(node.question))
    print(spacing + "--> True:")
    print_tree(node.true_branch, spacing + " ")

    print(spacing + "--> False:")
    print_tree(node.false_branch, spacing + " ")


def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100))  # + "%"
    return probs


def classify(row, node):
    if isinstance(node, Leaf):
        return node.predictions
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)
