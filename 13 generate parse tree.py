class ParseTree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = "\t" * level + self.label + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

def parse_sentence(sentence):
    words = sentence.split()
    return parse_s(words)

def parse_s(words):
    if not words:
        return None
    np_tree, np_length = parse_np(words)
    if np_tree is None:
        return None
    vp_tree = parse_vp(words[np_length:])
    if vp_tree is None:
        return None
    return ParseTree('S', [np_tree, vp_tree])

def parse_np(words):
    if not words:
        return None, 0
    det_tree, det_length = parse_det(words)
    if det_tree is None:
        return None, 0
    n_tree = parse_n(words[det_length:])
    if n_tree is None:
        return None, 0
    return ParseTree('NP', [det_tree, n_tree]), det_length + 1

def parse_vp(words):
    if not words:
        return None
    v_tree, v_length = parse_v(words)
    if v_tree is None:
        return None
    np_tree, np_length = parse_np(words[v_length:])
    if np_tree is None:
        return None
    return ParseTree('VP', [v_tree, np_tree])

def parse_det(words):
    if not words or words[0] not in ['the', 'a']:
        return None, 0
    return ParseTree('Det', [ParseTree(words[0])]), 1

def parse_n(words):
    if not words or words[0] not in ['cat', 'dog']:
        return None
    return ParseTree('N', [ParseTree(words[0])])

def parse_v(words):
    if not words or words[0] not in ['chased', 'ate']:
        return None
    return ParseTree('V', [ParseTree(words[0])]), 1

# Example usage
sentence = "the cat chased the dog"
parse_tree = parse_sentence(sentence)
if parse_tree:
    print(parse_tree)
else:
    print("Failed to parse sentence.")
