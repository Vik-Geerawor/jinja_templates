from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    templates = "templates"
    # specify the templates directory
    file_loader = FileSystemLoader(templates)
    print(f"{type(file_loader)}: {file_loader=}")

    # load environment
    env = Environment(loader=file_loader)
    print(f"{type(env)}: {env=}")

    # load the template
    template = "hello.txt"
    template = env.get_template(template)
    print(f"{type(template)}: {template=}")

    # render template
    output = template.render()
    print(output)
