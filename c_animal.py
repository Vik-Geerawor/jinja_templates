from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    templates = "templates"
    # specify the templates directory
    file_loader = FileSystemLoader(templates)

    # load environment
    env = Environment(loader=file_loader)

    # load the template
    template = "animal.txt"
    template = env.get_template(template)

    # render template
    # a dict to be passed to render
    person = {}
    person["name"] = "Mary"
    person["animal"] = "lamb"
    output = template.render(data=person)
    print(output)
