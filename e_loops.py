from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    templates = "templates"
    # specify the templates directory
    file_loader = FileSystemLoader(templates)

    # load environment
    env = Environment(loader=file_loader)

    # load the template
    template = "loops.j2"
    template = env.get_template(template)

    # render template
    rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
    output = template.render(colors=rainbow)

    print(output)
