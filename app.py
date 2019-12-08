from flask import Flask
from faker import Faker
import pttcrawler.nbacrawler as nba

app = Flask(__name__)  # __name__ 代表目前執行的模組

fakerTest3 = Faker()
# fakerTest3 = Faker("zh_TW")


@app.route("/")  # function 的裝飾(Decorator), 以函式為基礎,提供附加的功能
def index():
    return "<H1>hello Grand Maison TOKYO 2020</H1>"


@app.route("/ptt")  # function 的裝飾(Decorator), 以函式為基礎,提供附加的功能
def home():
    return nba.getPttNBATitles("https://www.ptt.cc/bbs/NBA/index6495.html")


@app.route("/about")
def test():
    return "<H3>About " + fakerTest3.name() + "</H3>"


if __name__ == "__main__":  # 如果以主程式執行
    app.run(host="0.0.0.0", debug=True)  # 立刻啟動伺服器
