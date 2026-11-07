from flask import Flask, render_template, request

# Brackets: first $18,750 at 4.7%, next $44,500 at 9.3%
# and income over $63,250 at 15.8%

app = Flask("app")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    income_text = request.form.get("income", "")

    try:
        income = float(income_text)
    except ValueError:
        return render_template("result.html", error="Please enter a number.")

    if income < 0:
        return render_template(
            "result.html",
            error="Income cannot be negative."
        )

    if income <= 18750:
        tax = income * 0.047
    elif income <= 63250:
        tax = (18750 * 0.047) + ((income - 18750) * 0.093)
    else:
        tax = (18750 * 0.047) + (44500 * 0.093) + ((income - 63250) * 0.158)

    income = f"${income:,.2f}"
    tax = f"${tax:,.2f}"

    return render_template("result.html", income=income, tax=tax)


app.run()