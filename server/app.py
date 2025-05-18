from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    interests = data.get('interests', '').lower()

    if 'design' in interests:
        careers = [
            'UI/UX Designer',
            'Graphic Designer',
            'Product Designer',
            'Motion Graphics Designer',
            'Interior Designer'
        ]
    elif 'data' in interests or 'analytics' in interests:
        careers = [
            'Data Analyst',
            'Data Scientist',
            'Machine Learning Engineer',
            'Business Intelligence Analyst',
            'Statistician'
        ]
    elif 'code' in interests or 'software' in interests or 'developer' in interests:
        careers = [
            'Software Engineer',
            'Backend Developer',
            'Full Stack Developer',
            'Mobile App Developer',
            'DevOps Engineer'
        ]
    elif 'business' in interests or 'management' in interests or 'marketing' in interests:
        careers = [
            'Business Analyst',
            'Product Manager',
            'Digital Marketing Specialist',
            'Sales Executive',
            'HR Manager'
        ]
    elif 'finance' in interests or 'accounting' in interests or 'investment' in interests:
        careers = [
            'Financial Analyst',
            'Accountant',
            'Investment Banker',
            'Auditor',
            'Risk Manager'
        ]
    elif 'health' in interests or 'medicine' in interests or 'biology' in interests:
        careers = [
            'Medical Researcher',
            'Healthcare Administrator',
            'Pharmacist',
            'Nurse',
            'Physiotherapist'
        ]
    elif 'teaching' in interests or 'education' in interests or 'tutor' in interests:
        careers = [
            'School Teacher',
            'College Lecturer',
            'Corporate Trainer',
            'Online Educator',
            'Education Consultant'
        ]
    elif 'dancing' in interests or 'dance' in interests:
        careers = [
            'Professional Dancer',
            'Choreographer',
            'Dance Instructor',
            'Dance Therapist',
            'Performing Artist'
        ]
    elif 'yoga' in interests:
        careers = [
            'Yoga Instructor',
            'Wellness Coach',
            'Physical Therapist',
            'Meditation Trainer',
            'Health Consultant'
        ]
    elif 'singing' in interests or 'singer' in interests or 'music' in interests:
        careers = [
            'Professional Singer',
            'Music Teacher',
            'Voice Trainer',
            'Music Therapist',
            'Sound Engineer'
        ]
    elif 'chef' in interests or 'cooking' in interests or 'culinary' in interests:
        careers = [
            'Professional Chef',
            'Pastry Chef',
            'Food Critic',
            'Culinary Instructor',
            'Restaurant Manager'
        ]
    else:
        careers = [
            'Software Engineer',
            'Content Creator',
            'Technical Writer',
            'Consultant',
            'Entrepreneur'
        ]

    return jsonify({'careers': careers})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    app.run(debug=True)
