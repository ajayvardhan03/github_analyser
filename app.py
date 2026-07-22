from flask import Flask, request, Response
from flask_cors import cross_origin

from analyze import AnalyzeRepo

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
@cross_origin()  # Avoid CORS errors
def process():

    if request.method == "GET":
        return "Open Github Repository and Check the Extension"
    data = request.get_json()
    openai_key = data.get("openaiKey")
    currentPageLink = data.get("currentPageLink")

    try:
        # Call AnalyzeRepo and get detailed summary
        summary_generator = AnalyzeRepo(openai_key, currentPageLink)
        result = summary_generator.run()
        # result is HTML generated from the LLM's summary of arbitrary repo
        # code, so it must not be run through Jinja2 (render_template_string
        # would execute any {{ }} / {% %} syntax it happened to contain).
        return Response(result, mimetype="text/html")
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
