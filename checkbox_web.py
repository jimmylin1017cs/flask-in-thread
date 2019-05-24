from flask import Flask, render_template, Response, g, request

import cv2
import time
import threading

class CheckBoxServer(threading.Thread):

    app = Flask(__name__)

    def __init__(self, host, port):
        threading.Thread.__init__(self)

        self.host = host
        self.port = port
        self.name_list = list()
        self.enable_list = list()

    @app.route('/', methods=['GET', 'POST'])
    def index(self):
        g.name_list = self.name_list
        print(request.form.getlist("person"))
        g.enable_list = list(map(int, request.form.getlist("person")))
        return render_template("stream.html")

    def update_name_list(self, name_list):
        self.name_list = name_list

    @app.route('/select', methods=['GET', 'POST'])
    def select():
        return Response(gen())

    def gen():
        return "SELECT"

    def run(self):
        self.app.run(host=self.host, port=self.port, threaded=True, debug=True, use_reloader=False)

if __name__ == "__main__":
    
    host = "0.0.0.0"
    port = 8091

    cbs = CheckBoxServer(host, port)

    cbs.update_name_list([1, 2])
    
    cbs.start()
