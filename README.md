# Smart Diabetes Bracelet System

A comprehensive software system for monitoring and managing diabetes through a smart bracelet device.

## Features

- Real-time health metrics monitoring (blood glucose, heart rate, body temperature)
- Secure data storage and management
- Interactive web dashboard for patients and healthcare providers
- Automated alerts for abnormal glucose levels
- Data visualization and trend analysis
- (Optional) AI-powered health recommendations

## Project Structure

```
smart-diabetes-bracelet/
├── manage.py              # Django management script
├── diabetes_bracelet/     # Main project directory
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── apps/                  # Django applications
│   ├── users/            # User management app
│   ├── devices/          # Device management app
│   ├── metrics/          # Health metrics app
│   └── dashboard/        # Dashboard app
├── static/               # Static files
├── templates/            # HTML templates
├── requirements.txt      # Python dependencies
└── docs/                # Documentation
```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Applications

### Users App
- User authentication and authorization
- Role-based access control (Patient/Doctor)
- User profiles and settings

### Devices App
- Device registration and management
- Device data collection
- Device status monitoring

### Metrics App
- Health metrics storage
- Data processing and analysis
- Alert generation

### Dashboard App
- Data visualization
- Real-time monitoring
- Reports and analytics

## Security

- All data is encrypted at rest and in transit
- Django's built-in security features
- Role-based access control
- Regular security audits and updates

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 