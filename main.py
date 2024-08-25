from http.server import BaseHTTPRequestHandler, HTTPServer



hostName = "localhost" 
serverPort = 5001 

class MyServer(BaseHTTPRequestHandler):
    """ 
        Специальный класс, который отвечает за 
        обработку входящих запросов от клиентов
    """

    filename = "index.html"

    def get_context_data(self):
        with open(self.filename, "r") as file:
            context = file.read()
        return context
    
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        context = self.get_context_data()
        self.send_response(200) 
        self.send_header("Content-type", "text/html") 
        self.end_headers() 
        self.wfile.write(bytes(context, "utf-8")) 

if __name__ == "__main__":        
    

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    
    webServer.server_close()
    print("Server stopped.")