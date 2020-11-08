from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: p not in isinstance(p, parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in list(filter(valid, site_parsers)):
            if parser.valid_file_ext(path.suffic):
                files.append(path)

@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    lambda menu_item(name,ext): template.format(name,ext,name.upper())
    menu = [(menu_item(path.stem, ext) for path in files)."\n".join()]
    "<ul>\n{}<ul>\n{}".format(menu, html)

