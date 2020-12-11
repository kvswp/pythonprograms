from pdfrw import PdfReader, PdfWriter
x = PdfReader('irctc.pdf')
print(x.keys())
print(x.Info)
print(x.Root.keys())
print("pdf has {} pages".format(len(x.pages)))
print(x.pages[0].Contents)
#print(x.pages[0].Contents)
#print(x.pages[0].Contents.stream)

y = PdfWriter()
y.addpage(x.pages[0])
y.write('result.pdf')
