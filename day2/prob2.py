def get_offset(alpha, beta):
    if alpha == beta:
        return
    offset = 0
    for alpha_char, beta_char in zip(alpha, beta):
        if alpha_char != beta_char:
            offset += 1
        if offset > 1:
            return
    return offset


def find_match(box_ids):
    for alpha in box_ids:
        alpha = alpha.strip()
        for beta in box_ids:
            beta = beta.strip()
            if get_offset(alpha, beta):
                return ''.join([alpha[i] for i in range(0, len(alpha)) if alpha[i] == beta[i]])


with open('source.txt') as source:
    print find_match(source.readlines())
