from flask import Flask, render_template, request, jsonify
from simulator import Simulator

app = Flask(__name__)
simulator = Simulator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    action = data.get('action')
    floor = data.get('floor')
    elevator = data.get('elevator')
    direction = data.get('direction')

    if action == 'call':
        simulator.call_elevator(floor, direction)
    elif action == 'select':
        simulator.select_floor(elevator, floor)

    simulator.update()
    return jsonify(simulator.get_state())

if __name__ == '__main__':
    app.run(debug=True)