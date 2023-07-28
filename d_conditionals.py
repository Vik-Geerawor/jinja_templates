from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    templates = "templates"
    # specify the templates directory
    file_loader = FileSystemLoader(templates)

    # load environment
    env = Environment(loader=file_loader)

    # load the template
    template = "conditions.j2"
    template = env.get_template(template)

    # render template
    output = template.render(flag=False)
    print(output)
