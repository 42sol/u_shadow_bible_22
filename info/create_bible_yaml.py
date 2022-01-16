# file-uuid:    bb44d74d-87d6-402f-a394-b05c182a700a
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
#
bible = Library(named='Bible') \
    .define_allowed_abbreviation_characters('A-z0-9')\
    .define_output_file_path('./books_1.yaml')\
    .define_auto_close_section = No
#
#-------------------------------------------------------------
#
bible.start_section(named='Old Testament', abbreviated_as='ot') \
     .add_book(named='Genesis', abbreviation_as='1Mo')\
     .add_book(named='Genesis', abbreviation_as='1Mo']\
     .add_book(named='Exodus', abbreviation_as='2Mo']\
     .add_book(named='Leviticus', abbreviation_as='3Mo']\
     .add_book(named='Numbers', abbreviation_as='4Mo']\
     .add_book(named='Deuteronomy', abbreviation_as='5Mo']\
     .add_book(named='Joshua', abbreviation_as='Jo']\
     .add_book(named='Judges', abbreviation_as='Ju']\
     .add_book(named='Ruth', abbreviation_as='Ru']\
     .add_book(named='1 Samuel', abbreviation_as='1Sa']\
     .add_book(named='2 Samuel', abbreviation_as='2Sa']\
     .add_book(named='1 Kings', abbreviation_as='1Ki']\
     .add_book(named='2 Kings', abbreviation_as='2Ki']\
     .add_book(named='1 Chronicles', abbreviation_as='1Chr']\
     .add_book(named='2 Chronicles', abbreviation_as='2Chr']\
     .add_book(named='Ezra', abbreviation_as='Ez']\
     .add_book(named='Nehemiah', abbreviation_as='Ne']\
     .add_book(named='Esther', abbreviation_as='Est']\
     .add_book(named='Job', abbreviation_as='Job']\
     .add_book(named='Psalms', abbreviation_as='Ps']\
     .add_book(named='Proverbs', abbreviation_as='Prov']\
     .add_book(named='Ecclesiastes', abbreviation_as='Ecm']\
     .add_book(named='Song of Solomon', abbreviation_as='Song']\
     .add_book(named='Isaiah', abbreviation_as='Isa']\
     .add_book(named='Jeremiah', abbreviation_as='Jer']\
     .add_book(named='Lamentations', abbreviation_as='Lam']\
     .add_book(named='Ezekiel', abbreviation_as='Ez']\
     .add_book(named='Daniel', abbreviation_as='Dan']\
     .add_book(named='Hosea', abbreviation_as='Hos']\
     .add_book(named='Joel', abbreviation_as='Jo']\
     .add_book(named='Amos', abbreviation_as='Am']\
     .add_book(named='Obadiah', abbreviation_as='Ob']\
     .add_book(named='Jonah', abbreviation_as='Jon']\
     .add_book(named='Micah', abbreviation_as='Mich']\
     .add_book(named='Nahum', abbreviation_as='Nah']\
     .add_book(named='Habakkuk', abbreviation_as='Hab']\
     .add_book(named='Zephaniah', abbreviation_as='Zep']\
     .add_book(named='Haggai', abbreviation_as='Hag']\
     .add_book(named='Zechariah', abbreviation_as='Zech']\
     .add_book(named='Malachi', abbreviation_as='Mal']\
    .close_section(check_with='ot', position_at=39)
#
#-------------------------------------------------------------
#
bible.start_section(named='New Testament', abbreviated_as='nt')\
     .add_book(named='Matthew', abbreviation_as='Mt']\
     .add_book(named='Mark', abbreviation_as='Mk']\
     .add_book(named='Luke', abbreviation_as='Lk']\
     .add_book(named='John', abbreviation_as='Jn']\
     .add_book(named='Acts', abbreviation_as='Ac']\
     .add_book(named='Romans', abbreviation_as='Rom']\
     .add_book(named='1 Corinthians', abbreviation_as='1Co']\
     .add_book(named='2 Corinthians', abbreviation_as='2Co']\
     .add_book(named='Galatians', abbreviation_as='Gal']\
     .add_book(named='Ephesians', abbreviation_as='Eph']\
     .add_book(named='Philippians', abbreviation_as='Phil']\
     .add_book(named='Colossians', abbreviation_as='Col']\
     .add_book(named='1 Thessalonians', abbreviation_as='1Th']\
     .add_book(named='2 Thessalonians', abbreviation_as='2Th']\
     .add_book(named='1 Timothy', abbreviation_as='1Ti']\
     .add_book(named='2 Timothy', abbreviation_as='2Ti']\
     .add_book(named='Titus', abbreviation_as='Tit']\
     .add_book(named='Philemon', abbreviation_as='Phil']\
     .add_book(named='Hebrews', abbreviation_as='Heb']\
     .add_book(named='James', abbreviation_as='Jam']\
     .add_book(named='1 Peter', abbreviation_as='1Pe']\
     .add_book(named='2 Peter', abbreviation_as='2Pe']\
     .add_book(named='1 John', abbreviation_as='1Jn']\
     .add_book(named='2 John', abbreviation_as='2Jn']\
     .add_book(named='3 John', abbreviation_as='3Jn']\
     .add_book(named='Jude', abbreviation_as='Jud']\
     .add_book(named='Revelation', abbreviation_as='Rev']\
     .close_section(check_with='at', position_at=66)
#
#-------------------------------------------------------------
#
bible.start_section(named='Apocrypha', abbreviated_as='xt-apo')\
     .add_book(named='Tobit', abbreviation_as='Tob']\
     .add_book(named='Judith', abbreviation_as='Jth']\
     .add_book(named='Wisdom of Solomon', abbreviation_as='Wis']\
     .add_book(named='Sirach', abbreviation_as='Sir']\
     .add_book(named='Ecclesiasticus', abbreviation_as='Ecc']\
     .add_book(named='Baruch', abbreviation_as='Bar']\
     .add_book(named='Letter of Jeremiah', abbreviation_as='1Jer']\
     .add_book(named='Song of Three Youths', abbreviation_as='SgY']\
     .add_book(named='Susanna', abbreviation_as='Sus']\
     .add_book(named='Bel and the Dragon', abbreviation_as='Bel']\
     .add_book(named='1 Maccabees', abbreviation_as='1Mac']\
     .add_book(named='2 Maccabees', abbreviation_as='2Mac']\
     .add_book(named='3 Maccabees', abbreviation_as='3Mac']\
     .add_book(named='4 Maccabees', abbreviation_as='4Mac']\
     .add_book(named='1 Esdras', abbreviation_as='1Esd']\
     .add_book(named='2 Esdras', abbreviation_as='2Esd']\
     .add_book(named='Prayer of Manasseh', abbreviation_as='Man']\
     .add_book(named='Ode', abbreviation_as='Ode']\
     .add_book(named='Epistle to the Laodiceans', abbreviation_as='Lao']\
     .close_section(check_with='xt-apo', position_at=118)
#
#-------------------------------------------------------------
#
bible.write() # yaml.dump(file_stream, bible.data)
#
#-------------------------------------------------------------