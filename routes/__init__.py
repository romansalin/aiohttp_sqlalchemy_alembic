import os


def apply_routes(app):

    for file in [file for file in os.listdir(app.config['root_path'] + "/routes/") if file != '__pycache__' and file != '__init__.py']:
        p, m = file.rsplit('.', 1)
        module_in_file = __import__("routes." + str(p))
        files_module = getattr(module_in_file, p)
        init = getattr(files_module, 'init')
        if "init" in dir():
            init(app)
            del init

    media = str(app.config['root_path']) + '/public/media'
    app.router.add_static("/media/",
                          path=str(media),
                          name="media")

    static = str(app.config['root_path']) + "/public/static"
    app.router.add_static("/",
                          path=str(static),
                          name="static")
