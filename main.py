from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    """
    Класс для создания веб-приложения с разными товарами, формой регистрации и FAQ
    """
    def open_indexhtml(self):
        """
        Функция для открытия файла
        :return:
        """
        with open('index.html', encoding='utf-8') as file:
            text = file.read()
        return text

    def do_GET(self):
        """
        Функция для get-запроса
        :return:
        """
        page_content = self.open_indexhtml()
        self.send_response(200)
        self.send_header("Content_type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, 'utf-8'))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")