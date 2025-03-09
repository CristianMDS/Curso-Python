class Decode:
    def decode_filename(self, filename: str):
        file = filename[(filename.index('_')+1):(filename.index('.')+4)]
        return file if file != '' else ''
        

obj1 = Decode()

obj1.decode_filename('2023122512345678_sleighDesign.png.grinchwa')
obj1.decode_filename('42_chimney_dimensions.pdf.hack2023')
obj1.decode_filename('987654321_elf-roster.csv.tempfile')
obj1.decode_filename('')