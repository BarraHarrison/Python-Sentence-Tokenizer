from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/static/index.html'  # Serve the index.html from the static directory
        return super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = dict(x.split('=') for x in post_data.split('&'))
        paragraph = params.get('paragraph', '')

        tokenized_output = self.sentence_to_word_tokenizer(paragraph)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(tokenized_output.encode('utf-8'))

    def sentence_to_word_tokenizer(self, paragraph):
        sentences = paragraph.split('.')
        tokenized_sentences = []
        for i, sentence in enumerate(sentences):
            sentence = sentence.strip()
            if sentence:
                words = sentence.split()
                tokenized_sentences.append(f"Sentence {i + 1}: {words}")
        return "\n".join(tokenized_sentences)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Ensure correct working directory
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CustomHandler)
    print("Server started at http://localhost:8000")
    httpd.serve_forever()
