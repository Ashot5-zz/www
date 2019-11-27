def pig_it(text):
    return ' '.join(('{}{}ay'.format(word[1:], word[0]) if word.isalpha() else word for word in text.split()))


if __name__ == '__main__':
    print(pig_it('this is a long text, which contains different words!'))
