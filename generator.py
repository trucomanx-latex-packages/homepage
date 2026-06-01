#!/usr/bin/python3

from text_template_engine.renderer import render_string, render_file

bloque_str="""
<div class="header libgradient bloque">
<div>
<h2>{{package}}</h2>
<p>
Download the latex package of {{package}} from
<a href="https://github.com/trucomanx-latex-packages/{{package}}">this link</a>
</p>
</div>
<img src="https://github.com/trucomanx-latex-packages/{{package}}/raw/master/screenshot.png"/>
</div>
"""

data_list=[ 
    {
        "title": "Background Images",
        "description": "Packages with commands to draw background images.",
        "packages": [
            "background-images"
        ]
    },
    {
        "title": "Catalographic Card",
        "description": "Packages with commands to generate catalog cards.",
        "packages": [
            "catalographic-card"
        ]
    },
    {
        "title": "Chapter title",
        "description": "Packages with commands to modify the <b>chapter</b> command.",
        "packages": [
            "chapter-format-formalbar",
            "chapter-format-formaltitle",
            "chapter-format-leftrule",
            "chapter-format-middlerule",
            "chapter-format-rightbar",
            "chapter-format-rightbar-text",
            "chapter-format-rightrule",
            "chapter-format-roundedtitle",
            "chapter-format-tworules",
            "chapter-format-upperbanner"
            ]
    },
    {
        "title": "Section title",
        "description": "Packages with commands to modify the <b>section</b> command.",
        "packages": [
            "section-format-simplecolor",
            "section-format-simpleline"
            ]
    },
    {
        "title": "Environment Box",
        "description": "Packages with environments to generate many types of boxes, like theorems, examples, information, etc.",
        "packages": [
            "env-box-formaltab",
            "env-box-insidetab",
            "env-box-notehor",
            "env-box-oddtab",
            "env-box-pictbox",
            "env-box-pictlin",
            "env-box-ribontab",
            "env-box-simple",
            "env-box-simplebox",
            "env-box-simpleimg",
            "env-box-simpleripple"
            ]
    },
    {
        "title": "Environment Bullet",
        "description": "Packages with environments to generate bullets.",
        "packages": [
            "env-bulletjournalarrow",
            "env-bulletjournalitem",
            "env-bulletjournalpicture",
            "env-bulletjournalribon"
        ]
    
    },
    {
        "title": "Environment Highlight",
        "description": "Packages with environments to highlight text; this type of environment does not have a number.",
        "packages": [
            "env-highlight-brokenpage",
            "env-highlight-foldedcorner",
            "env-highlight-multipleimg",
            "env-highlight-simpleimg",
            "env-highlight-simplenote",
            "env-highlight-simpleround",
            "env-highlight-simplezigzag",
            "env-highlight-tornoff"
        ]
    },
    {
        "title": "Environment Phrase",
        "description": "Packages with environments to display quotes and phrases.",
        "packages": [
            "env-phrasebox-ripple",
            "env-phrasebox-simple",
            "env-phrasebox-tab"
        ]
    },
    {
        "title": "Environment Wrapper",
        "description": "Packages with commands for wrapping text.",
        "packages": [
            "wrapper-breakable",
            "wrapper-variable"
        ]
    },
    {
        "title": "Lua Poems",
        "description": "Package with commands to display poems.",
        "packages": [
            "luapoemformats"
        ]
    },
    {
        "title": "Math Macros",
        "description": "Package with commands to display mathematical expressions.",
        "packages": [
            "math-macros"
        ]
    },
    {
        "title": "Ornamental breaks",
        "description": "Package with commands for displaying ornamental breaks.",
        "packages": [
            "ornamental-break-asterisks",
            "separator-rule"
        ]
    }
]

res = ""
for data in data_list:
    res += "\n"
    res += "<center><h1>"+data["title"]+"</h1></center>\n"
    res += "<p>"+data["description"]+"</p>\n"
    
    for package in data["packages"]:
        variables={"package": package}
        res += render_string(bloque_str, variables)+"\n"


render_file("template.html", "index.html", {"body": res})
