# -*- coding: utf-8 -*-
"""
Textbook Chapter Exercises Builder (Chapters 1 to 14)
GSEB Class 10 Computer Studies English Medium
"""
import json

def get_textbook_exercises():
    tb_questions = [
        # Chapter 1: Introduction to HTML
        {
            "id": "TB-CH01-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "Which of the following refers to a language designed for creating web pages?",
            "options": {"A": "C", "B": "C++", "C": "HTML", "D": "Java"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 1, Page 1",
            "textbookFact": "HTML (HyperText Markup Language) is specifically designed to create and structure web pages.",
            "neuroHook": "🧠 HTML is the skeleton and skin of every web page on the internet.",
            "neuroExplanation": "Domain categorization: C/C++/Java are general-purpose compiled programming languages, whereas HTML is the markup language of the web.",
            "cognitiveTrap": "Do not confuse programming languages (C/Java) with markup languages (HTML)."
        },
        {
            "id": "TB-CH01-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "Which of the following tag is used to create a line break in an HTML document?",
            "options": {"A": "<lb>", "B": "<break>", "C": "<br>", "D": "<line>"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 1, Page 6",
            "textbookFact": "The <br> tag inserts a single line break without creating an empty paragraph spacing.",
            "neuroHook": "🧠 <br> = BReak the line.",
            "neuroExplanation": "Phonetic abbreviation: 'br' triggers instant semantic recall of 'break'.",
            "cognitiveTrap": "<break> and <lb> do not exist in HTML."
        },
        {
            "id": "TB-CH01-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "How many levels of headings does HTML provide?",
            "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
            "answer": "D", "keyAnswer": "D",
            "textbookReference": "Chapter 1, Page 5",
            "textbookFact": "HTML provides exactly 6 levels of headings: <h1> (largest) down to <h6> (smallest).",
            "neuroHook": "🧠 Headings 1 through 6: <h1> is huge; <h6> is tiny.",
            "neuroExplanation": "Numerical hierarchy: 1 is top tier (largest), 6 is base tier (smallest).",
            "cognitiveTrap": "Thinking h1 is smallest because 1 is low number; in HTML, <h1> is largest."
        },
        {
            "id": "TB-CH01-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "Which tag is used to display a horizontal dividing rule across a page?",
            "options": {"A": "<line>", "B": "<hr>", "C": "<hl>", "D": "<rule>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 1, Page 7",
            "textbookFact": "The <hr> tag draws a Horizontal Rule (divider line) across the screen.",
            "neuroHook": "🧠 <hr> = Horizontal Rule.",
            "neuroExplanation": "Two-letter mnemonic: 'h' for Horizontal, 'r' for Rule.",
            "cognitiveTrap": "<line> and <hl> are incorrect guesses."
        },
        {
            "id": "TB-CH01-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "Which of the following is an example of an empty tag?",
            "options": {"A": "<b>", "B": "<p>", "C": "<br>", "D": "<html>"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 1, Page 6",
            "textbookFact": "<br> and <hr> are standalone/empty tags because they do not enclose text and require no closing tag.",
            "neuroHook": "🧠 Empty tags have no closing partner: <br> and <hr> fly solo.",
            "neuroExplanation": "Solitary token category: Identifying tags lacking closing counter-tokens.",
            "cognitiveTrap": "<b>, <p>, and <html> must all be closed."
        },
        {
            "id": "TB-CH01-06", "qnum": 6, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "What is the entity name used to display the '&' character on a web page?",
            "options": {"A": "&and;", "B": "&amp;", "C": "&persand;", "D": "&et;"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 1, Page 10",
            "textbookFact": "In HTML entity encoding, '&' is represented as &amp; (or &#38;).",
            "neuroHook": "🧠 &amp; = AMPersand entity.",
            "neuroExplanation": "Entity syntax template: & + name + ;",
            "cognitiveTrap": "&and; is not valid; use &amp;."
        },
        {
            "id": "TB-CH01-07", "qnum": 7, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "Which tag makes text appear as a superscript (e.g. x²)?",
            "options": {"A": "<sub>", "B": "<sup>", "C": "<super>", "D": "<pow>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 1, Page 9",
            "textbookFact": "<sup> stands for Superscript, raising characters above the baseline (e.g., 10<sup>th</sup>).",
            "neuroHook": "🧠 SUPER-man flies UP -> <sup>. SUB-marine dives DOWN -> <sub>.",
            "neuroExplanation": "Spatial semantic contrast between Super (above) and Sub (below).",
            "cognitiveTrap": "Do not confuse with <sub> (subscript for H₂O)."
        },
        {
            "id": "TB-CH01-08", "qnum": 8, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "Which of the following character formatting tags is a logical style tag?",
            "options": {"A": "<b>", "B": "<i>", "C": "<u>", "D": "<strong>"},
            "answer": "D", "keyAnswer": "D",
            "textbookReference": "Chapter 1, Page 8",
            "textbookFact": "<strong> and <em> are logical styles indicating importance, whereas <b>, <i>, <u> are physical styles.",
            "neuroHook": "🧠 Logical = Meaning (Strong / Emphasized); Physical = Font shape (Bold / Italic).",
            "neuroExplanation": "Semantics vs Presentation in modern computing cognitive models.",
            "cognitiveTrap": "<b> and <strong> look the same, but <strong> is logical."
        },
        {
            "id": "TB-CH01-09", "qnum": 9, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "What is the entity code to display a non-breaking blank space in HTML?",
            "options": {"A": "&space;", "B": "&blank;", "C": "&nbsp;", "D": "&sp;"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 1, Page 10",
            "textbookFact": "&nbsp; stands for Non-Breaking SPace and prevents automatic word wrapping while inserting a space.",
            "neuroHook": "🧠 &nbsp; = Non-Breaking SPace.",
            "neuroExplanation": "Acronym expansion: N-B-SP.",
            "cognitiveTrap": "&space; is invalid HTML."
        },
        {
            "id": "TB-CH01-10", "qnum": 10, "source": "Textbook Exercise", "chapter": 1, "chapterTitle": "Chapter 1: Introduction to HTML",
            "question": "Which application is used to view the rendered output of an HTML document?",
            "options": {"A": "Text Editor", "B": "Web Browser", "C": "Compiler", "D": "Assembler"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 1, Page 5",
            "textbookFact": "Web browsers (such as Mozilla Firefox, Google Chrome) parse and visually render HTML documents.",
            "neuroHook": "🧠 Editor creates code; Browser views the finished web page.",
            "neuroExplanation": "Tool specialization in software workflow.",
            "cognitiveTrap": "SciTE edits code; Browser displays output."
        },

        # Chapter 2: Head and Body Sections in HTML
        {
            "id": "TB-CH02-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "Which tag is used to specify metadata such as keywords and description in an HTML document?",
            "options": {"A": "<title>", "B": "<meta>", "C": "<head>", "D": "<base>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 2, Page 14",
            "textbookFact": "The <meta> tag inside <head> specifies author, description, and keywords for search engines.",
            "neuroHook": "🧠 Meta = Information about information.",
            "neuroExplanation": "Meta-cognitive awareness: Storing descriptive metadata.",
            "cognitiveTrap": "<title> defines window title; <meta> defines search metadata."
        },
        {
            "id": "TB-CH02-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "Which attribute of the <body> tag is used to set the background color of a web page?",
            "options": {"A": "color", "B": "bg", "C": "bgcolor", "D": "background"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 2, Page 16",
            "textbookFact": "The 'bgcolor' attribute sets background color; 'background' sets a background image.",
            "neuroHook": "🧠 BG-COLOR = BackGround COLOR; BACKGROUND = BackGround Image.",
            "neuroExplanation": "Distinct lexical targets for solid color vs bitmap graphics.",
            "cognitiveTrap": "Do not confuse bgcolor (for color) with background (for image path)."
        },
        {
            "id": "TB-CH02-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "Which attribute of <body> is used to set an image as the page background?",
            "options": {"A": "image", "B": "src", "C": "background", "D": "bgimg"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 2, Page 17",
            "textbookFact": "<body background=\"image.jpg\"> sets the image as tiled background.",
            "neuroHook": "🧠 Background = Image File Wallpaper.",
            "neuroExplanation": "Attribute binding with file URL strings.",
            "cognitiveTrap": "src is used in <img>, background is used in <body>."
        },
        {
            "id": "TB-CH02-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "What is the correct syntax for adding a comment in HTML?",
            "options": {"A": "// comment", "B": "/* comment */", "C": "<!-- comment -->", "D": "# comment"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 2, Page 15",
            "textbookFact": "HTML comments are delimited by <!-- at the start and --> at the end.",
            "neuroHook": "🧠 <!-- Shhh, browser won't read this! -->",
            "neuroExplanation": "Exclamation mark (!) alerts the parser to an instruction/comment block.",
            "cognitiveTrap": "// is C/C++/JavaScript; /* */ is CSS/C; <!-- --> is HTML."
        },
        {
            "id": "TB-CH02-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "Which attribute sets the default color of visited hyperlinks?",
            "options": {"A": "link", "B": "vlink", "C": "alink", "D": "visited"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 2, Page 18",
            "textbookFact": "'vlink' in <body> sets the color of Visited Links (default is purple).",
            "neuroHook": "🧠 'v' for Visited link.",
            "neuroExplanation": "Letter cueing: v = Visited, a = Active, link = normal.",
            "cognitiveTrap": "'alink' is active link (mouse down)."
        },
        {
            "id": "TB-CH02-06", "qnum": 2, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "What are the default margins (leftmargin and topmargin) measured in?",
            "options": {"A": "Inches", "B": "Centimeters", "C": "Pixels", "D": "Points"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 2, Page 18",
            "textbookFact": "HTML body margins (leftmargin, topmargin) are measured in screen pixels.",
            "neuroHook": "🧠 Screen dots = Pixels (the atom of computer displays).",
            "neuroExplanation": "Physical screen coordinate space is always pixel-based.",
            "cognitiveTrap": "Paper printing uses inches/cm, but web displays use pixels."
        },
        {
            "id": "TB-CH02-07", "qnum": 7, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "Which tag is used to provide anchor links between documents or sections?",
            "options": {"A": "<link>", "B": "<a>", "C": "<href>", "D": "<url>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 2, Page 18",
            "textbookFact": "The <a> (Anchor) tag creates hyperlinks via its 'href' attribute.",
            "neuroHook": "🧠 <a> = ANCHOR linking two shores together.",
            "neuroExplanation": "Nautical anchor metaphor for securing a link to a remote address.",
            "cognitiveTrap": "<href> is an attribute, not a tag; <link> is for external CSS."
        },
        {
            "id": "TB-CH02-08", "qnum": 8, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "In the hexadecimal color code #00FF00, which color is fully saturated?",
            "options": {"A": "Red", "B": "Green", "C": "Blue", "D": "White"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 2, Page 16",
            "textbookFact": "#RRGGBB format: RR=00 (no red), GG=FF (maximum green), BB=00 (no blue) = Pure Green.",
            "neuroHook": "🧠 RGB Order: Red (slot 1), Green (slot 2), Blue (slot 3). Slot 2 has FF = Full Green!",
            "neuroExplanation": "Tristimulus color representation mapped to visual cone photoreceptors.",
            "cognitiveTrap": "#FF0000 is Red; #00FF00 is Green; #0000FF is Blue."
        },
        {
            "id": "TB-CH02-09", "qnum": 9, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "Which of the following is the default text color in a web page when not specified?",
            "options": {"A": "Blue", "B": "Black", "C": "Red", "D": "Gray"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 2, Page 16",
            "textbookFact": "The standard default body text color is Black (#000000) on a White background.",
            "neuroHook": "🧠 Classic High Contrast: Black ink on white paper.",
            "neuroExplanation": "Luminance contrast maximizes foveal reading acuity.",
            "cognitiveTrap": "Blue is default for links, NOT body text."
        },
        {
            "id": "TB-CH02-10", "qnum": 10, "source": "Textbook Exercise", "chapter": 2, "chapterTitle": "Chapter 2: Head and Body Sections in HTML",
            "question": "Which tag sets a base URL for all relative links in an HTML document?",
            "options": {"A": "<base>", "B": "<baseurl>", "C": "<url>", "D": "<link>"},
            "answer": "A", "keyAnswer": "A",
            "textbookReference": "Chapter 2, Page 14",
            "textbookFact": "The <base> tag in <head> establishes the base URL for all relative references in the document.",
            "neuroHook": "🧠 <base> = Home base for all relative links.",
            "neuroExplanation": "Root anchor node in tree traversal.",
            "cognitiveTrap": "<baseurl> is not a valid HTML tag."
        },

        # Chapter 3: Handling Images in HTML
        {
            "id": "TB-CH03-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which tag is used to insert an image into an HTML page?",
            "options": {"A": "<image>", "B": "<img>", "C": "<pic>", "D": "<picture>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 3, Page 24",
            "textbookFact": "The <img> tag is an empty tag used to embed raster and vector images.",
            "neuroHook": "🧠 <img> = IMaGe tag.",
            "neuroExplanation": "Trigram abbreviation in HTML grammar.",
            "cognitiveTrap": "<image> is invalid in HTML4/5."
        },
        {
            "id": "TB-CH03-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which attribute of <img> specifies the path and filename of the image?",
            "options": {"A": "href", "B": "url", "C": "src", "D": "link"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 3, Page 24",
            "textbookFact": "'src' (Source) specifies the URL of the image file to load.",
            "neuroHook": "🧠 'src' = SouRCe of the picture.",
            "neuroExplanation": "Source binding in image rendering pipeline.",
            "cognitiveTrap": "href is for <a> anchors; src is for <img>."
        },
        {
            "id": "TB-CH03-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which attribute provides alternate text if the image fails to load?",
            "options": {"A": "title", "B": "alt", "C": "text", "D": "desc"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 3, Page 25",
            "textbookFact": "'alt' (Alternative Text) displays placeholder text for accessibility and broken images.",
            "neuroHook": "🧠 'alt' = ALTernate text backup.",
            "neuroExplanation": "Fault tolerance schema: fallback text for sensory impaired users.",
            "cognitiveTrap": "title shows a tooltip, alt is the true alternative text."
        },
        {
            "id": "TB-CH03-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which image format supports animations?",
            "options": {"A": "JPEG", "B": "BMP", "C": "GIF", "D": "TIFF"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 3, Page 26",
            "textbookFact": "GIF (Graphics Interchange Format) supports up to 256 colors and multi-frame animation.",
            "neuroHook": "🧠 GIF = Moving picture loop.",
            "neuroExplanation": "Temporal frame sequencing encoded in GIF header format.",
            "cognitiveTrap": "JPEG is for photographic stills and does not support animation."
        },
        {
            "id": "TB-CH03-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which image format is best suited for real-life photographs?",
            "options": {"A": "GIF", "B": "JPEG", "C": "BMP", "D": "XBM"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 3, Page 26",
            "textbookFact": "JPEG (Joint Photographic Experts Group) supports 16.7 million colors with lossy compression, ideal for photos.",
            "neuroHook": "🧠 JPEG = Photo Champion (millions of natural colors).",
            "neuroExplanation": "Discrete Cosine Transform (DCT) aligns with human visual perception falloff.",
            "cognitiveTrap": "GIF is limited to 256 colors, causing banding on photos."
        },
        {
            "id": "TB-CH03-06", "qnum": 6, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which attributes control the rendered width and height of an image?",
            "options": {"A": "size and length", "B": "width and height", "C": "x and y", "D": "w and h"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 3, Page 25",
            "textbookFact": "'width' and 'height' attributes define the dimensions in pixels or percentages.",
            "neuroHook": "🧠 Width (horizontal) + Height (vertical) = 2D bounding box.",
            "neuroExplanation": "2D Cartesian geometry bounding box in visual cortex.",
            "cognitiveTrap": "size is used in <font> or <input>, not <img>."
        },
        {
            "id": "TB-CH03-07", "qnum": 7, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which attribute adds empty vertical space above and below an image?",
            "options": {"A": "hspace", "B": "vspace", "C": "margin", "D": "pad"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 3, Page 27",
            "textbookFact": "'vspace' adds Vertical Space (top/bottom); 'hspace' adds Horizontal Space (left/right).",
            "neuroHook": "🧠 V-space = Vertical space; H-space = Horizontal space.",
            "neuroExplanation": "Spatial axis coordinates: V = Y-axis (top/bottom), H = X-axis (left/right).",
            "cognitiveTrap": "hspace is for left/right sides."
        },
        {
            "id": "TB-CH03-08", "qnum": 8, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which attribute adds a visible frame border around an image?",
            "options": {"A": "frame", "B": "outline", "C": "border", "D": "box"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 3, Page 28",
            "textbookFact": "<img border=\"2\"> draws a border with a thickness of 2 pixels around the image.",
            "neuroHook": "🧠 Border draws the frame.",
            "neuroExplanation": "Figure-ground segmentation cue.",
            "cognitiveTrap": "Border is the HTML attribute name."
        },
        {
            "id": "TB-CH03-09", "qnum": 9, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "What happens when an <img> tag is wrapped inside <a href=\"...\">...</a>?",
            "options": {"A": "Image becomes hidden", "B": "Image acts as a clickable hyperlink", "C": "Image is deleted", "D": "Image becomes animated"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 3, Page 29",
            "textbookFact": "Wrapping an image inside an anchor tag turns the picture into a clickable graphical hyperlink.",
            "neuroHook": "🧠 Clickable Picture = <a href><img></a>.",
            "neuroExplanation": "Affordance mapping: Visual object gains motor clickability.",
            "cognitiveTrap": "In older browsers, a blue border appeared around linked images unless border=0."
        },
        {
            "id": "TB-CH03-10", "qnum": 10, "source": "Textbook Exercise", "chapter": 3, "chapterTitle": "Chapter 3: Handling Images in HTML",
            "question": "Which modern image format supports alpha transparency and lossless compression?",
            "options": {"A": "BMP", "B": "PNG", "C": "TIFF", "D": "JPG"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 3, Page 26",
            "textbookFact": "PNG (Portable Network Graphics) was created to replace GIF, offering superior alpha transparency and lossless quality.",
            "neuroHook": "🧠 PNG = Crystal clear transparency without jagged edges.",
            "neuroExplanation": "Alpha channel variable opacity representation.",
            "cognitiveTrap": "JPEG does NOT support transparency."
        },

        # Chapter 4: Lists and Tables in HTML
        {
            "id": "TB-CH04-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which tag creates an ordered (numbered) list in HTML?",
            "options": {"A": "<ul>", "B": "<ol>", "C": "<nl>", "D": "<list>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 4, Page 35",
            "textbookFact": "<ol> stands for Ordered List (items numbered 1, 2, 3 or A, B, C).",
            "neuroHook": "🧠 <ol> = Ordered List; <ul> = Unordered List.",
            "neuroExplanation": "Phonetic abbreviation of structural concepts.",
            "cognitiveTrap": "<ul> uses bullet points without numbers."
        },
        {
            "id": "TB-CH04-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which tag defines an individual list item inside <ol> or <ul>?",
            "options": {"A": "<item>", "B": "<li>", "C": "<it>", "D": "<line>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 4, Page 35",
            "textbookFact": "<li> stands for List Item and defines each entry in ordered and unordered lists.",
            "neuroHook": "🧠 <li> = List Item.",
            "neuroExplanation": "Direct morphological acronym.",
            "cognitiveTrap": "<item> is not an HTML tag."
        },
        {
            "id": "TB-CH04-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "What is the default bullet type for an unordered list <ul>?",
            "options": {"A": "circle", "B": "square", "C": "disc", "D": "none"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 4, Page 37",
            "textbookFact": "The default bullet symbol in <ul> is 'disc' (solid filled circle).",
            "neuroHook": "🧠 Disc = Solid filled black circle.",
            "neuroExplanation": "Visual prototype for default list bullets.",
            "cognitiveTrap": "'circle' is hollow; 'disc' is the filled default."
        },
        {
            "id": "TB-CH04-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which tag is used to create a definition list?",
            "options": {"A": "<dl>", "B": "<ol>", "C": "<def>", "D": "<dict>"},
            "answer": "A", "keyAnswer": "A",
            "textbookReference": "Chapter 4, Page 38",
            "textbookFact": "<dl> defines a Definition List, containing <dt> (definition term) and <dd> (definition description).",
            "neuroHook": "🧠 <dl> = Definition List; <dt> = Term; <dd> = Description.",
            "neuroExplanation": "Trio schema for glossary/dictionary structures.",
            "cognitiveTrap": "<def> is Python syntax, not HTML."
        },
        {
            "id": "TB-CH04-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which tag defines a table row in an HTML table?",
            "options": {"A": "<td>", "B": "<th>", "C": "<tr>", "D": "<row>"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 4, Page 41",
            "textbookFact": "<tr> stands for Table Row and groups cells horizontally.",
            "neuroHook": "🧠 <tr> = Table Row.",
            "neuroExplanation": "Horizontal row vector representation.",
            "cognitiveTrap": "<td> is table data (cell), <tr> is the row."
        },
        {
            "id": "TB-CH04-06", "qnum": 6, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which tag defines a table header cell with centered, bold text?",
            "options": {"A": "<td>", "B": "<th>", "C": "<h1>", "D": "<tc>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 4, Page 41",
            "textbookFact": "<th> stands for Table Header; browsers display its text bold and centered by default.",
            "neuroHook": "🧠 <th> = Table Header (Bold + Centered).",
            "neuroExplanation": "Dual presentation defaults: visual weight (bold) + alignment (center).",
            "cognitiveTrap": "<td> text is regular weight and left-aligned."
        },
        {
            "id": "TB-CH04-07", "qnum": 7, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which attribute merges two or more columns into a single cell?",
            "options": {"A": "rowspan", "B": "colspan", "C": "cellmerge", "D": "colmerge"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 4, Page 45",
            "textbookFact": "'colspan' (Column Span) merges multiple columns horizontally into one cell.",
            "neuroHook": "🧠 Colspan = Spans across COLUMNS (horizontal bridge).",
            "neuroExplanation": "Spatial span across vertical grid boundaries.",
            "cognitiveTrap": "rowspan merges vertically across rows."
        },
        {
            "id": "TB-CH04-08", "qnum": 8, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which attribute sets the distance between the cell wall and its content?",
            "options": {"A": "cellspacing", "B": "cellpadding", "C": "border", "D": "margin"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 4, Page 43",
            "textbookFact": "'cellpadding' controls padding between cell borders and the inner text; 'cellspacing' sets space between adjacent cells.",
            "neuroHook": "🧠 Cell-PADDING = Soft cushion inside the cell. Cell-SPACING = Distance between cells.",
            "neuroExplanation": "Internal cushion (padding) vs external distance (spacing) tactile metaphor.",
            "cognitiveTrap": "Students frequently invert cellpadding and cellspacing."
        },
        {
            "id": "TB-CH04-09", "qnum": 9, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which tag provides an explanatory caption/title for a table?",
            "options": {"A": "<title>", "B": "<caption>", "C": "<summary>", "D": "<header>"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 4, Page 42",
            "textbookFact": "The <caption> tag must appear immediately after <table> to specify the table's heading.",
            "neuroHook": "🧠 <caption> = Label on the photo/table.",
            "neuroExplanation": "Structural label attachment to complex visual data.",
            "cognitiveTrap": "<title> is for the whole web page, <caption> is for tables."
        },
        {
            "id": "TB-CH04-10", "qnum": 10, "source": "Textbook Exercise", "chapter": 4, "chapterTitle": "Chapter 4: Lists and Tables in HTML",
            "question": "Which attribute of <ol> specifies the starting number of the list?",
            "options": {"A": "begin", "B": "from", "C": "start", "D": "value"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 4, Page 36",
            "textbookFact": "<ol start=\"5\"> causes the numbered list to commence at 5.",
            "neuroHook": "🧠 'start' tells where the countdown starts.",
            "neuroExplanation": "Sequence origin parameter.",
            "cognitiveTrap": "begin is not an HTML attribute; use start."
        },

        # Chapter 8: Charts in Calc
        {
            "id": "TB-CH08-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 8, "chapterTitle": "Chapter 8: Charts in Calc",
            "question": "Which tool in Calc is used to generate graphs from spreadsheet data?",
            "options": {"A": "Formula Wizard", "B": "Chart Wizard", "C": "Graph Maker", "D": "Plot Wizard"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 8, Page 130",
            "textbookFact": "The 'Chart Wizard' guides the user through 4 simple steps to produce charts.",
            "neuroHook": "🧠 Chart Wizard waves its wand to turn numbers into colorful graphs.",
            "neuroExplanation": "Wizard paradigm: Stepping through complex graphical configuration.",
            "cognitiveTrap": "The feature is called Chart Wizard, not Graph Maker."
        },
        {
            "id": "TB-CH08-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 8, "chapterTitle": "Chapter 8: Charts in Calc",
            "question": "How many steps are there in Calc's Chart Wizard?",
            "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 8, Page 131",
            "textbookFact": "Chart Wizard has 4 steps: 1. Chart Type, 2. Data Range, 3. Data Series, 4. Chart Elements.",
            "neuroHook": "🧠 4 Steps of Chart: 1-Type, 2-Range, 3-Series, 4-Elements.",
            "neuroExplanation": "Procedural schema chunked into a 4-item list in prefrontal memory.",
            "cognitiveTrap": "Do not confuse with 3 (Header areas); Chart Wizard has 4 steps."
        },
        {
            "id": "TB-CH08-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 8, "chapterTitle": "Chapter 8: Charts in Calc",
            "question": "Which chart type displays data as slices of a circular disk?",
            "options": {"A": "Bar chart", "B": "Column chart", "C": "Pie chart", "D": "Line chart"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 8, Page 132",
            "textbookFact": "A Pie chart represents portions of a 100% whole as angular slices.",
            "neuroHook": "🧠 Slicing a delicious round Pizza / Pie into percentage slices.",
            "neuroExplanation": "Gastronomic mental model for proportional part-to-whole relationships.",
            "cognitiveTrap": "Bar charts use horizontal bars; Pie uses circular slices."
        },
        {
            "id": "TB-CH08-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 8, "chapterTitle": "Chapter 8: Charts in Calc",
            "question": "Which chart type shows vertical rectangular bars to compare values across categories?",
            "options": {"A": "Column chart", "B": "Bar chart", "C": "Area chart", "D": "Net chart"},
            "answer": "A", "keyAnswer": "A",
            "textbookReference": "Chapter 8, Page 132",
            "textbookFact": "Column charts use vertical columns; Bar charts use horizontal bars.",
            "neuroHook": "🧠 Architectural Columns stand VERTICALLY like pillars.",
            "neuroExplanation": "Architectural pillar metaphor establishes vertical orientation.",
            "cognitiveTrap": "Bar charts are horizontal; Column charts are vertical."
        },
        {
            "id": "TB-CH08-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 8, "chapterTitle": "Chapter 8: Charts in Calc",
            "question": "What is the key or color guide identifying different data series in a chart called?",
            "options": {"A": "Title", "B": "Legend", "C": "Axis", "D": "Grid"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 8, Page 134",
            "textbookFact": "The Legend maps colors/symbols to the corresponding data series labels.",
            "neuroHook": "🧠 Legend decodes the secret colors on the map/chart.",
            "neuroExplanation": "Cartographic decoding schema in visual information processing.",
            "cognitiveTrap": "Gridlines are background lines; Legend is the color symbol key."
        },

        # Chapter 10: Introduction to C
        {
            "id": "TB-CH10-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 10, "chapterTitle": "Chapter 10: Introduction to C",
            "question": "Who developed the C programming language?",
            "options": {"A": "Dennis Ritchie", "B": "Ken Thompson", "C": "Bjarne Stroustrup", "D": "Bill Gates"},
            "answer": "A", "keyAnswer": "A",
            "textbookReference": "Chapter 10, Page 160",
            "textbookFact": "Dennis Ritchie created C at Bell Laboratories in 1972.",
            "neuroHook": "🧠 Dennis Ritchie gave birth to C at Bell Labs.",
            "neuroExplanation": "Biographical anchor in history of computing.",
            "cognitiveTrap": "Bjarne Stroustrup created C++; Dennis Ritchie created C."
        },
        {
            "id": "TB-CH10-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 10, "chapterTitle": "Chapter 10: Introduction to C",
            "question": "In which year and laboratory was the C language developed?",
            "options": {"A": "1969, IBM", "B": "1972, Bell Laboratories", "C": "1983, Microsoft", "D": "1991, CERN"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 10, Page 160",
            "textbookFact": "C was developed in 1972 at AT&T Bell Laboratories.",
            "neuroHook": "🧠 1972: Year C was born at Bell Labs.",
            "neuroExplanation": "Historical timestamp pair (1972 + Bell Labs).",
            "cognitiveTrap": "1991 was HTML at CERN; 1972 was C at Bell Labs."
        },
        {
            "id": "TB-CH10-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 10, "chapterTitle": "Chapter 10: Introduction to C",
            "question": "Every C program must contain which of the following essential functions?",
            "options": {"A": "start()", "B": "main()", "C": "run()", "D": "program()"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 10, Page 162",
            "textbookFact": "Execution of every C program always commences at the main() function.",
            "neuroHook": "🧠 main() is the Front Door where the computer enters the program.",
            "neuroExplanation": "Entry point execution schema.",
            "cognitiveTrap": "start() does not exist; main() is mandatory."
        },
        {
            "id": "TB-CH10-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 10, "chapterTitle": "Chapter 10: Introduction to C",
            "question": "Which character is used to terminate executable statements in C?",
            "options": {"A": "Colon (:)", "B": "Period (.)", "C": "Semicolon (;)", "D": "Comma (,)"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 10, Page 163",
            "textbookFact": "In C, every statement must end with a semicolon (;) as the statement terminator.",
            "neuroHook": "🧠 Semicolon (;) = The full-stop period of C language.",
            "neuroExplanation": "Syntactic punctuation rule in lexical analysis.",
            "cognitiveTrap": "Leaving out a semicolon causes the most infamous compiler error in C."
        },
        {
            "id": "TB-CH10-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 10, "chapterTitle": "Chapter 10: Introduction to C",
            "question": "What is the file extension of a C language source code file?",
            "options": {"A": ".cp", "B": ".c", "C": ".obj", "D": ".exe"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 10, Page 164",
            "textbookFact": "C source files have the extension '.c' (e.g., hello.c).",
            "neuroHook": "🧠 C language = .c extension.",
            "neuroExplanation": "Direct 1-letter extension identity.",
            "cognitiveTrap": ".obj is compiled object code; .c is source code."
        },

        # Chapter 11: Data Types and Operators in C
        {
            "id": "TB-CH11-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 11, "chapterTitle": "Chapter 11: Data Types and Operators in C",
            "question": "How many reserved keywords exist in standard ANSI C?",
            "options": {"A": "24", "B": "32", "C": "48", "D": "64"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 11, Page 175",
            "textbookFact": "ANSI C defines exactly 32 reserved keywords (int, float, if, for, while, return, etc.).",
            "neuroHook": "🧠 32 Teeth in your mouth = 32 Keywords in ANSI C.",
            "neuroExplanation": "Biological numerical peg: Aligning 32 adult teeth with 32 C keywords.",
            "cognitiveTrap": "Do not confuse with C++ (which has over 60 keywords)."
        },
        {
            "id": "TB-CH11-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 11, "chapterTitle": "Chapter 11: Data Types and Operators in C",
            "question": "Which data type in C is used to store floating-point decimal numbers?",
            "options": {"A": "int", "B": "char", "C": "float", "D": "void"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 11, Page 176",
            "textbookFact": "'float' stores single-precision decimal values (typically 4 bytes).",
            "neuroHook": "🧠 float = Floating decimal point.",
            "neuroExplanation": "IEEE 754 floating point mental model.",
            "cognitiveTrap": "int stores only whole integers, not decimals."
        },
        {
            "id": "TB-CH11-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 11, "chapterTitle": "Chapter 11: Data Types and Operators in C",
            "question": "What is the memory size of a 'char' data type in C?",
            "options": {"A": "1 byte", "B": "2 bytes", "C": "4 bytes", "D": "8 bytes"},
            "answer": "A", "keyAnswer": "A",
            "textbookReference": "Chapter 11, Page 176",
            "textbookFact": "A 'char' occupies exactly 1 byte (8 bits), holding values from -128 to 127 (or 0 to 255).",
            "neuroHook": "🧠 1 Single Letter = 1 Byte.",
            "neuroExplanation": "Unit byte identity for ASCII character representation.",
            "cognitiveTrap": "int is 2 or 4 bytes; char is strictly 1 byte."
        },
        {
            "id": "TB-CH11-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 11, "chapterTitle": "Chapter 11: Data Types and Operators in C",
            "question": "Which operator is used to calculate the remainder of an integer division in C?",
            "options": {"A": "/", "B": "%", "C": "#", "D": "\\"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 11, Page 180",
            "textbookFact": "The modulus operator (%) returns the remainder of integer division (e.g. 7 % 3 = 1).",
            "neuroHook": "🧠 % (Modulus) catches the leftover remainder.",
            "neuroExplanation": "Arithmetic remainder operator distinct from quotient operator.",
            "cognitiveTrap": "/ gives the quotient; % gives the remainder."
        },
        {
            "id": "TB-CH11-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 11, "chapterTitle": "Chapter 11: Data Types and Operators in C",
            "question": "Which of the following is the logical AND operator in C?",
            "options": {"A": "&", "B": "&&", "C": "AND", "D": "||"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 11, Page 182",
            "textbookFact": "'&&' is Logical AND (both conditions true); single '&' is bitwise AND.",
            "neuroHook": "🧠 Double Ampersand (&&) = Logical AND.",
            "neuroExplanation": "Short-circuit boolean logic token representation.",
            "cognitiveTrap": "Single & is bitwise, double && is boolean logical."
        },

        # Chapter 12: Control Structures in C
        {
            "id": "TB-CH12-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 12, "chapterTitle": "Chapter 12: Control Structures in C",
            "question": "Which loop in C is an exit-controlled loop that executes at least once?",
            "options": {"A": "for", "B": "while", "C": "do...while", "D": "switch"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 12, Page 200",
            "textbookFact": "do...while checks its condition at the end (exit-controlled), guaranteeing at least one execution.",
            "neuroHook": "🧠 'DO' first, ask questions 'WHILE' exiting! Guarantees at least 1 turn.",
            "neuroExplanation": "Post-test loop structure vs pre-test loop structure.",
            "cognitiveTrap": "while and for test conditions first; do-while tests at the end."
        },
        {
            "id": "TB-CH12-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 12, "chapterTitle": "Chapter 12: Control Structures in C",
            "question": "Which statement terminates a loop or switch block immediately?",
            "options": {"A": "continue", "B": "break", "C": "stop", "D": "exit"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 12, Page 203",
            "textbookFact": "The 'break' keyword halts the loop/switch immediately and jumps to the next statement.",
            "neuroHook": "🧠 BREAK smashes the loop and jumps outside.",
            "neuroExplanation": "Immediate control flow diversion to loop exit node.",
            "cognitiveTrap": "continue skips to next iteration; break terminates the entire loop."
        },
        {
            "id": "TB-CH12-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 12, "chapterTitle": "Chapter 12: Control Structures in C",
            "question": "Which statement skips the current iteration and jumps to the next cycle of the loop?",
            "options": {"A": "break", "B": "goto", "C": "continue", "D": "skip"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 12, Page 204",
            "textbookFact": "The 'continue' statement skips the remaining body statements of the current iteration and proceeds to the next loop evaluation.",
            "neuroHook": "🧠 CONTINUE says: 'Skip the rest of today, jump to tomorrow's round!'",
            "neuroExplanation": "Loop iteration increment bypass schema.",
            "cognitiveTrap": "Do not confuse break (stops all) with continue (skips one)."
        },
        {
            "id": "TB-CH12-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 12, "chapterTitle": "Chapter 12: Control Structures in C",
            "question": "Which branch is executed in a switch-case statement when no case value matches?",
            "options": {"A": "else", "B": "otherwise", "C": "default", "D": "fallback"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 12, Page 197",
            "textbookFact": "The 'default' label handles any input value that does not match any specified 'case'.",
            "neuroHook": "🧠 Default = Fallback safety net when nothing else matches.",
            "neuroExplanation": "Catch-all clause in multi-way dispatch tables.",
            "cognitiveTrap": "else belongs to if; default belongs to switch."
        },
        {
            "id": "TB-CH12-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 12, "chapterTitle": "Chapter 12: Control Structures in C",
            "question": "How many expressions does a standard for-loop header contain?",
            "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 12, Page 198",
            "textbookFact": "for (initialization; condition; increment/decrement) contains exactly 3 expressions.",
            "neuroHook": "🧠 3 parts of for(): 1. Start, 2. Check, 3. Step.",
            "neuroExplanation": "Ternary control loop header structure in procedural syntax.",
            "cognitiveTrap": "Do not count the curly braces; the loop header contains 3 semicolon-separated parts."
        },

        # Chapter 13: Arrays in C
        {
            "id": "TB-CH13-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 13, "chapterTitle": "Chapter 13: Arrays in C",
            "question": "What is an array in C?",
            "options": {
                "A": "A collection of variables of different data types",
                "B": "A collection of elements of the same data type stored in contiguous memory",
                "C": "A mathematical formula",
                "D": "A compiler directive"
            },
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 13, Page 215",
            "textbookFact": "An array is a fixed-size, sequenced collection of elements of the same data type stored in contiguous memory locations.",
            "neuroHook": "🧠 Array = Egg Carton. Identical slots in a continuous row.",
            "neuroExplanation": "Contiguous spatial memory representation.",
            "cognitiveTrap": "Structures store different types; Arrays store homogeneous (same) types."
        },
        {
            "id": "TB-CH13-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 13, "chapterTitle": "Chapter 13: Arrays in C",
            "question": "What is the index (subscript) of the very first element in a C array?",
            "options": {"A": "-1", "B": "0", "C": "1", "D": "any number"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 13, Page 216",
            "textbookFact": "C arrays are strictly 0-indexed; the first item is at index 0.",
            "neuroHook": "🧠 Index starts at ZERO: arr[0] is the firstborn.",
            "neuroExplanation": "Zero-offset memory addressing schema.",
            "cognitiveTrap": "Human counting starts at 1, but C array indexing starts at 0."
        },
        {
            "id": "TB-CH13-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 13, "chapterTitle": "Chapter 13: Arrays in C",
            "question": "If an array is declared as 'int marks[10];', what is the index of its last element?",
            "options": {"A": "10", "B": "9", "C": "11", "D": "8"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 13, Page 216",
            "textbookFact": "For an array of size N, valid indices range from 0 to N-1. Here, 10 - 1 = 9.",
            "neuroHook": "🧠 10 elements -> 0 through 9. Last is always N - 1.",
            "neuroExplanation": "Off-by-one boundary limit in zero-based indexing.",
            "cognitiveTrap": "marks[10] is an out-of-bounds error! Index 9 is the last valid slot."
        },
        {
            "id": "TB-CH13-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 13, "chapterTitle": "Chapter 13: Arrays in C",
            "question": "Which special character terminates a string in C?",
            "options": {"A": "\\n", "B": "\\t", "C": "\\0", "D": "\\b"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 13, Page 220",
            "textbookFact": "Strings in C are character arrays ending with the null terminator character '\\0'.",
            "neuroHook": "🧠 '\\0' = Null Terminator stop sign at the end of every string.",
            "neuroExplanation": "Sentinel value paradigm for unbounded sequential data.",
            "cognitiveTrap": "\\n is newline; \\0 is null terminator."
        },
        {
            "id": "TB-CH13-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 13, "chapterTitle": "Chapter 13: Arrays in C",
            "question": "Which header file must be included to use string functions like strlen() and strcpy()?",
            "options": {"A": "<stdio.h>", "B": "<math.h>", "C": "<string.h>", "D": "<conio.h>"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 13, Page 222",
            "textbookFact": "<string.h> contains prototypes for string manipulation functions.",
            "neuroHook": "🧠 String tools live inside <string.h>.",
            "neuroExplanation": "Modular standard library organization.",
            "cognitiveTrap": "<stdio.h> is for input/output (printf/scanf); <string.h> is for strings."
        },

        # Chapter 14: Functions in C
        {
            "id": "TB-CH14-01", "qnum": 1, "source": "Textbook Exercise", "chapter": 14, "chapterTitle": "Chapter 14: Functions in C",
            "question": "What is the primary benefit of dividing a large program into smaller functions?",
            "options": {
                "A": "Makes the program slower",
                "B": "Code reusability, modularity, and easier debugging",
                "C": "Increases memory consumption",
                "D": "Prevents compilation"
            },
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 14, Page 230",
            "textbookFact": "Modular programming divides tasks into self-contained functions, boosting readability and reusability.",
            "neuroHook": "🧠 Divide & Conquer: Break big problems into bite-sized function modules.",
            "neuroExplanation": "Cognitive chunking and working memory optimization in software engineering.",
            "cognitiveTrap": "Functions optimize structure, they do not slow programs down."
        },
        {
            "id": "TB-CH14-02", "qnum": 2, "source": "Textbook Exercise", "chapter": 14, "chapterTitle": "Chapter 14: Functions in C",
            "question": "What return type is used when a function returns no value to the caller?",
            "options": {"A": "null", "B": "empty", "C": "void", "D": "zero"},
            "answer": "C", "keyAnswer": "C",
            "textbookReference": "Chapter 14, Page 232",
            "textbookFact": "'void' indicates that the function performs actions but does not return a value.",
            "neuroHook": "🧠 VOID = The empty void that returns nothing.",
            "neuroExplanation": "Absence of value representation in type system.",
            "cognitiveTrap": "null is a pointer value; void is the function return type."
        },
        {
            "id": "TB-CH14-03", "qnum": 3, "source": "Textbook Exercise", "chapter": 14, "chapterTitle": "Chapter 14: Functions in C",
            "question": "What are the variables declared inside a function header called?",
            "options": {"A": "Actual parameters", "B": "Formal parameters", "C": "Global variables", "D": "Constants"},
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 14, Page 234",
            "textbookFact": "Parameters defined in the function definition/header are 'formal parameters'; values passed in the call are 'actual parameters'.",
            "neuroHook": "🧠 Formal in the definition; Actual in the calling function.",
            "neuroExplanation": "Role distinction between parameter definition vs argument instantiation.",
            "cognitiveTrap": "Actual arguments are passed during the call; formal parameters receive them."
        },
        {
            "id": "TB-CH14-04", "qnum": 4, "source": "Textbook Exercise", "chapter": 14, "chapterTitle": "Chapter 14: Functions in C",
            "question": "What is a function prototype?",
            "options": {
                "A": "The actual execution body",
                "B": "A forward declaration stating the function's name, return type, and parameter types",
                "C": "A comment in the program",
                "D": "An operating system command"
            },
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 14, Page 233",
            "textbookFact": "A prototype declares the function's signature before its actual definition so the compiler knows how to validate calls.",
            "neuroHook": "🧠 Prototype = ID Card introducing the function to the compiler ahead of time.",
            "neuroExplanation": "Lookahead parsing declaration in single-pass compilers.",
            "cognitiveTrap": "Prototype is just the header declaration followed by a semicolon (;)."
        },
        {
            "id": "TB-CH14-05", "qnum": 5, "source": "Textbook Exercise", "chapter": 14, "chapterTitle": "Chapter 14: Functions in C",
            "question": "What is the scope of a variable declared inside a function?",
            "options": {
                "A": "Global (accessible everywhere)",
                "B": "Local (accessible only within that function)",
                "C": "Accessible across all files",
                "D": "Permanent"
            },
            "answer": "B", "keyAnswer": "B",
            "textbookReference": "Chapter 14, Page 236",
            "textbookFact": "Local variables exist on the stack and can only be accessed within the enclosing block/function.",
            "neuroHook": "🧠 Local = Stays inside its own house (function).",
            "neuroExplanation": "Encapsulation boundary preventing variable collision across call stacks.",
            "cognitiveTrap": "Global variables are outside all functions; local variables are inside."
        }
    ]

    print(f"Loaded textbook exercise questions. Total: {len(tb_questions)}")
    return tb_questions

if __name__ == "__main__":
    tb = get_textbook_exercises()
