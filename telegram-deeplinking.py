from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:8000/resolve?link=https://telegram.me/BotFather?start=123q124


@app.route('/resolve', methods=['GET'])
def display_link():
    link = request.args.get('link')
    base_url = link.split('/')[-1]
    if '?' in base_url:
        bot_name, command = base_url.split('?')
        result_link = '<a href="tg://resolve?domain={}&{}">Открыть в Telegram</a>'.format(bot_name, command)
    else:
        result_link = '<a href="tg://resolve?domain={}">Открыть в Telegram</a>'.format(base_url)
    return result_link





if __name__ == '__main__':
    app.run(port=8000, debug=True)
