# Extracted from https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
cool.app.run(
    host=cool.app.config.get("HOST", "localhost"),
    port=cool.app.config.get("PORT", 9000)
)            

