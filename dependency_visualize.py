from spacy import displacy

def dependency2html(filepath):
    ex = {
        "words": [{"text": 'root', 'tag': 'root'}],
        "arcs": []
    }

    for line in open(filepath, encoding='utf-8'):
        if len(line.strip()) == 0:
            continue
        sp = line.split()
        ex['words'].append({'text': sp[1], 'tag': sp[3]})
        index = int(sp[0])
        parent_index = int(sp[6])
        if parent_index > index:
            ex['arcs'].append({'start': index, 'end': parent_index, 'label': sp[7], 'dir': 'left'})
        else:
            ex['arcs'].append({'start': parent_index, 'end': index, 'label': sp[7], 'dir': 'right'})
    html = displacy.render(ex, style='dep', manual=True)
    return html


