import sys
import xml.parsers.expat

def unescape(s):
    want_unicode = False
    if isinstance(s, unicode):
        s = s.encode("utf-8")
        want_unicode = True

    list = []

    p = xml.parsers.expat.ParserCreate("utf-8")
    p.buffer_text = True
    p.returns_unicode = want_unicode
    p.CharacterDataHandler = list.append

    p.Parse("<e>", 0)
    p.Parse(s, 0)
    p.Parse("</e>", 1)

    es = ""
    if want_unicode:
        es = u""
    return es.join(list)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print 'usage: python %s <escaped str>' % args[0]
        sys.exit(1)
    print unescape(args[1])
