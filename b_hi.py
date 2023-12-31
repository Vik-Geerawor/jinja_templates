from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    # specify the templates directory
    templates = "templates"
    file_loader = FileSystemLoader(templates)

    # load environment
    env = Environment(loader=file_loader)

    # load the template
    template = "hi.txt"
    template = env.get_template(template)

    # render template
    output = template.render(name="Jason")
    print(output)
