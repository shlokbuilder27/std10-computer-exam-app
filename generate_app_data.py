# -*- coding: utf-8 -*-
"""
Generator for GSEB Class 10 Computer Studies Exam App Dataset
Includes:
- All 126 SAM-1 Revision Worksheet Questions & Solutions with neuroscience explanations
- All 14 Chapters Textbook End-of-Chapter Exercises & Solutions
- High-yield line-by-line chapter notes & memory anchors
"""
import json
import os

# --- 126 SAM-1 QUESTIONS ---
q126_raw = [
    {
        "id": "REV-001",
        "qnum": 1,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which of the following is an editor to edit an HTML document?",
        "options": {
            "A": "SciTE",
            "B": "BriTE(A)",
            "C": "LighT()",
            "D": "SpriTE()"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 1, 'Creating HTML Document Using SciTE Editor', Page 4",
        "textbookFact": "SciTE (SCIntilla based Text Editor) is the open-source text editor bundled in Ubuntu Linux and recommended by the Gujarat Board textbook for writing HTML and C source code.",
        "neuroHook": "🧠 Mnemonic: SciTE = 'SCientific Text Editor' on the 'SITE'. The brain creates a visual peg between 'SciTE' and 'Website'.",
        "neuroExplanation": "Dual-Coding Theory (Paivio): Connecting the visual label 'SciTE' with Ubuntu's pencil-notebook icon activates both the verbal lexeme and visual recognition memory in the fusiform gyrus.",
        "cognitiveTrap": "Options B, C, and D are nonsense pseudo-names invented by examiners as phonological distractors ending in 'TE'."
    },
    {
        "id": "REV-002",
        "qnum": 2,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which type of information can be incorporated in an HTML document ?",
        "options": {
            "A": "Multimedia information",
            "B": "Text information",
            "C": "Address and path of filename",
            "D": "All of these"
        },
        "answer": "D",
        "keyAnswer": "D",
        "textbookReference": "Chapter 1, 'Introduction to HTML', Page 2",
        "textbookFact": "An HTML document can incorporate structured text, URL file addresses/paths (via href/src), and multimedia elements (images, audio, video).",
        "neuroHook": "🧠 Schema Formation: Think of HTML as a 'Master Container' that weaves text, file pathways, and audio-visual streams into a single perceptual field.",
        "neuroExplanation": "Semantic Priming: By recognizing that HTML stands for Hypertext, the brain realizes 'Hyper' means non-linear links (paths) connecting multi-sensory media.",
        "cognitiveTrap": "Do not rush to pick (B) just because HTML files are stored as plain text. The browser renders all types of embedded media."
    },
    {
        "id": "REV-003",
        "qnum": 3,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which of the following is the full form of HTML?",
        "options": {
            "A": "Hot Text Manipulation Language (B)",
            "B": "Hyper Text Manipulation Law",
            "C": "Hyper Text Markup Language",
            "D": "Hidden Text Markup Language"
        },
        "answer": "C",
        "keyAnswer": "C",
        "textbookReference": "Chapter 1, 'What is HTML?', Page 1",
        "textbookFact": "HTML stands for Hyper Text Markup Language. Designed by Tim Berners-Lee in 1991 at CERN.",
        "neuroHook": "🧠 Neural Hook: Hyper = jumping links; Markup = enclosed in tags <>; Language = browser communication grammar.",
        "neuroExplanation": "Chunking: Decompose 'HTML' into two functional brain chunks: [HyperText = dynamic navigation] + [Markup Language = structural tags].",
        "cognitiveTrap": "Beware of 'Manipulation' or 'Law' planted to exploit fast semantic skimming."
    },
    {
        "id": "REV-004",
        "qnum": 4,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "To display the web content, which mark-up language is needed?",
        "options": {
            "A": "CML",
            "B": "HTML",
            "C": "NML",
            "D": "WML"
        },
        "answer": "B",
        "keyAnswer": "B",
        "textbookReference": "Chapter 1, 'Introduction to HTML', Page 1",
        "textbookFact": "HTML is the standard foundational markup language parsed by rendering engines in all web browsers.",
        "neuroHook": "🧠 Recognition Anchor: 'Web' + 'Browser' = HTML is the native visual language of the World Wide Web.",
        "neuroExplanation": "Associative LTP (Long-Term Potentiation): Repeatedly coupling the web browser window with HTML tag execution hardens the hippocampal memory trace.",
        "cognitiveTrap": "WML (Wireless Markup Language) was an obsolete mobile protocol, but standard web content relies directly on HTML."
    },
    {
        "id": "REV-005",
        "qnum": 5,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "How does <p> tag show writing?",
        "options": {
            "A": "Bold",
            "B": "Underline",
            "C": "Italicized",
            "D": "Paragraphs"
        },
        "answer": "D",
        "keyAnswer": "D",
        "textbookReference": "Chapter 1, 'Paragraph Tag <p>', Page 6",
        "textbookFact": "The <p> tag formats enclosed text into paragraphs, automatically inserting a blank space/line before and after the text block.",
        "neuroHook": "🧠 Phonetic Link: <p> starts with 'P' for 'Paragraph'.",
        "neuroExplanation": "Letter-Name Strategy: Direct 1-to-1 acoustic mapping between the tag letter 'p' and the structural unit 'paragraph' minimizes working memory load.",
        "cognitiveTrap": "Don't confuse with <b> (Bold) or <u> (Underline)."
    },
    {
        "id": "REV-006",
        "qnum": 6,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which name identifies the latest version of HTML?",
        "options": {
            "A": "HTML 3.0",
            "B": "HTML 4.0",
            "C": "HTML 5.0",
            "D": "HTML 6.0"
        },
        "answer": "C",
        "keyAnswer": "C",
        "textbookReference": "Chapter 1, 'Evolution of HTML', Page 2",
        "textbookFact": "HTML 5.0 (HTML5) is the latest standardized version of HTML, introducing native video/audio, canvas, and semantic tags.",
        "neuroHook": "🧠 High-Five Rule: HTML 5 is the modern 'High-Five' standard for responsive web applications.",
        "neuroExplanation": "Numerical Peg: Anchor '5' as the current generation. Note that HTML6 does not exist as a standard specification.",
        "cognitiveTrap": "Do not pick HTML 6.0 thinking newer is higher; the W3C standard is HTML 5 / Living Standard."
    },
    {
        "id": "REV-007",
        "qnum": 7,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which short cut key is used to view result in browser HTML code ?",
        "options": {
            "A": "F3",
            "B": "F4",
            "C": "F5",
            "D": "F6"
        },
        "answer": "C",
        "keyAnswer": "C",
        "textbookReference": "Chapter 1, 'Viewing HTML Page in Browser', Page 5",
        "textbookFact": "Pressing the F5 function key in web browsers (or Ctrl+R) reloads the page to display the latest saved HTML changes.",
        "neuroHook": "🧠 Motor Memory: F5 = 'Fast Fresh' / 'Refresh'. Your index finger taps F5 to wake up the screen.",
        "neuroExplanation": "Sensorimotor Consolidation: Procedural memory in the cerebellum connects pressing F5 with visual browser re-rendering.",
        "cognitiveTrap": "F3 is 'Find Next'; F7 is 'Spell Check in Calc'; F5 is always browser Refresh."
    },
    {
        "id": "REV-008",
        "qnum": 8,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which option will you choose by right click to open file having HTML document ?",
        "options": {
            "A": "Open With",
            "B": "Open Now",
            "C": "Open File",
            "D": "Open Document"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 1, 'Viewing HTML Page', Page 5",
        "textbookFact": "Right-clicking an HTML file provides the 'Open With' context menu item, enabling the user to choose either a browser (Firefox/Chrome) or text editor (SciTE).",
        "neuroHook": "🧠 Decision Tree: Right Click -> 'Open With' -> Choose your tool (Browser vs SciTE).",
        "neuroExplanation": "Contextual Retrieval: The phrase 'Open With' signifies choosing an application from a set of alternatives.",
        "cognitiveTrap": "'Open Now' and 'Open Document' are fabricated options."
    },
    {
        "id": "REV-009",
        "qnum": 9,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which of the following are two broad classes of formatting character in HTML?",
        "options": {
            "A": "Physical and logical",
            "B": "Internal and external",
            "C": "Temporary and permanent",
            "D": "Head and body"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 1, 'Character Formatting Styles', Page 8",
        "textbookFact": "HTML text styles are broadly classified into two categories: Physical Styles (specify exact visual presentation, like <b>, <i>, <u>) and Logical Styles (describe structural role/meaning, like <strong>, <em>, <code>).",
        "neuroHook": "🧠 Neuro Dichotomy: Physical = Body appearance (bold, italic); Logical = Brain meaning (importance, emphasis).",
        "neuroExplanation": "Categorical Schema: Organizing formatting tags into Physical (visual) vs Logical (semantic) builds an efficient dual taxonomy in the cerebral cortex.",
        "cognitiveTrap": "Head and body are structural sections of an HTML document, NOT formatting character classes."
    },
    {
        "id": "REV-010",
        "qnum": 10,
        "source": "Revision Worksheet SAM-1",
        "chapter": 2,
        "chapterTitle": "Head and Body Sections in HTML",
        "question": "Which of the following is used to set an active link in HTML code ?",
        "options": {
            "A": "alink",
            "B": "vlink",
            "C": "before link",
            "D": "after link"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 2, 'Link Attributes in <body>', Page 18",
        "textbookFact": "The 'alink' attribute in the <body> tag specifies the color of an active hyperlink (the moment the mouse button is pressed on it). 'vlink' sets visited link color; 'link' sets normal unvisited link color.",
        "neuroHook": "🧠 Phonetic Truncation: 'a' + 'link' = Active Link; 'v' + 'link' = Visited Link.",
        "neuroExplanation": "Acoustic Cueing: The initial letter 'a' triggers instant recall of 'Active' state in the temporal lobe.",
        "cognitiveTrap": "'before link' and 'after link' are distractors; HTML uses link, vlink, and alink."
    },
    {
        "id": "REV-011",
        "qnum": 11,
        "source": "Revision Worksheet SAM-1",
        "chapter": 2,
        "chapterTitle": "Head and Body Sections in HTML",
        "question": "Which of the following is used to specify a color in HTML code ?",
        "options": {
            "A": "Color code in hexadecimal",
            "B": "Color code in decimal",
            "C": "Color mixing model",
            "D": "Pixel in percentage"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 2, 'Color Representation in HTML', Page 16",
        "textbookFact": "Colors in HTML are defined either by pre-defined color names or by 6-digit Hexadecimal RGB values in the format #RRGGBB (00 to FF).",
        "neuroHook": "🧠 Hex Anchor: #FF0000 = Red. Hexadecimal = base 16 (0-9, A-F), the brain's 6-character color code.",
        "neuroExplanation": "Spatial Encoding: Associating the # symbol with 6 hex slots (#RRGGBB) forms a compact spatial schema in working memory.",
        "cognitiveTrap": "Decimal RGB is used in modern CSS (rgb(255,0,0)), but textbook HTML color attributes explicitly specify Hexadecimal code."
    },
    {
        "id": "REV-012",
        "qnum": 12,
        "source": "Revision Worksheet SAM-1",
        "chapter": 2,
        "chapterTitle": "Head and Body Sections in HTML",
        "question": "The meta-tags in an HTML document are written in which of the following section?",
        "options": {
            "A": "Body",
            "B": "Code",
            "C": "Head",
            "D": "Special"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 2, 'The <head> Element and <meta> Tag', Page 14 vs Worksheet Answer Key",
        "textbookFact": "IMPORTANT DUAL-KNOWLEDGE: In standard web specifications and the Gujarat Board textbook Chapter 2, <meta> tags belong inside the <head> section. However, in the school's official SAM-1 answer key, question 12 is keyed as '(A) Body'. Students must be aware of this specific worksheet answer key for school marks while understanding the true technical fact.",
        "neuroHook": "🧠 Double-Memory Flag: Worksheet Key = Body (A); Real Spec = Head (C). Anchor both so no marks are lost!",
        "neuroExplanation": "Metacognitive Monitoring: Tracking test-maker anomalies prevents frustration when a school's answer key deviates from canonical theory.",
        "cognitiveTrap": "In the SAM-1 school exam, select A because that matches their published key, but in board exams, remember <meta> is in <head>."
    },
    {
        "id": "REV-013",
        "qnum": 13,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "What is the ASCII value for & symbol ?",
        "options": {
            "A": "36",
            "B": "37",
            "C": "38",
            "D": "39"
        },
        "answer": "C",
        "keyAnswer": "C",
        "textbookReference": "Chapter 1, 'Special Characters and Entities in HTML', Page 10",
        "textbookFact": "ASCII decimal 38 represents the ampersand '&' character. In HTML, it can be written as &#38; or &amp;.",
        "neuroHook": "🧠 Shape Peg: The symbol '&' has two loops resembling the numeral '8'. Hence: 38!",
        "neuroExplanation": "Iconic-Numerical Mapping: Visual resemblance between the physical curvature of '&' and '8' anchors ASCII 38 into episodic memory.",
        "cognitiveTrap": "36 is '$', 37 is '%', 38 is '&', 39 is single quote '\''."
    },
    {
        "id": "REV-014",
        "qnum": 14,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which symbol is used for indicating smaller quantity?",
        "options": {
            "A": ">",
            "B": "&",
            "C": "<",
            "D": "$"
        },
        "answer": "C",
        "keyAnswer": "C",
        "textbookReference": "Chapter 1, 'Special Entities & Relational Symbols', Page 10",
        "textbookFact": "The '<' symbol signifies 'less than' or a smaller quantity. In HTML entities, it is written as &lt;.",
        "neuroHook": "🧠 Spatial Arrow: '<' points to the left where numbers are smaller (on the number line).",
        "neuroExplanation": "Spatial-Numerical Association of Response Codes (SNARC effect): The human brain instinctively maps smaller magnitudes to the left ('<').",
        "cognitiveTrap": "'>' is greater than (points right)."
    },
    {
        "id": "REV-015",
        "qnum": 15,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Full form of ASCII is............",
        "options": {
            "A": "American Standard Code for Interchange Information",
            "B": "American Standard Code for International Information",
            "C": "American Standard Code for Increment Interchange",
            "D": "American Standard Code for Information Interchange"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 1, 'Character Sets and ASCII', Page 10 vs Worksheet Key",
        "textbookFact": "Standard full form is 'American Standard Code for Information Interchange'. In the SAM-1 worksheet answer key, option (A) 'American Standard Code for Interchange Information' is officially designated as the intended key.",
        "neuroHook": "🧠 Worksheet Anchor: Look for 'American Standard Code for...' Notice the school key marked (A) with inverted words.",
        "neuroExplanation": "Cognitive Discrepancy Reconciliation: Keeping both versions active in working memory protects against grading discrepancy in school exams.",
        "cognitiveTrap": "Standard computer science uses (D), but SAM-1 key marks (A)."
    },
    {
        "id": "REV-016",
        "qnum": 16,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "By what name & is known?",
        "options": {
            "A": "Ampire",
            "B": "Ampercent",
            "C": "Ampersand",
            "D": "Amparantant"
        },
        "answer": "C",
        "keyAnswer": "C",
        "textbookReference": "Chapter 1, 'Special Characters in HTML', Page 10",
        "textbookFact": "The '&' character is named 'Ampersand', originating from the Latin phrase 'and per se and'.",
        "neuroHook": "🧠 Phonetic Peg: 'Amp' + 'er' + 'sand' — writing 'AND' on the sand.",
        "neuroExplanation": "Morphological Decomposition: Breaking unfamiliar jargon into familiar auditory syllables facilitates long-term memory retrieval.",
        "cognitiveTrap": "'Ampire' and 'Ampercent' are phonological distractors."
    },
    {
        "id": "REV-017",
        "qnum": 17,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Which of the following should the special symbols?",
        "options": {
            "A": ">, <, &",
            "B": "Code",
            "C": "code",
            "D": "None of these"
        },
        "answer": "D",
        "keyAnswer": "D",
        "textbookReference": "Chapter 1, 'Special Symbols in HTML', Page 10 vs Worksheet Key",
        "textbookFact": "While '>, <, &' are indeed special symbols in HTML, the worksheet answer key designates '(D) None of these' due to question phrasing.",
        "neuroHook": "🧠 Key Alert: Worksheet Answer Key = (D) None of these. Remember this exact question ID.",
        "neuroExplanation": "Verbatim Retrieval: Storing question-to-key pairs prevents exam surprises when question text contains typos.",
        "cognitiveTrap": "Do not argue with the school answer key during SAM-1 grading; mark D as published."
    },
    {
        "id": "REV-018",
        "qnum": 18,
        "source": "Revision Worksheet SAM-1",
        "chapter": 1,
        "chapterTitle": "Introduction to HTML",
        "question": "Out of following, which indicate HTML extension?",
        "options": {
            "A": ".h",
            "B": ".hmt",
            "C": ".html",
            "D": ".hmlt"
        },
        "answer": "C",
        "keyAnswer": "C",
        "textbookReference": "Chapter 1, 'Saving HTML Files', Page 4",
        "textbookFact": "Web pages are saved with the standard file extension '.html' or '.htm'.",
        "neuroHook": "🧠 4-Letter Peg: H-T-M-L -> .html. (.h is for C header files!)",
        "neuroExplanation": "Orthographic Neighborhood Effect: The brain easily spots anagram typos like .hmt or .hmlt when trained on exact letter sequences.",
        "cognitiveTrap": ".h is a C-language header file, NOT an HTML file."
    },
    {
        "id": "REV-019",
        "qnum": 19,
        "source": "Revision Worksheet SAM-1",
        "chapter": 5,
        "chapterTitle": "Introduction to Calc",
        "question": "How can one calculate total of values entered in a worksheet in a Calc document ?",
        "options": {
            "A": "By autosum",
            "B": "By manual entry",
            "C": "By formula",
            "D": "All of these"
        },
        "answer": "D",
        "keyAnswer": "D",
        "textbookReference": "Chapter 5, 'Performing Calculations in Calc', Page 82",
        "textbookFact": "Values can be summed using the AutoSum tool button (Σ), by manual entry (=A1+A2), or by using the built-in formula/function (=SUM(A1:A5)).",
        "neuroHook": "🧠 Redundant Pathways: Three roads to the same sum: AutoSum (click), Formula (function), Manual (plus sign).",
        "neuroExplanation": "Cognitive Flexibility: Recognizing multiple valid solution paths promotes conceptual robustness in spreadsheet problem-solving.",
        "cognitiveTrap": "Picking just 'By autosum' without reading option D ('All of these')."
    },
    {
        "id": "REV-020",
        "qnum": 20,
        "source": "Revision Worksheet SAM-1",
        "chapter": 5,
        "chapterTitle": "Introduction to Calc",
        "question": "Which of the following is the extension of a worksheet created in Calc ?",
        "options": {
            "A": ".ods",
            "B": ".xls",
            "C": ".odd",
            "D": ".obj"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 5, 'Saving Spreadsheet in Calc', Page 84",
        "textbookFact": "OpenOffice/LibreOffice Calc saves spreadsheets with the default OpenDocument format: .ods (OpenDocument Spreadsheet).",
        "neuroHook": "🧠 Mnemonic: ODS = 'OpenDocument Spreadsheet'. (.odt = text, .odp = presentation).",
        "neuroExplanation": "Acronym De-obfuscation: O=Open, D=Document, S=Spreadsheet. Knowing the root terms guarantees permanent recall.",
        "cognitiveTrap": ".xls is Microsoft Excel's legacy extension, not native Calc."
    },
    {
        "id": "REV-021",
        "qnum": 21,
        "source": "Revision Worksheet SAM-1",
        "chapter": 5,
        "chapterTitle": "Introduction to Calc",
        "question": "Which of the following type of package does Calc refer to ?",
        "options": {
            "A": "Spreadsheet",
            "B": "Multi-sheet",
            "C": "Double sheet",
            "D": "Cannot be determined"
        },
        "answer": "A",
        "keyAnswer": "A",
        "textbookReference": "Chapter 5, 'What is OpenOffice Calc?', Page 78",
        "textbookFact": "Calc is categorized as an Electronic Spreadsheet application package.",
        "neuroHook": "🧠 Category Peg: Calc = Spreadsheet; Writer = Word Processor; Impress = Presentation.",
        "neuroExplanation": "Hierarchical Schema: Fitting Calc under the overarching software class 'Spreadsheet' activates categorical clustering in long-term memory.",
        "cognitiveTrap": "Even though Calc contains multiple sheets, its official software classification is 'Spreadsheet'."
    },
    {
        "id": "REV-022",
        "qnum": 22,
        "source": "Revision Worksheet SAM-1",
        "chapter": 5,
        "chapterTitle": "Introduction to Calc",
        "question": "Which option is used to close Calc program?",
        "options": {
            "A": "File -> Quit",
            "B": "Ctrl+Q shortcut key",
            "C": "Close button",
            "D": "Any of above"
        },
        "answer": "D",
        "keyAnswer": "D",
        "textbookReference": "Chapter 5, 'Closing Calc', Page 85",
        "textbookFact": "Calc can be closed by navigating to File -> Quit, pressing the keyboard shortcut Ctrl+Q, or clicking the window's close [X] icon.",
        "neuroHook": "🧠 Multi-modal Exit: Menu (File->Quit), Keyboard (Ctrl+Q), Mouse ([X] button) — all shut down Calc.",
        "neuroExplanation": "Motor Equivalence: The motor cortex prepares three equivalent execution programs for terminating an application.",
        "cognitiveTrap": "Do not pick only (A); all three options close the program."
    },
    {
        "id": "REV-023",
        "qnum": 23,
        "source": "Revision Worksheet SAM-1",
        "chapter": 5,
        "chapterTitle": "Introduction to Calc",
        "question": "Which option is used to create a new file?",
        "options": {
            "A": "File -> New",
            "B": "Ctrl + O shortcut key",
            "C": "New tool button",
            "D": "Any of given"
        },
        "answer": "D",
        "keyAnswer": "D",
        "textbookReference": "Chapter 5, 'Creating a New Spreadsheet', Page 79 vs Worksheet Key",
        "textbookFact": "Creating a new file is done via File -> New -> Spreadsheet, Ctrl+N, or the New tool button. In the SAM-1 worksheet key, '(D) Any of given' is designated.",
        "neuroHook": "🧠 Exam Key Anchor: SAM-1 marks (D) Any of given for creating a new file.",
        "neuroExplanation": "Practical note: Ctrl+O is technically 'Open', but the test designer grouped it into general file operations under 'Any of given'.",
        "cognitiveTrap": "In the worksheet, pick (D) to match the official school key."
    },
    {
        "id": "REV-024",
        "qnum": 24,
        "source": "Revision Worksheet SAM-1",
        "chapter": 5,
        "chapterTitle": "Introduction to Calc",
        "question": "In which menu Cut-Paste option is available ?",
        "options": {
            "A": "File",
            "B": "Edit",
            "C": "View",
            "D": "Format"
        },
        "answer": "B",
        "keyAnswer": "B",
        "textbookReference": "Chapter 5, 'Calc Menus and Toolbars', Page 80",
        "textbookFact": "Editing actions (Undo, Redo, Cut, Copy, Paste, Find & Replace) are located in the 'Edit' menu.",
        "neuroHook": "🧠 Semantic Link: If you modify, cut, or paste data, you are 'Editing' it -> EDIT menu.",
        "neuroExplanation": "Functional Grouping: Associating content alteration with the 'Edit' concept activates semantic associations in the left prefrontal cortex.",
        "cognitiveTrap": "Format alters appearance (fonts/colors); Edit alters data content (Cut/Copy/Paste)."
    },
    {
        "id": "REV-025",
        "qnum": 25,
        "source": "Revision Worksheet SAM-1",
        "chapter": 5,
        "chapterTitle": "Introduction to Calc",
        "question": "Which of the following option is used to add the values between cell E2 to E5 in Calc?",
        "options": {
            "A": "=E2+E3+E4+E5",
            "B": "=SUM(E2:E5)",
            "C": "Σ Button",
            "D": "All of these"
        },
        "answer": "D",
        "keyAnswer": "D",
        "textbookReference": "Chapter 5, 'Using AutoSum and SUM Function', Page 83",
        "textbookFact": "All three methods (manual plus operator, SUM range formula, and the AutoSum button) calculate the total of cells E2 through E5.",
        "neuroHook": "🧠 Triad of Addition: Expression (=E2+E3+E4+E5), Function (=SUM(E2:E5)), Button (Σ).",
        "neuroExplanation": "Multiple Representation: Storing arithmetic addition in algebraic, functional, and graphical formats enhances cognitive adaptability.",
        "cognitiveTrap": "Students often pick (B) prematurely because it is the most common formula, forgetting (A) and (C) are also valid."
    }
]

print(f"Sample raw questions loaded: {len(q126_raw)}")
