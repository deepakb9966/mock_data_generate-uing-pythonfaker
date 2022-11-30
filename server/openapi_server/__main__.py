#!/usr/bin/env python3

import connexion

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'mockdata OpenAPI'},
                pythonic_params=True)

    # app.run(port=8080)http://127.0.0.1:8080/ui/
    from waitress import serve
    app.debug = True
    print("server run at http://localhost:{port}".format(port=8080))
    # serve.print_listen("Serving on http://{}:{}")
    print(serve(app, host="0.0.0.0", port=8080))


if __name__ == '__main__':
    main()
