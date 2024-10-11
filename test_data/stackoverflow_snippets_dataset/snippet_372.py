# Extracted from https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')


