# file-uuid:    faf50ae7-ea61-46f1-9612-9d0fb4b170a7
# project-uuid: 0d4d2fbf-596a-4fd9-9452-783d3dfa05d3
#-------------------------------------------------------------
#
# SUI Definitions
# - lang: english
#-------------------------------------------------------------
No = False
Yes = True
#
#-------------------------------------------------------------

class Bible_Book:

    def __init__(self, group, index_in_bible, position, name, abbreviation, aliases = []):
        self.key = f'book-{group}-{index_in_bible}'  
        self.position = position 
        self.name = name 
        self.abbreviation = abbreviation
        self.aliases = aliases


    def is_ot(self):
        return '-ot-' in self.key
