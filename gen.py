import genanki

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

  
def highlight(lines):
    i = 0
    hstr = ''
    book_name = ''
    location = ''
    for line in lines:
        # import ipdb; ipdb.set_trace()
        if line == "==========\n":
            yield (book_name, location, hstr)
            i = 0
            hstr = ''
            book_name = ''
            location = ''
        elif i == 0:
            book_name = line.split('\n')[0]
            i = i+1
        elif i == 1:
            location = line.split('\n')[0]
            i = i+1
        elif i == 2:
            i = i+2 # empty line
        else:
            hstr = hstr + line + '\n'



my_deck = genanki.Deck(
  2059400111,
  'Kindle Highlights')


with open('./kindle_highlights.txt', 'r') as highlights:
    lines = highlights.readlines()
    i = 0
    for (book_name, location, note) in highlight(lines):
        # print(book_name)
        # print(location)
        # print(note)
        # if len(note.split('\n')) > 2:
        #     print(book_name)
        #     print(note)
        anki_note = genanki.Note(model=my_model, fields = [book_name, note])
        my_deck.add_note(anki_note)
    genanki.Package(my_deck).write_to_file('khigh.apkg')
  
# my_note = genanki.Note(model=my_model,
#                        fields=['Capital of Argentina', 'Buenos Aires'])
# my_note2 = genanki.Note(model=my_model,
#                         fields=['Capital of India', 'New Delhi'])


# my_deck.add_note(my_note)
# my_deck.add_note(my_note2)
# genanki.Package(my_deck).write_to_file('output.apkg')

