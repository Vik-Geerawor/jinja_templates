from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    # specify the templates directory
    templates = "templates"
    file_loader = FileSystemLoader(templates)

    # load environment
    env = Environment(loader=file_loader)

    # create header.html
    # create base.html, include header.html within, extending base

    # load the template
    template = "index.html"
    template = env.get_template(template)

    # render template
    data = {}
    data["title"] = "MyJinja"
    data["heading"] = "*** My Jinja Moves ***"
    data["body"] = "How d'you like that..!?"
    output = template.render(content=data)

    # write to a file
    with open("home.html", "w") as f:
        print(output, file=f)

    print(f"homepage created: home.html")
