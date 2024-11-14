from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route for the algorithm endpoint (POST)
@app.route('/run_algorithm', methods=['POST'])

def run_algorithm():
    data = request.json  # Retrieve JSON data from the request
    result = sort_selection(data['input'])
    return jsonify({"result": result})

# Route to serve the front-end HTML page (GET)
@app.route('/', methods=['GET'])

def home():
    return render_template('index.html')

# Selection sort algorithm function
def sort_selection(input_data):
    nums = input_data.copy()
    sorted_array = []
    while len(nums) > 0:
        smallest = nums[0]
        for x in nums:
            if x < smallest:
                smallest = x
        sorted_array.append(smallest)
        nums.remove(smallest)
    return sorted_array

if __name__ == '__main__':
    app.run()
