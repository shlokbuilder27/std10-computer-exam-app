# -*- coding: utf-8 -*-
"""
Master Dataset Compiler
Combines:
- 126 SAM-1 Revision Worksheet Questions
- Textbook Chapter Exercise Questions
- Chapter Line-by-Line High Yield Notes
- Neuroscience Spaced Repetition Rules
Outputs: F:\SHLOK\me\Academics\computer_exam_app\questions_data.js
"""
import json
import os
from build_sam1_database import get_full_database
from build_textbook_database import get_textbook_exercises

# Line-by-line chapter notes
CHAPTER_NOTES = {
    1: {
        "title": "Introduction to HTML",
        "focus": "History, Basic Tags, Physical & Logical Styles, Special Entities, Hex Colors",
        "highYield": [
            "HTML was invented by Tim Berners-Lee in 1991 at CERN, derived from SGML (ISO 8879).",
            "Latest standardized version is HTML 5.0.",
            "Files are saved with .html or .htm extension. Edited in SciTE; viewed in a Web Browser (F5 to refresh).",
            "HTML document has 2 sections: <head> (metadata & title) and <body> (content visible on page).",
            "Basic tags: <h1> to <h6> (6 heading levels, h1 is largest, h6 is smallest), <p> (paragraph), <br> (empty line break), <hr> (horizontal rule).",
            "Physical Styles: <b> (bold), <i> (italic), <u> (underline), <s> (strikethrough), <tt> (typewriter monospaced).",
            "Logical Styles: <strong> (bold emphasis), <em> (italic stress), <code> (programming code), <cite> (book/movie citation).",
            "Subscript <sub> drops below baseline (H₂O); Superscript <sup> rises above baseline (x²).",
            "<pre> preserves preformatted whitespace and line returns exactly as typed.",
            "Special characters: &amp; (&, ASCII 38), &lt; (<, ASCII 60), &gt; (>, ASCII 62), &nbsp; (non-breaking space), &copy; (©), &reg; (®)."
        ],
        "neuroMnemonic": "🧠 H-T-M-L: Head + Title + Meta + Layout. <b> is Bold body, <strong> is Strong logic."
    },
    2: {
        "title": "Head and Body Sections in HTML",
        "focus": "Meta tags, <body> attributes, Color codes, Hyperlinks, Comments",
        "highYield": [
            "<head> contains metadata not rendered directly: <title>, <meta>, <style>, <script>, <base>, <link>.",
            "<meta> specifies page description, keywords, author, and refresh intervals.",
            "HTML comments: <!-- comment text --> (ignored by browser, can appear in both <head> and <body>).",
            "<body> attributes: bgcolor (background color), background (background wallpaper image), text (font color), leftmargin, topmargin (in pixels).",
            "Link color attributes: link (unvisited, default blue), vlink (visited, default purple), alink (active mouse-click, default red).",
            "Color specification: 16 named colors or 6-digit Hexadecimal #RRGGBB (00 to FF, e.g. #FF0000 Red, #00FF00 Green, #0000FF Blue, #000000 Black, #FFFFFF White).",
            "<a> tag creates hyperlinks via href attribute: <a href=\"url\">Clickable text</a>.",
            "<basefont> sets default font properties for the entire document."
        ],
        "neuroMnemonic": "🧠 V-A-L: Visited (vlink), Active (alink), Link (default). Colors in RGB triplets."
    },
    3: {
        "title": "Handling Images in HTML",
        "focus": "<img> tag, Image attributes, File formats (JPEG, GIF, PNG)",
        "highYield": [
            "<img> is an empty tag used to insert images into web pages.",
            "src (Source) specifies image URL or file path: <img src=\"photo.jpg\">.",
            "alt (Alternate text) displays description if image cannot load (crucial for screen readers and accessibility).",
            "width and height control dimensions in pixels or percentages.",
            "hspace (horizontal margin) and vspace (vertical margin) add blank cushion space around the image.",
            "border sets border frame thickness in pixels.",
            "align attribute: top, middle, bottom, left, right.",
            "Image Formats: JPEG (lossy compression, millions of colors, photos), GIF (256 colors, supports animation & transparency), PNG (lossless, full alpha transparency)."
        ],
        "neuroMnemonic": "🧠 J-P-G for Photos, G-I-F for Loops, P-N-G for Crisp Logos."
    },
    4: {
        "title": "Lists and Tables in HTML",
        "focus": "<ol>, <ul>, <dl>, <table>, <tr>, <th>, <td>, colspan, rowspan",
        "highYield": [
            "<ol> (Ordered List): numbered list (type: 1, a, A, i, I; start attribute sets starting number).",
            "<ul> (Unordered List): bulleted list (type: disc [default], circle, square).",
            "<li> (List Item): individual list entry inside <ol> or <ul>.",
            "<dl> (Definition List): glossary list; <dt> = Definition Term, <dd> = Definition Description.",
            "<table>: container; <caption> = table title placed immediately after <table>.",
            "<tr> = Table Row, <th> = Table Header (bold, centered), <td> = Table Data (normal, left-aligned).",
            "cellpadding: space between cell border and text inside. cellspacing: space between adjacent cells.",
            "colspan merges columns horizontally; rowspan merges rows vertically."
        ],
        "neuroMnemonic": "🧠 O-L for Order (1,2,3), U-L for Unordered (bullets). Table rows (<tr>) hold headers (<th>) and data (<td>)."
    },
    5: {
        "title": "Introduction to Calc",
        "focus": "Spreadsheet concept, Calc UI, Data types, Formulas, File formats",
        "highYield": [
            "Calc is an electronic Spreadsheet program in OpenOffice.org / LibreOffice.",
            "File extension: .ods (OpenDocument Spreadsheet).",
            "Default sheet names: Sheet 1, Sheet 2, Sheet 3 (at bottom tabs).",
            "Developers team: Niklas Nebel, Michael Benisch, Daniel Rentz, Eike Rathke.",
            "Formula bar: Name Box (shows active cell address like A1), Function Wizard (fx), Sum (Σ AutoSum), Input line.",
            "Data types: Text/Labels (left-aligned by default), Numbers (right-aligned), Dates/Time, Formulas (start with '=').",
            "Operators: Arithmetic (+, -, *, /, ^, %), Comparison (=, <>, <, >, <=, >=), Text concatenation (&).",
            "Shortcuts: Ctrl+N (New), Ctrl+O (Open), Ctrl+S (Save), Ctrl+Q (Quit), F1 (Help)."
        ],
        "neuroMnemonic": "🧠 Calc = .ods. Text sits LEFT, Numbers sit RIGHT, Formulas start with EQUAL (=)."
    },
    6: {
        "title": "Data Formatting and Editing in Calc",
        "focus": "Formatting cells, Page preview, Header/Footer, Validation, Sort, Filter",
        "highYield": [
            "Format Cells dialog: Ctrl + 1 (Number, Font, Alignment, Borders, Background).",
            "Header and Footer: Divided into 3 sections (Left area, Center area, Right area). Center area defaults to Sheet Name.",
            "Page Style dialog: Format -> Page (Page tab sets Portrait/Landscape orientation and Left/Right/Top/Bottom margins).",
            "Views: View -> Normal, View -> Page Break Preview (drag blue lines to adjust breaks).",
            "Editing: Cut (Ctrl+X), Copy (Ctrl+C), Paste (Ctrl+V), Find & Replace (Ctrl+F), Spell Check (F7).",
            "Data Validation: Data -> Validity (restricts input to valid ranges). 'Delete all' removes contents and validations.",
            "Data Sorting: Data -> Sort (arranges data in ascending or descending sequence).",
            "Data Filtering: Data -> Filter (AutoFilter, Standard Filter - displays matching rows, hides others)."
        ],
        "neuroMnemonic": "🧠 3 Header boxes (Left, Center, Right). F7 checks spelling, F1 gives help. 2 Orientations: Tall Portrait, Wide Landscape."
    },
    7: {
        "title": "Functions in Calc",
        "focus": "Math, Statistical, Date/Time, Logical, and Text functions",
        "highYield": [
            "All functions start with '=' sign. Insert via Function Wizard (Ctrl + F2) or direct typing.",
            "Math: SUM(), PRODUCT(), ROUND(num, digits), SQRT(), POWER(), ABS(), MOD(div, div).",
            "Statistical: AVERAGE(), COUNT() (numbers only), COUNTA() (all non-empty cells), MAX(), MIN().",
            "Date/Time: TODAY() (current date), NOW() (date & time), DATE(y,m,d), DAY() (day of month 1-31), MONTH() (1-12), YEAR().",
            "DAYS(date2, date1): Calculates date2 - date1. If date2 < date1, returns negative number!",
            "DAYSINYEAR(date): Returns 365 or 366 (leap year). YEARS(start, end, type) calculates year count.",
            "Logical: IF(condition, value_if_true, value_if_false), AND(), OR(), NOT().",
            "Text: CONCATENATE(), UPPER(), LOWER(), PROPER() (capitalizes each word), LEN(), TRIM()."
        ],
        "neuroMnemonic": "🧠 DAYS(end, start) = End minus Start. PROPER is Text, NOT Logic. IF has 3 parts: Test, Yes, No."
    },
    8: {
        "title": "Charts in Calc",
        "focus": "Chart Wizard (4 steps), Chart types (Column, Bar, Pie), Chart elements",
        "highYield": [
            "Chart Wizard has 4 steps: 1. Chart Type, 2. Data Range, 3. Data Series, 4. Chart Elements.",
            "Column Chart: Vertical rectangular columns (compares categories over time).",
            "Bar Chart: Horizontal bars.",
            "Pie Chart: Proportional circular slices of a 100% whole.",
            "XY (Scatter) Chart: Plots coordinate pairs (scientific/statistical data).",
            "Chart elements: Title, Subtitle, X-axis, Y-axis, Gridlines, Legend (the key identifying data series)."
        ],
        "neuroMnemonic": "🧠 4 Steps in Wizard: Type -> Range -> Series -> Elements. Columns stand up; Bars lie flat; Pie slices a whole."
    },
    9: {
        "title": "Problem Solving and Flowcharts",
        "focus": "IPO model, Algorithm properties, Standard flowchart symbols",
        "highYield": [
            "Problem solving steps: 1. Specify problem completely and clearly, 2. Design algorithm, 3. Draw flowchart, 4. Code, 5. Test/Debug, 6. Document.",
            "IPO model: Input -> Process (the core solution engine) -> Output.",
            "Algorithm: Finite, step-by-step, unambiguous instructions in natural language (English).",
            "Flowchart: Diagrammatic/pictorial representation of an algorithm using standard ANSI symbols.",
            "Terminal (Start/Stop): Oval / Rounded Rectangle.",
            "Input / Output: Parallelogram (e.g. Read A, Print Sum).",
            "Process: Rectangle (calculations, assignments like Sum = A + B).",
            "Decision / Condition: Diamond (rhombus) with True/False or Yes/No exit branches.",
            "Connector: Circle with letter/number inside (connects flowlines on same page).",
            "Flowlines / Arrows: Indicate direction and sequence of action."
        ],
        "neuroMnemonic": "🧠 Oval = Starts & Stops. Parallelogram = In & Out. Rectangle = Busy Working. Diamond = Decision at the crossroad."
    },
    10: {
        "title": "Introduction to C",
        "focus": "History, Dennis Ritchie, Bell Labs 1972, main(), Semicolon, .c extension",
        "highYield": [
            "Developed in 1972 by Dennis Ritchie at AT&T Bell Laboratories.",
            "Derived from B language (Ken Thompson) and BCPL.",
            "C is a structured, middle-level, case-sensitive programming language.",
            "Execution always begins at the main() function.",
            "Statements end with a semicolon (;) as the statement terminator.",
            "Curly braces { } define code blocks.",
            "Source code file extension is .c. Compiled into object file .obj / executable .exe.",
            "Comments: Single-line // and multi-line /* ... */."
        ],
        "neuroMnemonic": "🧠 C born in 1972 at Bell Labs by Dennis Ritchie. Front door is main(); full stop is semicolon (;)."
    },
    11: {
        "title": "Data Types and Operators in C",
        "focus": "32 Keywords, Data types (int, float, char), Modulus %, Logical && || !",
        "highYield": [
            "ANSI C has exactly 32 reserved keywords (cannot be used as variable names).",
            "Basic types: char (1 byte, ASCII), int (2 or 4 bytes, whole numbers), float (4 bytes, decimals), double (8 bytes, high precision), void (empty).",
            "Arithmetic operators: +, -, *, /, % (Modulus: returns remainder of integer division, e.g. 7 % 3 = 1).",
            "Relational operators: == (equality), != (not equal), <, >, <=, >=.",
            "Logical operators: && (Logical AND), || (Logical OR), ! (Logical NOT).",
            "Increment/Decrement: ++ (increment by 1), -- (decrement by 1).",
            "Ternary operator: condition ? expr1 : expr2 (Conditional operator)."
        ],
        "neuroMnemonic": "🧠 32 Teeth = 32 Keywords. 1 Byte = char. % gets remainder. == tests equality (= assigns)."
    },
    12: {
        "title": "Control Structures in C",
        "focus": "if-else, switch-case-default, loops (for, while, do-while), break, continue",
        "highYield": [
            "Selection: if, if-else, nested if, else-if ladder, switch-case.",
            "switch statement tests integral/char expressions; each case ends with 'break;'. 'default' executes if no case matches.",
            "Loops: for (entry-controlled, 3 expressions: init; condition; step), while (entry-controlled, tests condition at entry).",
            "do-while: exit-controlled loop (condition tested at the end; guarantees execution AT LEAST ONCE).",
            "break: terminates the loop or switch immediately and jumps out.",
            "continue: skips the remainder of current iteration and jumps to the next cycle."
        ],
        "neuroMnemonic": "🧠 DO-WHILE always runs at least once! BREAK breaks out; CONTINUE skips to next round."
    },
    13: {
        "title": "Arrays in C",
        "focus": "1D and 2D arrays, 0-based indexing, String '\\0' null terminator, <string.h>",
        "highYield": [
            "Array: Homogeneous collection of elements of same data type stored in contiguous memory.",
            "Indexing is strictly 0-based: First element is arr[0], last element is arr[N-1].",
            "int marks[10] has valid indices 0 to 9. Accessing marks[10] causes an out-of-bounds error.",
            "Strings in C are character arrays terminated by the null character '\\0'.",
            "\"Hello\" has 5 letters + 1 '\\0' = 6 bytes of memory.",
            "Header <string.h> provides: strlen() (string length), strcpy() (copy), strcat() (concatenate), strcmp() (compare)."
        ],
        "neuroMnemonic": "🧠 Arrays start at ZERO (0 to N-1). Strings carry '\\0' as the final stop sign."
    },
    14: {
        "title": "Functions in C",
        "focus": "Modularity, Function prototype, void, Actual vs Formal parameters, Scope",
        "highYield": [
            "Functions enable modular programming, code reusability, and easier debugging.",
            "3 elements: 1. Function declaration/prototype (ends with ;), 2. Function definition (header + body), 3. Function call.",
            "Return type 'void' means the function returns no value to the caller.",
            "Parameters: Formal parameters are in the function definition header; Actual parameters are passed during function call.",
            "Call by Value: Passes copy of data (original variables remain unchanged).",
            "Scope: Local variables (declared inside function, accessible only within it), Global variables (declared outside all functions, accessible everywhere)."
        ],
        "neuroMnemonic": "🧠 Divide & conquer with functions. VOID returns nothing. FORMAL in header, ACTUAL in call."
    }
}

def main():
    sam1_qs = get_full_database()
    tb_qs = get_textbook_exercises()
    
    master_data = {
        "metadata": {
            "title": "GSEB Class 10 Computer Studies Brain-Exam App",
            "version": "2.0-NeuroMastery",
            "examSource": "Shree Swaminarayan Gurukul Vidyalaya SAM-1 + GSEB Textbook Ch 1-14",
            "totalQuestions": len(sam1_qs) + len(tb_qs),
            "sam1Count": len(sam1_qs),
            "textbookCount": len(tb_qs)
        },
        "chapterNotes": CHAPTER_NOTES,
        "sam1Questions": sam1_qs,
        "textbookQuestions": tb_qs
    }
    
    js_content = f"// Auto-generated GSEB Class 10 Computer Studies Knowledge Base\nconst EXAM_DATABASE = {json.dumps(master_data, indent=2)};\n"
    
    out_path = r"F:\SHLOK\me\Academics\computer_exam_app\questions_data.js"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully wrote {len(sam1_qs)} SAM-1 questions and {len(tb_qs)} textbook questions to {out_path}!")

if __name__ == "__main__":
    main()
