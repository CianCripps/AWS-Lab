from flask import Flask, render_template
import random

app = Flask(__name__)

# Generate random data
def generate_random_data():
    data = [random.randint(1, 100) for _ in range(100)]
    return data

# Calculate statistics from the data
def calculate_statistics(data):
    total = sum(data)
    minimum = min(data)
    maximum = max(data)
    average = round(sum(data) / len(data), 2)
    return {
        'total': total,
        'minimum': minimum,
        'maximum': maximum,
        'average': average
    }

# Route to display statistics
@app.route('/')
def statistics():
    random_data = generate_random_data()
    stats = calculate_statistics(random_data)
    return render_template('statistics.html', data=random_data, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
