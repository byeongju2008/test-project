from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 상단 고정 배지
default_skills = ["python", "sql", "html", "bash"]

# 서버 실행 중에만 유지되는 메모리 저장소
messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        skill = request.form.get("skill", "").strip()
        # 빈 값 예외 처리 및 리스트 추가
        if skill and skill not in messages:
            messages.append(skill)
        return redirect("/") # [수행평가 기준] 리다이렉트
    
    # 데이터 전달
    return render_template("index.html", default_skills=default_skills, messages=messages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)