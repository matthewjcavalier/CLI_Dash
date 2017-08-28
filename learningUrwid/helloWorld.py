import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    text.set_text(repr(key))

palette = [('banner', 'black', 'light gray'),
           ('streak', 'black', 'dark red'),
           ('bg', 'white', 'yellow')]

text = urwid.Text(('banner', u'Hello World!'), align='center')
mapOne = urwid.AttrMap(text, 'streak')
fill = urwid.Filler(mapOne)
mapTwo = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(mapTwo, palette, unhandled_input=show_or_exit)
loop.run()
