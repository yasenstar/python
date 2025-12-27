languages = ["Regional Assembly Language","Autocode","FORTRAN","IPL (LISP的先驱)","FLOW-MATIC (COBOL的先驱)","COMTRAN (COBOL的先驱)","LISP","ALGOL 58","FACT (COBOL的先驱)","COBOL","APL","Simula","SNOBOL","CPL (C的先驱)","BASIC","PL/I","BCPL (C的先驱)","Logo","Pascal","Forth","C语言","Smalltalk","Prolog","ML","Scheme","SQL","Ada","C++","Common Lisp","MATLAB","Eiffel","Objective-C","Erlang","Perl","Tcl","FL (Backus)","Haskell","Python","Visual Basic","HTML","Ruby","Lua","CLOS (part of ANSI Common Lisp)","Java","Delphi (Object Pascal)","JavaScript","PHP","REBOL","D","C#","Visual Basic .NET","F#","Scala","Factor","Windows PowerShell","Rust","Clojure","Go"]

years = [1951, 1952, 1954, 1954, 1955, 1957, 1958, 1958, 1959, 1959, 1962, 1962, 1962, 1963, 1964, 1964, 1967 ,1968 ,1970 ,1970 ,1972 ,1972 ,1972 ,1973 ,1975 ,1978 ,1980 ,1983 ,1984 ,1984 ,1985 ,1986 ,1986 ,1987 ,1988 ,1989 ,1990 ,1991 ,1991 ,1991 ,1993 ,1993 ,1994 ,1995 ,1995 ,1995 ,1995 ,1997 ,1999 ,2001 ,2001 ,2002 ,2003 ,2003 ,2006 ,2006 ,2007 ,2009]

# A
if __name__ == '__main__':
    for i in range(0, len(languages)):
        language = languages[i]
        year = years[i]
        print(language, ':', year)

# B
if __name__ == '__main__':
    [print(languages[i], ':', years[i]) for i in range(0, len(languages))]


# C
if __name__ == '__main__':
    i = 0
    while i < len(years):
        language = languages[i]
        year = years[i]
        print(language, ':', year)
        i += 1

# D
if __name__ == '__main__':
    for language in languages:
        for year in years:
            print(language, ':', year)