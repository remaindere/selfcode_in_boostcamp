class Note :
    def __init__(self, content = None) :
        self.content = content

    def remove(self) :
        self.content = ""

    def __str__(self) :
        return "Note contains : %s" % \
                self.content
    
    def __add__(self, other) :
        return self.content + other.content

    def get_note_content(self) :
        return self.content

    def change_note_content(self, content) :
        self.content = content

class Notebook :
    def __init__(self):
        self.pagecount = 0
        self.notes = {}
    
    def insert(self, note, pagenumber) :
        if self.pagecount <= 300 :
            self.notes[pagenumber] = note.get_note_content()
            self.pagecount +=1
        else :
            print("Cannot create more pages")

    def remove(self, pagenumber) :
        del(self.notes[pagenumber])
        #we can use notes.pop(pagenumber-1), instead
        print("Removed %d page note" % \
                pagenumber)

    def get_number_of_pages(self) :
        return self.pagecount

    def get_content_of_pages(self, pagenumber) :
        return self.notes[pagenumber]

lecture_points = Note("1+1=2")
naksur = Note("aaaaaaaaa so lazy")
pandas = Note("no panda in here")

print(lecture_points)
print(naksur)
print(pandas)

my_personal_diary = Notebook()
my_personal_diary.insert(lecture_points, 1)
my_personal_diary.insert(naksur, 2)
my_personal_diary.insert(pandas, 3)

print(my_personal_diary.get_number_of_pages())
print(my_personal_diary.get_content_of_pages(1))
print(my_personal_diary.get_content_of_pages(2))
print(my_personal_diary.get_content_of_pages(3))
